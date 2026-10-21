# Ingestion module - design notes (Week 2, Day 2)

Answer in your own words, 2-4 sentences each. Replace every line that starts with
`TODO:`. (Delete nothing else.)

## 1. Exceptions or assertions?
In `validate_record` I raise exceptions for a negative duration, but in
`IngestionReport.check_invariants` I use `assert`. Why is each the right tool there?

We use exceptions for checking file data because bad inputs happen in the real world and must always be caught. We use assertions to check our own code's internal logic, because if an assertion fails, it means our program has a bug, not that the user gave us bad data.

## 2. Stop or collect?
Why is a malformed JSON file a `SourceError` that stops loading, while a record with
a bad status is a `RecordValidationError` that is collected? Who benefits from this split?

A malformed file stops loading because it is completely unreadable, meaning zero records can be processed. A record with bad status only affects that single row, so it is much better to save the error info and keep loading the rest of the good rows.

## 3. What did the context managers buy you?
Name two things that `open_source` / `LoadSession` do for the caller that you would otherwise have to remember to do at every call site.

open_source automatically handles file cleanup (making sure files close safely even if an error happens) and text encoding (like stripping Excel BOM characters). LoadSession automatically tracks how long a file took to load without needing extra timer code everywhere.

## 4. Your hardest bad-input case
Which sample file or record took you longest to handle, and what was the cause?

Handling XML files was the trickiest because the test cases could be nested deep inside the file rather than just being direct children, which required using .iter() instead of standard searches to find them all.
