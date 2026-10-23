import csv
import io
from decimal import Decimal, InvalidOperation
from django.core.exceptions import ValidationError
from django.db import transaction
from .forms import ObservationForm
from .models import Observation


def import_csv(upload, owner):
    if upload.size > 1_000_000:
        raise ValidationError('CSV exceeds 1 MB.')
    try:
        reader = csv.DictReader(io.StringIO(upload.read().decode('utf-8-sig')))
        if reader.fieldnames != ['title', 'value', 'notes']:
            raise ValidationError('Expected columns: title,value,notes (in that order).')
        records = []
        for line, row in enumerate(reader, 2):
            if len(records) >= 500:
                raise ValidationError('Import at most 500 rows.')
            form = ObservationForm(row)
            if None in row or not form.is_valid():
                raise ValidationError(f'Row {line}: invalid title, value or columns.')
            record = form.save(commit=False)
            record.owner = owner
            records.append(record)
        if not records:
            raise ValidationError('The file has no observations.')
    except (UnicodeDecodeError, csv.Error, ValueError) as exc:
        raise ValidationError('Use a valid UTF-8 CSV file.') from exc
    with transaction.atomic():
        Observation.objects.bulk_create(records)
    return len(records)


def csv_cell(value):
    value = str(value)
    return "'" + value if value.startswith(('=', '+', '-', '@', '\t', '\r')) else value
