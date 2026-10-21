"""qe_foundations/ingestion/validation.py  -  TASK 5 (about 25 min)

validate_record() decides whether ONE raw record is acceptable.

IMPORTANT: this is VALIDATION OF EXTERNAL DATA. Raise exceptions here.
Do NOT use `assert` in this file (assertions can be switched off with `python -O`).
See README Task 5 for the exact rules.
"""
import math
from .exceptions import InvalidValueError, MissingFieldError

REQUIRED_FIELDS = ("id", "title", "status", "duration")
VALID_STATUSES = ("pass", "fail", "blocked")


def validate_record(row, raw):
    """Turn one raw record into a clean dict, or raise a RecordValidationError.

    row : 1-based record number in the file (used in error messages)
    raw : whatever the reader produced for that record (usually a dict)

    Returns {"id": str, "title": str, "status": str, "duration": float}.
    """
    if not isinstance(raw, dict):
        raise InvalidValueError(row, "record", raw, "an object with the test fields")

    for name in REQUIRED_FIELDS:
        value = raw.get(name)
        if value is None or str(value).strip() == "":
            raise MissingFieldError(row, name)

    clean_id = str(raw["id"]).strip()
    clean_title = str(raw["title"]).strip()

    status_raw = str(raw["status"]).strip()
    clean_status = status_raw.lower()
    if clean_status not in VALID_STATUSES:
        raise InvalidValueError(row, "status", raw["status"], f"one of {VALID_STATUSES}")

    dur_raw = raw["duration"]
    if isinstance(dur_raw, bool):
        raise InvalidValueError(row, "duration", dur_raw, "a finite number >= 0")
    try:
        duration_float = float(dur_raw)
    except (ValueError, TypeError) as error:
        raise InvalidValueError(row, "duration", dur_raw, "a finite number >= 0") from error

    if not math.isfinite(duration_float) or duration_float < 0:
        raise InvalidValueError(row, "duration", dur_raw, "a finite number >= 0")

    return {
        "id": clean_id,
        "title": clean_title,
        "status": clean_status,
        "duration": duration_float,
    } 