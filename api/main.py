"""Local teaching API. Independent from Django accounts; bind to loopback."""
import os
import sqlite3
from contextlib import asynccontextmanager, closing
from pathlib import Path
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query, Response
from pydantic import BaseModel, Field, ConfigDict

DB_PATH = Path(os.environ.get('FASTAPI_DB_PATH', 'api-observations.sqlite3'))


def connection():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db


def initialize():
    with closing(connection()) as db, db:
        db.execute('CREATE TABLE IF NOT EXISTS observations (id INTEGER PRIMARY KEY, title TEXT NOT NULL, value REAL NOT NULL, notes TEXT NOT NULL)')


@asynccontextmanager
async def lifespan(app):
    initialize()
    yield


app = FastAPI(title='Observation Laboratory API', version='1.0', lifespan=lifespan,
              description='Local educational REST service. Separate data store from Django. No authentication: keep on loopback.')


class ObservationInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra='forbid')
    title: str = Field(min_length=3, max_length=100)
    value: float = Field(ge=0, le=999999.99, allow_inf_nan=False)
    notes: str = Field(default='', max_length=2000)


class ObservationOutput(ObservationInput):
    id: int


@app.get('/health')
async def health():
    return {'status': 'ok'}


@app.get('/observations', response_model=list[ObservationOutput])
def list_observations(min_value: Annotated[float, Query(ge=0)] = 0,
                      limit: Annotated[int, Query(ge=1, le=100)] = 50):
    with closing(connection()) as db:
        return [dict(row) for row in db.execute('SELECT * FROM observations WHERE value >= ? ORDER BY id LIMIT ?', (min_value, limit))]


@app.post('/observations', response_model=ObservationOutput, status_code=201)
def create_observation(data: ObservationInput, response: Response):
    with closing(connection()) as db, db:
        cursor = db.execute('INSERT INTO observations(title,value,notes) VALUES (?,?,?)', (data.title, data.value, data.notes))
        result = {**data.model_dump(), 'id': cursor.lastrowid}
    response.headers['Location'] = f'/observations/{result["id"]}'
    return result


@app.get('/observations/{observation_id}', response_model=ObservationOutput)
def get_observation(observation_id: int):
    with closing(connection()) as db:
        row = db.execute('SELECT * FROM observations WHERE id=?', (observation_id,)).fetchone()
    if row is None:
        raise HTTPException(404, 'Observation not found')
    return dict(row)


@app.put('/observations/{observation_id}', response_model=ObservationOutput)
def replace_observation(observation_id: int, data: ObservationInput):
    with closing(connection()) as db, db:
        cursor = db.execute('UPDATE observations SET title=?,value=?,notes=? WHERE id=?', (data.title, data.value, data.notes, observation_id))
        if cursor.rowcount == 0:
            raise HTTPException(404, 'Observation not found')
    return {**data.model_dump(), 'id': observation_id}


@app.delete('/observations/{observation_id}', status_code=204)
def delete_observation(observation_id: int):
    with closing(connection()) as db, db:
        cursor = db.execute('DELETE FROM observations WHERE id=?', (observation_id,))
        if cursor.rowcount == 0:
            raise HTTPException(404, 'Observation not found')
    return Response(status_code=204)
