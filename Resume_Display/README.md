# Profile Display — Suresh Korumilli

A simple, console-based Python application that displays Suresh Korumilli's
professional profile — summary, experience, core skills, certifications,
and education — through an interactive menu.

## Overview

This version is built using only core Python fundamentals — variables,
input, if/else, loops, lists, dictionaries, and functions (no classes,
no external libraries). Profile data (contact info, summary, work
history, skills, certifications, and education) is stored directly in
variables, lists, and dictionaries at the top of the script. Each
section has its own display function, and a menu-driven `main()`
function (using a `while` loop and `if/elif/else`) lets the user choose
which section to view, or print the full profile at once.

## Features

- **Full Profile View** — prints the entire resume in a clean, formatted layout
- **Section-wise View** — view Summary, Experience, Core Skills,
  Certifications, or Education individually
- **Menu-driven console interface** — simple numbered options, loops
  until the user exits
- Built using only core Python (no external libraries required)

## File Structure

```
profile_display.py   # Main script containing the Profile class and menu logic
README.md             # This file
```

## How to Run

Requires Python 3.6+.

```bash
python profile_display.py
```

You'll see a menu like:

```
PROFILE MENU
  1. View Full Profile
  2. View Summary
  3. View Experience
  4. View Core Skills
  5. View Certifications
  6. View Education
  0. Exit
```

Enter the number corresponding to the section you'd like to view.

## Design Notes

- **Variables** hold single values like `name` and `title`.
- **Dictionaries** store key-value data: `contact`, `core_skills`, and
  `education`.
- **Lists** (and lists of dictionaries) store repeating data:
  `certifications`, and `experience` (each job is a dictionary with a
  nested list of `highlights`).
- **Functions** separate each section's display logic (`display_summary`,
  `display_experience`, etc.), keeping the code organized and reusable.
- **Loops** (`for`) walk through lists and dictionaries to print each
  entry; a `while` loop keeps the menu running until the user exits.
- **if/elif/else** handles the menu choice and invalid input.
- **input()** captures the user's menu selection.
- This keeps the project aligned with the self-learning goal of
  practicing core Python fundamentals before introducing classes.

## Possible Extensions

- Export the profile to a PDF or formatted text file
- Add a search function (e.g., search skills or companies by keyword)
- Read profile data from an external JSON/CSV file instead of hardcoding it
- Add unit tests for each display method
