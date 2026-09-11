<div align="center">

# Habit Tracker

**A terminal-based habit tracking system for building and maintaining daily routines.**

Track streaks, visualize progress, and stay accountable — all from your terminal.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## Features

- **Habit CRUD** — create, update, and delete habits with custom names and descriptions
- **Daily check-ins** — mark habits as complete for any day
- **Streak tracking** — automatic consecutive-day streak calculation
- **Progress visualization** — terminal-based charts showing completion history
- **Flexible scheduling** — daily, weekly, or custom frequency targets
- **Persistent storage** — JSON-based local data file
- **Zero dependencies** — pure Python standard library (no pip install needed)

---

## Quick Start

```bash
git clone https://github.com/yourname/habit-tracker.git
cd habit-tracker
python main.py
```

---

## Usage

```
$ python main.py

=== Habit Tracker ===

1. Add Habit
2. Check In
3. View Habits
4. View Stats
5. Delete Habit
6. Exit

> 1
Habit name: exercise
Description: Daily 30-minute workout
Frequency (daily/weekly): daily
✅ Habit "exercise" created!

> 2
Your habits:
  1. exercise
Select habit: 1
Date (YYYY-MM-DD, or Enter for today): 
✅ Checked in! Streak: 7 days 🔥

> 3

  Habit          Streak   This Week   Completion
  ─────────────  ───────  ──────────  ──────────
  exercise       7 🔥     ████░░░     57%
  reading        3        █░░░░░░     14%
  meditation     12 🔥    ██████░     86%
```

---

## Project Structure

```
habit-tracker/
├── main.py           # Entry point — CLI menu
├── data/
│   └── habits.json   # Persistent habit data
├── requirements.txt  # (empty — zero dependencies)
└── .gitignore
```

---

## Data Model

Each habit is stored as:

```json
{
  "id": "exercise",
  "description": "Daily 30-minute workout",
  "frequency": "daily",
  "completed_dates": ["2026-09-01", "2026-09-02", "..."],
  "created_at": "2026-09-01"
}
```

---

## Roadmap

- [ ] Weekly/monthly summary reports
- [ ] Export to CSV
- [ ] Habit categories and tags
- [ ] Reminder notifications
- [ ] Multiple data storage backends (SQLite, PostgreSQL)

---

## License

MIT — use freely for personal and commercial projects.
