# 🏠 Schedule

**Schedule** is a keyboard-first family operating dashboard built with Python, Textual, and SQLite.

It combines household scheduling, rotating responsibilities, memorization, randomized homework, searchable study assignments, and progress tracking inside one terminal interface.

---

## ✨ Features

- 👩‍🍳 Randomized cooking rotation
- 🚫 Nobody cooks two days in a row
- 🍽 Cook automatically handles dishes
- 🧽 Rotating kitchen responsibilities
- 🛁 Bathroom cleaning assignments
- 🧹 Kitchen cleaning assignments
- 📦 Basement cleaning assignments
- 🧺 Laundry assignments
- 📚 Daily memorization rotation
- 🎓 Randomized homework
- 🔎 Searchable assignment library
- 🤖 NotebookLM study activities
- 📅 Weekly schedule
- 📜 SQLite history
- ✅ Completion tracking
- 🎨 Multiple terminal palettes

---

# 👩‍🍳 Cooking Rotation

The cook is shuffled between:

```text
Zara
Jasmin
Aria
```

The primary rule is:

> Nobody cooks two days in a row.

Whoever cooks also handles the dishes.

Example:

```text
👩‍🍳 COOK

Jasmin

Jasmin cooks today.
Jasmin also does the dishes.
```

If Jasmin cooks today, tomorrow's cook must be either Zara or Aria.

---

# 🍽 Kitchen Responsibilities

Kitchen responsibilities are divided between all three people.

```text
Cook
└── Dishes

Second Person
└── Counters + Stove

Third Person
└── Table + Chairs + Floor
```

Example:

```text
Jasmin
└── Cook + Dishes

Zara
└── Counters + Stove

Aria
└── Table + Chairs + Floor
```

The non-cooking assignments can be shuffled while preserving the cooking rule.

---

# 🏠 Household Chores

Additional household jobs are assigned separately.

```text
🛁 Bathrooms
🧹 Kitchen Cleaning
📦 Basement
🧺 Laundry
```

Example:

```text
Bathrooms
→ Aria

Kitchen Cleaning
→ Zara

Basement
→ Jasmin

Laundry
→ Aria
```

This makes the daily schedule flexible without tying every responsibility to the cook.

---

# 📚 Memorization

Every day all three books are assigned.

Current books:

```text
Mason Encyclopedia 1
Mason Encyclopedia 2
Bible
```

The books rotate between all three students.

### Day 1

```text
Zara
→ Mason Encyclopedia 1

Jasmin
→ Mason Encyclopedia 2

Aria
→ Bible
```

### Day 2

```text
Zara
→ Mason Encyclopedia 2

Jasmin
→ Bible

Aria
→ Mason Encyclopedia 1
```

### Day 3

```text
Zara
→ Bible

Jasmin
→ Mason Encyclopedia 1

Aria
→ Mason Encyclopedia 2
```

The rotation then continues.

Each memorization assignment can be marked complete.

---

# 🎓 Homework Engine

Homework is shuffled independently from chores.

Press:

```text
H
```

to generate new homework.

Example:

```text
Zara
Vocabulary
→ Vocabulary List

Jasmin
NotebookLM
→ NotebookLM Class Generation

Aria
Critical Thinking
→ Cause and Effect
```

Another shuffle might produce:

```text
Zara
Reading
→ Chapter Summary

Jasmin
Research
→ Timeline

Aria
Quiz & Review
→ Rapid Recall
```

---

# 🔎 Searchable Study Categories

The homework library is searchable.

Current categories include:

```text
Vocabulary
Reading
Writing
Memorization
Research
NotebookLM
Quiz & Review
Presentation
Critical Thinking
Projects
```

The search system checks:

- Category
- Assignment title
- Description
- Keywords

Example searches:

```text
vocab
quiz
research
NotebookLM
presentation
memory
```

---

# 📝 Vocabulary Assignments

Available activities include:

```text
Vocabulary List
Vocabulary Three Times
Context Clues
Word Families
```

## Vocabulary List

Choose 10 words and provide:

```text
Word
Definition
Synonym
Antonym
Original Sentence
```

## Vocabulary Three Times

Write each vocabulary word three times and then define it.

## Context Clues

Find unfamiliar words in reading material and infer their meaning before checking the definition.

---

# 📖 Reading Assignments

Examples include:

```text
Focused Reading
Chapter Summary
Main Idea and Evidence
Question the Text
```

### Focused Reading

Read an assigned section and identify five important facts.

### Chapter Summary

Summarize a chapter or section using your own words.

### Main Idea and Evidence

Identify:

```text
1 Main Idea
3 Supporting Pieces of Evidence
```

---

# ✍️ Writing Assignments

Examples include:

```text
One Paragraph Response
Five Sentence Summary
Compare and Contrast
Short Essay
```

Students practice organizing information instead of only recalling facts.

---

# 🧠 Memorization Activities

Additional exercises include:

```text
Read Cover Recite
Seven Repetitions
Teach From Memory
```

A basic memorization cycle is:

```text
READ
 ↓
COVER
 ↓
RECITE
 ↓
CHECK
 ↓
REPEAT
```

---

# 🔬 Research Assignments

Research options include:

```text
Three Source Research
Source Comparison
Research Brief
Timeline
```

## Three Source Research

Students:

1. Select a topic.
2. Find three sources.
3. Identify important information.
4. Record verified facts.
5. Write a summary.

---

# 🤖 NotebookLM Assignments

NotebookLM has a dedicated homework category.

Assignments include:

```text
NotebookLM Class Generation
NotebookLM Study Guide
NotebookLM Flashcards
NotebookLM Quiz
NotebookLM Mind Map
NotebookLM Audio Lesson
NotebookLM Video Lesson
NotebookLM Slide Deck
NotebookLM Infographic
NotebookLM Data Table
```

## NotebookLM Class Generation

This workflow turns source material into a miniature class:

```text
SOURCE MATERIAL
      ↓
  NOTEBOOKLM
      ↓
  STUDY GUIDE
      ↓
  FLASHCARDS
      ↓
     QUIZ
      ↓
   MIND MAP
      ↓
 PRESENTATION
```

The student then explains what was learned.

---

# ❓ Quiz & Review

Assignments include:

```text
Ten Question Quiz
Mistake Review
Rapid Recall
```

The goal is active recall rather than simply rereading material.

---

# 🎤 Presentation

Presentation activities include:

```text
Five Minute Lesson
Three Slide Presentation
Oral Summary
```

These assignments require students to explain information aloud.

---

# 🧠 Critical Thinking

Assignments include:

```text
Five Whys
Cause and Effect
Evidence Check
Teach It Differently
```

## Five Whys

```text
Why?
 ↓
Why?
 ↓
Why?
 ↓
Why?
 ↓
Why?
```

Each level requires an answer.

## Teach It Differently

Explain the same idea:

```text
To a child
To a classmate
To an expert
```

---

# 🛠 Projects

Project assignments include:

```text
Mini Research Project
Create a Study Sheet
Build a Question Bank
```

A study sheet can contain:

```text
Important Terms
Definitions
Facts
Dates
Concepts
Questions
Answers
```

---

# 🖥 Interface

The application uses a multi-tab Textual interface.

```text
┌─────────┬──────────┬──────┬─────────┬──────────┐
│  Today  │ Homework │ Week │ History │ Settings │
└─────────┴──────────┴──────┴─────────┴──────────┘
```

## Today

Displays:

- Today's cook
- Dishes
- Counters and stove
- Table, chairs, and floor
- Bathrooms
- Kitchen cleaning
- Basement
- Laundry
- Memorization assignments

## Homework

Displays:

- Today's randomized homework
- Completion state
- Search box
- Category filter
- Assignment library

## Week

Shows upcoming household responsibilities for the entire week.

## History

Displays previously saved schedules.

## Settings

Contains application settings such as the selected color palette.

---

# 🎨 Color Palettes

Available themes include:

```text
Purple Storm
Ocean Blue
Matrix Green
Amber Night
Rose Noir
Midnight Mono
```

Palette settings are stored in SQLite.

---

# ⌨️ Keyboard Controls

```text
G    Shuffle chores
H    Shuffle homework
S    Save
W    Week view
Q    Quit
```

Standard Textual navigation also works:

```text
Tab
Shift+Tab
Arrow Keys
Enter
Space
```

---

# 🗄 SQLite Database

Schedule uses SQLite, so no external database server is required.

The application automatically creates:

```text
daily_schedule.db
```

Major tables include:

```text
chore_days
memorization
assignment_catalog
homework_daily
settings
```

## chore_days

Stores household schedules such as:

```text
date
cook
dishes
counters_stove
table_chairs_floor
bathrooms
kitchen_clean
basement
laundry
```

## memorization

Stores:

```text
date
person
book
completed
```

## assignment_catalog

Stores:

```text
category
title
description
keywords
active
```

## homework_daily

Stores:

```text
date
person
task_id
completed
assigned_at
```

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/obsidiandevcoder/Schedule.git
cd Schedule
```

## Install Virtual Environment Support

On Debian, Ubuntu, or Linux Mint:

```bash
sudo apt update
sudo apt install -y python3-venv
```

## Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Upgrade pip

```bash
python -m pip install --upgrade pip
```

## Install Textual

```bash
python -m pip install textual
```

## Run Schedule

```bash
python daily_schedule_tui.py
```

---

# ▶️ Daily Launch

After installation:

```bash
cd ~/daily-schedule
source .venv/bin/activate
python daily_schedule_tui.py
```

Or run the application using an existing environment containing Textual:

```bash
~/job-tracker/.venv/bin/python ~/daily-schedule/daily_schedule_tui.py
```

---

# 🔐 Privacy

The local SQLite database may contain household scheduling and study history.

For a public repository, the database should normally remain local.

Recommended `.gitignore`:

```text
.venv/
venv/
__pycache__/
*.py[cod]
daily_schedule.db
daily_schedule.db-shm
daily_schedule.db-wal
.DS_Store
```

If the database is already tracked:

```bash
git rm --cached daily_schedule.db
```

This removes it from Git without deleting the local database.

---

# 📁 Project Structure

```text
Schedule/
│
├── daily_schedule_tui.py
├── README.md
├── requirements.txt
├── .gitignore
└── daily_schedule.db     # Local only
```

---

# 🛣 Roadmap

Future improvements could include:

```text
Custom family members
Custom books
Custom assignments
Assignment editor
Completion statistics
Chore fairness scoring
Monthly calendar
Homework history
Study streaks
CSV export
JSON export
Markdown export
```

---

# 🏠 Schedule

**One terminal dashboard for chores, cooking, cleaning, homework, memorization, and family study.**

