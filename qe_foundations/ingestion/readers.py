"""qe_foundations/ingestion/readers.py  -  TASK 4 (about 35 min)

One reader per format. Each returns a LIST OF RAW RECORDS and only deals with
FORMAT problems (is this valid CSV / JSON / XML? are the columns there?).
Business rules (is the status allowed? is the duration negative?) belong to
validation.py, NOT here.

Always open files through open_source() from contexts.py.
See README Task 4 for the exact contract of each reader.
"""

import csv
import json
import xml.etree.ElementTree as ET

from .contexts import open_source
from .exceptions import MalformedSourceError, MissingColumnsError
from .validation import REQUIRED_FIELDS


def read_csv_records(path):
    """CSV -> list of raw dicts, one per data row (use csv.DictReader)."""
    with open_source(path) as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        if fieldnames is None:
            raise MissingColumnsError(path, list(REQUIRED_FIELDS))
        missing = [f for f in REQUIRED_FIELDS if f not in fieldnames]
        if missing:
            raise MissingColumnsError(path, missing)
        return list(reader)


def read_json_records(path):
    """JSON -> list of raw records. Expected shape: {"suite": ..., "tests": [...]}."""
    try:
        with open_source(path) as handle:
            data = json.load(handle)
    except json.JSONDecodeError as error:
        raise MalformedSourceError(path, f"invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}") from error

    if not isinstance(data, dict):
        raise MalformedSourceError(path, "JSON root must be an object")
    if "tests" not in data or not isinstance(data["tests"], list):
        raise MalformedSourceError(path, "JSON missing 'tests' list")
    return data["tests"]


def read_xml_records(path):
    """XML -> list of raw dicts, one per <testcase> element at ANY depth."""
    try:
        with open_source(path) as handle:
            tree = ET.parse(handle)
            root = tree.getroot()
    except ET.ParseError as error:
        raise MalformedSourceError(path, f"invalid XML: {error}") from error

    records = []
    for case in root.iter("testcase"):
        records.append({
            "id": case.get("id"),
            "status": case.get("status"),
            "title": case.findtext("title"),
            "duration": case.findtext("duration"),
        })
    return records
