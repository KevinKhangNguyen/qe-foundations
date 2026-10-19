# QE Foundations

A Python package providing foundational utilities, data generation, and helper functions for quality engineering workflows.

---

## Project 1 milestone - Week 2, Monday
This milestone establishes the modularized package structure (qe_foundations/utils/), core helper functions, dependency configuration, and initial project documentation.

### What Exists Now
* Modular Package Architecture: Refactored legacy code into a structured qe_foundations/utils/ package utilizing explicit absolute imports and clean module re-exports via __all__.
* Utility Modules: Implemented specialized modules for string manipulation (slugify, mask_email, is_valid_email), numeric constraints (clamp, percent), date operations (days_between, is_weekend), and test user generation.
* Environment & Tooling: Configured local virtual environment tracking via requirements.txt and requirements-dev.txt, verified via smoke tests.

### What is Coming (Tue - Fri)
* Tuesday: Comprehensive unit testing implementation using pytest.
* Wednesday: Code quality enforcement, linting, formatting, and CI pipeline setup.
* Thursday & Friday: Advanced mocking, fixture generation, and end-to-end integration checks.

---

## Setup Instructions

Follow these steps to set up your local development environment:

1. Create a virtual environment:
   python -m venv .venv

2. Activate the virtual environment:
   PowerShell:
   .venv\Scripts\Activate.ps1

   Bash:
   source .venv/bin/activate

3. Install project dependencies:
   python -m pip install -r requirements.txt

4. Verify your setup:
   python smoke_utils.py

---

## Usage Example

from qe_foundations.utils import slugify, mask_email, days_between

# Format strings into clean URL slugs
title_slug = slugify("Hello World! QE Foundations")
print(title_slug)  # Output: hello-world-qe-foundations

# Mask sensitive user data for logs or tests
masked = mask_email("alex.qa@example.com")
print(masked)  # Output: a***a@example.com

# Calculate duration between two dates
duration = days_between("2026-01-01", "2026-01-15")
print(duration)  # Output: 14