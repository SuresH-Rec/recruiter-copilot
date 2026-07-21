# Profile Display — Suresh Korumilli

A simple, console-based Python application that displays Suresh Korumilli's
professional profile — summary, experience, core skills, certifications,
and education — through an interactive menu.

## Overview

The profile data (contact info, summary, work history, skills,
certifications, and education) is modeled inside a `Profile` class. Each
section has its own display method, and a menu-driven `main()` function
lets the user choose which section to view, or print the full profile at
once.

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

- The `Profile` class separates **data** (set in `__init__`) from
  **display logic** (the `display_*` methods), making it easy to update
  details later without touching the presentation code.
- Data is stored using simple Python structures — lists of dicts for
  experience, dicts for skills/contact/education — keeping the code
  readable and easy to extend.
- This project fits into the broader self-learning goal of building
  Python fundamentals (variables, loops, functions, conditionals,
  classes) through practical, recruitment-relevant tools.

## Possible Extensions

- Export the profile to a PDF or formatted text file
- Add a search function (e.g., search skills or companies by keyword)
- Read profile data from an external JSON/CSV file instead of hardcoding it
- Add unit tests for each display method
