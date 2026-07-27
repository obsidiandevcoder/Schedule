````bash
cd ~/daily-schedule

cat >> README.md <<'EOF'

Facts

Dates

Concepts

Questions

Answers

---

# 🗄 Database

Schedule uses SQLite.

The local database file is:

```text
daily_schedule.db
````

Main tables include:

```text
chore_days
memorization
assignment_catalog
homework_daily
settings
```

The database is created automatically on first run.

---

# 🎨 Palettes

Available themes:

```text
Purple Storm
Ocean Blue
Matrix Green
Amber Night
Rose Noir
Midnight Mono
```

---

# ⌨️ Keyboard Controls

```text
G    Shuffle chores
H    Shuffle homework
S    Save
W    Week view
Q    Quit
```

---

# 🚀 Installation

Clone:

```bash
git clone https://github.com/obsidiandevcoder/Schedule.git
cd Schedule
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Textual:

```bash
python -m pip install --upgrade pip
python -m pip install textual
```

Run:

```bash
python daily_schedule_tui.py
```

---

# 🔐 Privacy

Do not commit personal schedule history.

Recommended `.gitignore`:

```text
.venv/
__pycache__/
*.pyc
daily_schedule.db
daily_schedule.db-shm
daily_schedule.db-wal
```

---

# 🛣 Roadmap

Planned improvements:

```text
Custom family members
Custom books
Custom assignments
Assignment editor
Completion statistics
Chore fairness scoring
Monthly calendar
Homework history
CSV export
JSON export
Markdown export
Study streaks
```

---

# 🏠 Schedule

**One terminal dashboard for chores, cooking, cleaning, homework, memorization, and family study.**

EOF

tail -n 20 README.md

git add README.md
git commit -m "Complete detailed README"
git push

```
```

Facts

Dates

Concepts

Questions

Answers

---

# 🗄 Database

Schedule uses SQLite.

The local database file is:

```text
daily_schedule.db

Main tables include:

chore_days
memorization
assignment_catalog
homework_daily
settings

The database is created automatically on first run.

🎨 Palettes

Available themes:

Purple Storm
Ocean Blue
Matrix Green
Amber Night
Rose Noir
Midnight Mono
⌨️ Keyboard Controls
G    Shuffle chores
H    Shuffle homework
S    Save
W    Week view
Q    Quit
🚀 Installation

Clone:

git clone https://github.com/obsidiandevcoder/Schedule.git
cd Schedule

Create a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install Textual:

python -m pip install --upgrade pip
python -m pip install textual

Run:

python daily_schedule_tui.py
🔐 Privacy

Do not commit personal schedule history.

Recommended .gitignore:

.venv/
__pycache__/
*.pyc
daily_schedule.db
daily_schedule.db-shm
daily_schedule.db-wal
🛣 Roadmap

Planned improvements:

Custom family members
Custom books
Custom assignments
Assignment editor
Completion statistics
Chore fairness scoring
Monthly calendar
Homework history
CSV export
JSON export
Markdown export
Study streaks
🏠 Schedule

One terminal dashboard for chores, cooking, cleaning, homework, memorization, and family study.

