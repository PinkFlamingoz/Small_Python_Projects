# Small Python Projects

## Overview

This repository is a grab bag of self-contained exercises that explore core Python concepts—loops, conditionals, file I/O, data structures, APIs, basic databases, and a little bit of text processing. Most scripts can be run directly from the command line and rely only on the standard library, with a few drawing on small helper utilities in `basic_functions.py` or sample data under `DATA/`, `texts/`, and `dictionaries/`.

## Script Quick Reference

- `bank_says_hello.py` – Pays out different dollar amounts based on the first word of a typed greeting.
- `basic_functions.py` – Shared helper that repeatedly prompts for input with optional type casting, bounds, and blank handling.
- `calculator.py` – Tiny demo that adds and divides two integers, highlighting floating-point precision.
- `cases.py` – Downloads the NYTimes US COVID case data, computes 14-day windows, and compares seven-day averages between weeks.
- `classes.py` – Defines a `Student` class with setters/getters and an interactive console workflow.
- `dictionary.py` – Minimal in-memory dictionary backend used by the spell checker (`speller.py`).
- `dna.py` – Matches DNA STR counts from a sequence file against a CSV database of profiles.
- `fancy_font.py` – Renders user-provided text in ASCII art using PyFiglet (choose a font with CLI flags or pick one at random).
- `how_many_coins_to_give_back.py` – Greedy coin change calculator for US coins that reports the total coins returned.
- `jar.py` – Cookie jar class with capacity management and a menu-driven CLI for deposits, withdrawals, and configuration.
- `library.py` – CSV-backed personal library tracker supporting CRUD, read/unread filters, and persistence.
- `load_data_to_database.py` – Creates and populates a SQLite database of students and houses, then offers an admin console for edits and reports.
- `loops.py` – Practice script that iterates over words in different ways to demonstrate loop constructs and slicing.
- `movie_searches.py` – Interactive browser for the provided `movies.db`, offering reports on titles, ratings, and people involved.
- `phonebook.py` – Appends a single name/number pair to `DATA/phonebook.csv` using CSV writer utilities.
- `print_hashtag_grids.py` – Generates assorted ASCII shapes (lines, grids, pyramids, Pascal triangle, diamond) with configurable size.
- `speller.py` – Command-line spell checker that benchmarks dictionary load and lookup times for the supplied texts.
- `tacos.py` – Running tally of menu items ordered from a taco stand menu, with totals displayed as you go.
- `tic_tac_toe.py` – Playable human-vs-computer Tic-Tac-Toe featuring simple AI move selection.
- `tournament.py` – Simulates repeated tournaments based on Elo-style ratings to estimate win probabilities from a CSV roster.
- `valid_credit_card.py` – Implements the Luhn checksum to classify credit card numbers as AMEX, Mastercard, Visa, or invalid.
- `what_grade_is_this_text.py` – Implements the Coleman-Liau index to estimate the US reading grade of supplied text.

## Data & Dependencies

- Sample data lives under `DATA/`, `texts/`, and `dictionaries/`. Many scripts expect these files relative to the project root.
- Third-party packages used:
	- `requests` for pulling live COVID data (`cases.py`).
	- `pyfiglet` for ASCII art rendering (`fancy_font.py`).
- SQLite comes bundled with Python but requires the included `.db` files for the database-driven scripts.

## Running Scripts

Run any project individually:

```powershell
py <script_name>.py
```

Some scripts accept command-line arguments (e.g., `dna.py`, `library.py`, `movie_searches.py`, `speller.py`, `tournament.py`). Consult the script headers or CLI prompts for usage details.