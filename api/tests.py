import pytest
from fastapi.testclient import TestClient
from api import main

@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(main, 'DB_PATH', tmp_path / 'test.sqlite3')
    with TestClient(main.app) as client:
        yield client


def test_resource_lifecycle(client):
    response = client.post('/observations', json={'title': 'Latency', 'value': 12})
    assert response.status_code == 201
    key = response.json()['id']
    assert response.headers['location'] == f'/observations/{key}'
    assert client.get(f'/observations/{key}').json()['value'] == 12
    assert client.get('/observations?min_value=13').json() == []
    assert client.put(f'/observations/{key}', json={'title': 'Updated', 'value': 15}).json()['title'] == 'Updated'
    assert client.delete(f'/observations/{key}').status_code == 204
    assert client.get(f'/observations/{key}').status_code == 404


@pytest.mark.parametrize('data', [{'title': 'x', 'value': 1}, {'title': 'Valid', 'value': -1}, {'title': '   ', 'value': 1}, {'title': 'Valid', 'value': 1, 'unknown': 2}])
def test_invalid_body(client, data):
    assert client.post('/observations', json=data).status_code == 422
    assert client.get('/observations').json() == []


def test_errors_and_openapi(client):
    assert client.get('/observations?min_value=-1').status_code == 422
    assert client.get('/observations?limit=101').status_code == 422
    assert client.get('/observations/nope').status_code == 422
    assert client.put('/observations/999', json={'title': 'Missing', 'value': 1}).status_code == 404
    assert client.delete('/observations/999').status_code == 404
    assert client.get('/openapi.json').json()['info']['title'] == 'Observation Laboratory API'
    assert client.get('/docs').status_code == 200
    assert client.get('/health').json() == {'status': 'ok'}


def test_persistence_across_clients(client):
    key = client.post('/observations', json={'title': 'Persisted', 'value': 3}).json()['id']
    with TestClient(main.app) as second:
        assert second.get(f'/observations/{key}').json()['title'] == 'Persisted'
