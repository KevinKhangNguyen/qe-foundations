"""qe_foundations.utils - helpers for building and checking QA test data."""

from qe_foundations.utils.strings import slugify, normalize_whitespace, is_valid_email
from qe_foundations.utils.numbers import is_positive_int, clamp, percent
from qe_foundations.utils.dates import add_days, is_weekend, timestamp_for_filename
from qe_foundations.utils.data_gen import FIRST_NAMES, ROLES, make_users

__all__ = [
    "slugify",
    "normalize_whitespace",
    "is_valid_email",
    "is_positive_int",
    "clamp",
    "percent",
    "add_days",
    "is_weekend",
    "timestamp_for_filename",
    "make_users",
]