#!/usr/bin/env python3

import random
import sqlite3
from datetime import date, datetime, timedelta
from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import (
    Button,
    Checkbox,
    DataTable,
    Footer,
    Header,
    Input,
    Select,
    Static,
    TabbedContent,
    TabPane,
)


# ============================================================
# PATHS
# ============================================================

APP_DIR = Path(__file__).resolve().parent
DB_FILE = APP_DIR / "daily_schedule.db"


# ============================================================
# FAMILY
# ============================================================

PEOPLE = [
    "Zara",
    "Jasmin",
    "Aria",
]


# ============================================================
# MEMORIZATION BOOKS
# ============================================================

BOOKS = [
    "Mason Encyclopedia 1",
    "Mason Encyclopedia 2",
    "Bible",
]


# ============================================================
# ROTATION ANCHOR
# ============================================================

ROTATION_ANCHOR = date(2026, 7, 27)


# ============================================================
# PALETTES
# ============================================================

PALETTES = {
    "purple": "Purple Storm",
    "ocean": "Ocean Blue",
    "matrix": "Matrix Green",
    "amber": "Amber Night",
    "rose": "Rose Noir",
    "mono": "Midnight Mono",
}


# ============================================================
# HOMEWORK CATEGORIES
# ============================================================

HOMEWORK_CATEGORIES = [
    "Vocabulary",
    "Reading",
    "Writing",
    "Memorization",
    "Research",
    "NotebookLM",
    "Quiz & Review",
    "Presentation",
    "Critical Thinking",
    "Projects",
]


# ============================================================
# DEFAULT ASSIGNMENT DATABASE
# ============================================================

ASSIGNMENT_SEED = [

    # --------------------------------------------------------
    # VOCABULARY
    # --------------------------------------------------------

    (
        "Vocabulary",
        "Vocabulary List",
        "Choose 10 key words. Write the definition, synonym, antonym, and one original sentence for each.",
        "words definitions synonym antonym sentence spelling"
    ),

    (
        "Vocabulary",
        "Vocabulary Three Times",
        "Choose 10 vocabulary words and write each word three times before defining it.",
        "words writing repetition definitions spelling"
    ),

    (
        "Vocabulary",
        "Context Clues",
        "Find 8 unfamiliar words in today's reading and infer each meaning from context before checking the definition.",
        "context words reading definitions"
    ),

    (
        "Vocabulary",
        "Word Families",
        "Choose 8 words and identify related nouns, verbs, adjectives, or other forms.",
        "grammar vocabulary words forms"
    ),


    # --------------------------------------------------------
    # READING
    # --------------------------------------------------------

    (
        "Reading",
        "Focused Reading",
        "Read one assigned section and write five important facts from it.",
        "reading facts comprehension"
    ),

    (
        "Reading",
        "Chapter Summary",
        "Read one chapter or section and summarize it in your own words.",
        "reading summary comprehension chapter"
    ),

    (
        "Reading",
        "Main Idea and Evidence",
        "Identify the main idea and give three pieces of evidence that support it.",
        "main idea evidence comprehension"
    ),

    (
        "Reading",
        "Question the Text",
        "Write five questions about the reading and answer them using the text.",
        "reading questions answers comprehension"
    ),


    # --------------------------------------------------------
    # WRITING
    # --------------------------------------------------------

    (
        "Writing",
        "One Paragraph Response",
        "Write one organized paragraph explaining the most important thing learned today.",
        "paragraph writing response"
    ),

    (
        "Writing",
        "Five Sentence Summary",
        "Explain the lesson in exactly five complete sentences.",
        "writing summary sentences"
    ),

    (
        "Writing",
        "Compare and Contrast",
        "Compare two ideas, people, events, texts, or concepts and explain at least three similarities or differences.",
        "compare contrast writing"
    ),

    (
        "Writing",
        "Short Essay",
        "Write an introduction, two body paragraphs, and a conclusion about the assigned subject.",
        "essay writing paragraphs"
    ),


    # --------------------------------------------------------
    # MEMORIZATION
    # --------------------------------------------------------

    (
        "Memorization",
        "Read Cover Recite",
        "Read the passage, cover it, recite what you remember, then check your accuracy.",
        "memory recitation passage"
    ),

    (
        "Memorization",
        "Seven Repetitions",
        "Recite the assigned passage seven times and record which parts are still difficult.",
        "memorize repetition recitation"
    ),

    (
        "Memorization",
        "Teach From Memory",
        "Explain the assigned material aloud without looking at the book.",
        "memory teach aloud recall"
    ),


    # --------------------------------------------------------
    # RESEARCH
    # --------------------------------------------------------

    (
        "Research",
        "Three Source Research",
        "Research one topic using three sources and write five verified facts.",
        "research sources facts"
    ),

    (
        "Research",
        "Source Comparison",
        "Compare two sources covering the same subject and identify where they agree or disagree.",
        "research sources compare evidence"
    ),

    (
        "Research",
        "Research Brief",
        "Create a short research brief containing the topic, major facts, evidence, and conclusion.",
        "research brief evidence conclusion"
    ),

    (
        "Research",
        "Timeline",
        "Create a chronological timeline of important events from the topic being studied.",
        "history timeline chronology events"
    ),


    # --------------------------------------------------------
    # NOTEBOOKLM
    # --------------------------------------------------------

    (
        "NotebookLM",
        "NotebookLM Class Generation",
        "Build a mini-class from selected sources: create a study guide, flashcards, quiz, mind map, and short presentation.",
        "notebooklm class study guide flashcards quiz mind map slides"
    ),

    (
        "NotebookLM",
        "NotebookLM Study Guide",
        "Load the assigned sources into NotebookLM and generate a study guide. Review it and write five things learned.",
        "notebooklm study guide sources"
    ),

    (
        "NotebookLM",
        "NotebookLM Flashcards",
        "Generate flashcards from the assigned sources and complete one full review session.",
        "notebooklm flashcards memory"
    ),

    (
        "NotebookLM",
        "NotebookLM Quiz",
        "Generate a quiz from the assigned sources, complete it, and review every missed question.",
        "notebooklm quiz questions review"
    ),

    (
        "NotebookLM",
        "NotebookLM Mind Map",
        "Generate a mind map and explain the five most important connections shown on it.",
        "notebooklm mind map concepts"
    ),

    (
        "NotebookLM",
        "NotebookLM Audio Lesson",
        "Generate an Audio Overview, listen to it, and write five notes from the lesson.",
        "notebooklm audio overview listening notes"
    ),

    (
        "NotebookLM",
        "NotebookLM Video Lesson",
        "Generate a Video Overview and write a short summary of the major ideas presented.",
        "notebooklm video overview summary"
    ),

    (
        "NotebookLM",
        "NotebookLM Slide Deck",
        "Generate a slide deck from the study sources and explain each slide aloud.",
        "notebooklm slides presentation"
    ),

    (
        "NotebookLM",
        "NotebookLM Infographic",
        "Generate an infographic and identify the most important facts and relationships it shows.",
        "notebooklm infographic visual"
    ),

    (
        "NotebookLM",
        "NotebookLM Data Table",
        "Create a data table comparing important people, concepts, events, terms, or ideas from the sources.",
        "notebooklm table compare data"
    ),


    # --------------------------------------------------------
    # QUIZ AND REVIEW
    # --------------------------------------------------------

    (
        "Quiz & Review",
        "Ten Question Quiz",
        "Create and answer ten questions about the current subject.",
        "quiz review questions"
    ),

    (
        "Quiz & Review",
        "Mistake Review",
        "Review previous mistakes and explain why each incorrect answer was wrong.",
        "quiz mistakes correction"
    ),

    (
        "Quiz & Review",
        "Rapid Recall",
        "Answer 15 short recall questions without using notes, then correct the answers.",
        "quiz recall test"
    ),


    # --------------------------------------------------------
    # PRESENTATION
    # --------------------------------------------------------

    (
        "Presentation",
        "Five Minute Lesson",
        "Teach the subject aloud for five minutes as if you are the teacher.",
        "presentation speaking teaching"
    ),

    (
        "Presentation",
        "Three Slide Presentation",
        "Create three slides: What it is, Why it matters, and What was learned.",
        "presentation slides"
    ),

    (
        "Presentation",
        "Oral Summary",
        "Give a two-minute spoken summary without reading directly from notes.",
        "speech presentation summary"
    ),


    # --------------------------------------------------------
    # CRITICAL THINKING
    # --------------------------------------------------------

    (
        "Critical Thinking",
        "Five Whys",
        "Choose one important idea and ask why five times, answering each level.",
        "why reasoning critical thinking"
    ),

    (
        "Critical Thinking",
        "Cause and Effect",
        "Identify three causes and three effects related to today's subject.",
        "cause effect reasoning"
    ),

    (
        "Critical Thinking",
        "Evidence Check",
        "Choose three claims from the lesson and identify the evidence supporting each one.",
        "evidence claims reasoning"
    ),

    (
        "Critical Thinking",
        "Teach It Differently",
        "Explain the same concept three ways: to a child, to a classmate, and to an expert.",
        "explanation reasoning teaching"
    ),


    # --------------------------------------------------------
    # PROJECTS
    # --------------------------------------------------------

    (
        "Projects",
        "Mini Research Project",
        "Choose one topic, research it, summarize it, and present the result.",
        "project research presentation"
    ),

    (
        "Projects",
        "Create a Study Sheet",
        "Create a one-page reference sheet containing the major terms, facts, and concepts.",
        "project study sheet review"
    ),

    (
        "Projects",
        "Build a Question Bank",
        "Create 20 reusable questions and answers from the current study material.",
        "project questions quiz bank"
    ),
]


# ============================================================
# DATABASE
# ============================================================

class Database:

    def __init__(self, path):
        self.path = path
        self.setup()

    def connect(self):
        return sqlite3.connect(self.path)

    def setup(self):

        with self.connect() as conn:

            # ------------------------------------------------
            # CHORES
            # ------------------------------------------------

            conn.execute("""
                CREATE TABLE IF NOT EXISTS chore_days (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    date TEXT UNIQUE NOT NULL,
                    day TEXT NOT NULL,

                    cook TEXT NOT NULL,

                    dishes TEXT NOT NULL,
                    counters_stove TEXT NOT NULL,
                    table_chairs_floor TEXT NOT NULL,

                    bathrooms TEXT NOT NULL,
                    kitchen_clean TEXT NOT NULL,
                    basement TEXT NOT NULL,
                    laundry TEXT NOT NULL,

                    saved_at TEXT NOT NULL
                )
            """)

            # ------------------------------------------------
            # MEMORIZATION
            # ------------------------------------------------

            conn.execute("""
                CREATE TABLE IF NOT EXISTS memorization (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    date TEXT NOT NULL,
                    person TEXT NOT NULL,
                    book TEXT NOT NULL,

                    completed INTEGER NOT NULL DEFAULT 0,

                    UNIQUE(date, person)
                )
            """)

            # ------------------------------------------------
            # ASSIGNMENT CATALOG
            # ------------------------------------------------

            conn.execute("""
                CREATE TABLE IF NOT EXISTS assignment_catalog (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    category TEXT NOT NULL,
                    title TEXT NOT NULL UNIQUE,
                    description TEXT NOT NULL,
                    keywords TEXT DEFAULT '',
                    active INTEGER NOT NULL DEFAULT 1
                )
            """)

            # ------------------------------------------------
            # DAILY HOMEWORK
            # ------------------------------------------------

            conn.execute("""
                CREATE TABLE IF NOT EXISTS homework_daily (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    date TEXT NOT NULL,
                    person TEXT NOT NULL,
                    task_id INTEGER NOT NULL,

                    completed INTEGER NOT NULL DEFAULT 0,

                    assigned_at TEXT NOT NULL,

                    UNIQUE(date, person),

                    FOREIGN KEY(task_id)
                    REFERENCES assignment_catalog(id)
                )
            """)

            # ------------------------------------------------
            # SETTINGS
            # ------------------------------------------------

            conn.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
            """)

            # ------------------------------------------------
            # SEED ASSIGNMENTS
            # ------------------------------------------------

            conn.executemany("""
                INSERT OR IGNORE INTO assignment_catalog (
                    category,
                    title,
                    description,
                    keywords
                )
                VALUES (?, ?, ?, ?)
            """, ASSIGNMENT_SEED)

            conn.commit()

    # ========================================================
    # SETTINGS
    # ========================================================

    def get_setting(self, key, default=""):

        with self.connect() as conn:

            row = conn.execute(
                "SELECT value FROM settings WHERE key = ?",
                (key,),
            ).fetchone()

        return row[0] if row else default

    def set_setting(self, key, value):

        with self.connect() as conn:

            conn.execute("""
                INSERT INTO settings (key, value)
                VALUES (?, ?)

                ON CONFLICT(key)
                DO UPDATE SET value = excluded.value
            """, (
                key,
                value,
            ))

            conn.commit()

    # ========================================================
    # ASSIGNMENTS
    # ========================================================

    def search_assignments(
        self,
        search="",
        category="ALL",
    ):

        sql = """
            SELECT
                id,
                category,
                title,
                description

            FROM assignment_catalog

            WHERE active = 1
        """

        values = []

        if category != "ALL":

            sql += """
                AND category = ?
            """

            values.append(category)

        search = search.strip()

        if search:

            term = f"%{search.lower()}%"

            sql += """
                AND (
                    LOWER(category) LIKE ?
                    OR LOWER(title) LIKE ?
                    OR LOWER(description) LIKE ?
                    OR LOWER(keywords) LIKE ?
                )
            """

            values.extend([
                term,
                term,
                term,
                term,
            ])

        sql += """
            ORDER BY category, title
        """

        with self.connect() as conn:

            return conn.execute(
                sql,
                values,
            ).fetchall()

    def get_assignment(self, task_id):

        with self.connect() as conn:

            return conn.execute("""
                SELECT
                    id,
                    category,
                    title,
                    description

                FROM assignment_catalog

                WHERE id = ?
            """, (
                task_id,
            )).fetchone()

    # ========================================================
    # HOMEWORK
    # ========================================================

    def save_homework(
        self,
        date_text,
        assignments,
    ):

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        with self.connect() as conn:

            for person, task in assignments.items():

                conn.execute("""
                    INSERT INTO homework_daily (
                        date,
                        person,
                        task_id,
                        completed,
                        assigned_at
                    )

                    VALUES (?, ?, ?, ?, ?)

                    ON CONFLICT(date, person)

                    DO UPDATE SET
                        task_id = excluded.task_id,
                        completed = excluded.completed,
                        assigned_at = excluded.assigned_at
                """, (
                    date_text,
                    person,
                    task["id"],
                    1 if task.get("completed") else 0,
                    now,
                ))

            conn.commit()

    def load_homework(self, date_text):

        with self.connect() as conn:

            rows = conn.execute("""
                SELECT
                    h.person,
                    h.completed,
                    a.id,
                    a.category,
                    a.title,
                    a.description

                FROM homework_daily h

                JOIN assignment_catalog a
                    ON a.id = h.task_id

                WHERE h.date = ?

                ORDER BY h.person
            """, (
                date_text,
            )).fetchall()

        result = {}

        for row in rows:

            result[row[0]] = {
                "completed": bool(row[1]),
                "id": row[2],
                "category": row[3],
                "title": row[4],
                "description": row[5],
            }

        return result

    # ========================================================
    # CHORE SAVE
    # ========================================================

    def save_chore_day(
        self,
        schedule,
        completions,
    ):

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        with self.connect() as conn:

            conn.execute("""
                INSERT INTO chore_days (
                    date,
                    day,
                    cook,
                    dishes,
                    counters_stove,
                    table_chairs_floor,
                    bathrooms,
                    kitchen_clean,
                    basement,
                    laundry,
                    saved_at
                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

                ON CONFLICT(date)

                DO UPDATE SET
                    day = excluded.day,
                    cook = excluded.cook,
                    dishes = excluded.dishes,
                    counters_stove = excluded.counters_stove,
                    table_chairs_floor = excluded.table_chairs_floor,
                    bathrooms = excluded.bathrooms,
                    kitchen_clean = excluded.kitchen_clean,
                    basement = excluded.basement,
                    laundry = excluded.laundry,
                    saved_at = excluded.saved_at
            """, (
                schedule["date"],
                schedule["day"],
                schedule["cook"],
                schedule["dishes"],
                schedule["counters_stove"],
                schedule["table_chairs_floor"],
                schedule["bathrooms"],
                schedule["kitchen_clean"],
                schedule["basement"],
                schedule["laundry"],
                now,
            ))

            for person, book in schedule["books"].items():

                conn.execute("""
                    INSERT INTO memorization (
                        date,
                        person,
                        book,
                        completed
                    )

                    VALUES (?, ?, ?, ?)

                    ON CONFLICT(date, person)

                    DO UPDATE SET
                        book = excluded.book,
                        completed = excluded.completed
                """, (
                    schedule["date"],
                    person,
                    book,
                    1 if completions.get(person, False) else 0,
                ))

            conn.commit()

    def get_chore_day(self, date_text):

        with self.connect() as conn:

            return conn.execute("""
                SELECT
                    id,
                    date,
                    day,
                    cook,
                    dishes,
                    counters_stove,
                    table_chairs_floor,
                    bathrooms,
                    kitchen_clean,
                    basement,
                    laundry,
                    saved_at

                FROM chore_days

                WHERE date = ?
            """, (
                date_text,
            )).fetchone()

    def get_completions(self, date_text):

        with self.connect() as conn:

            rows = conn.execute("""
                SELECT
                    person,
                    completed

                FROM memorization

                WHERE date = ?
            """, (
                date_text,
            )).fetchall()

        return {
            person: bool(done)
            for person, done in rows
        }

    def chore_history(self):

        with self.connect() as conn:

            return conn.execute("""
                SELECT
                    id,
                    date,
                    cook,
                    bathrooms,
                    kitchen_clean,
                    basement,
                    laundry

                FROM chore_days

                ORDER BY date DESC

                LIMIT 200
            """).fetchall()


# ============================================================
# TUI
# ============================================================

class FamilyDashboard(App):

    TITLE = "Richmack Family Dashboard"

    SUB_TITLE = (
        "Chores • Study • Homework • Memorization"
    )

    BINDINGS = [
        Binding("g", "shuffle_chores", "Shuffle Chores"),
        Binding("h", "shuffle_homework", "Shuffle Homework"),
        Binding("s", "save_all", "Save"),
        Binding("w", "show_week", "Week"),
        Binding("q", "quit", "Quit"),
    ]

    CSS = """

    Screen {
        background: #0f1020;
    }

    #hero {
        height: 4;
        content-align: center middle;
        text-style: bold;
        border-bottom: solid #a78bfa;
    }

    TabbedContent {
        height: 1fr;
    }

    TabPane {
        padding: 1 2;
    }

    .card {
        border: round #a78bfa;
        padding: 1 2;
        margin: 1;
        height: auto;
    }

    .card-title {
        text-style: bold;
        margin-bottom: 1;
    }

    #chore-top {
        height: 16;
    }

    #chore-top .card {
        width: 1fr;
        height: 100%;
    }

    #house-row {
        height: 13;
    }

    #house-row .card {
        width: 1fr;
        height: 100%;
    }

    #memorization {
        border: round #a78bfa;
        padding: 1 2;
        margin: 1;
        height: auto;
    }

    #homework-today {
        border: round #a78bfa;
        padding: 1 2;
        margin: 1;
        height: auto;
    }

    #homework-controls {
        height: 5;
    }

    #homework-controls Input {
        width: 2fr;
        margin: 1;
    }

    #homework-controls Select {
        width: 1fr;
        margin: 1;
    }

    #buttons {
        height: 5;
        align: center middle;
    }

    Button {
        margin: 1;
        min-width: 17;
    }

    #status,
    #homework-status {
        height: 3;
        content-align: center middle;
        text-style: bold;
    }

    DataTable {
        height: 1fr;
    }

    .settings-box {
        border: round #a78bfa;
        margin: 1 2;
        padding: 1 2;
        height: auto;
    }

    /* PURPLE */

    .palette-purple {
        background: #0f1020;
    }

    .palette-purple #hero {
        color: #ddd6fe;
        border-bottom: solid #a78bfa;
    }

    .palette-purple .card,
    .palette-purple #memorization,
    .palette-purple #homework-today,
    .palette-purple .settings-box {
        border: round #a78bfa;
    }

    /* OCEAN */

    .palette-ocean {
        background: #061c2a;
    }

    .palette-ocean #hero {
        color: #bae6fd;
        border-bottom: solid #38bdf8;
    }

    .palette-ocean .card,
    .palette-ocean #memorization,
    .palette-ocean #homework-today,
    .palette-ocean .settings-box {
        border: round #38bdf8;
    }

    /* MATRIX */

    .palette-matrix {
        background: #061109;
    }

    .palette-matrix #hero {
        color: #86efac;
        border-bottom: solid #22c55e;
    }

    .palette-matrix .card,
    .palette-matrix #memorization,
    .palette-matrix #homework-today,
    .palette-matrix .settings-box {
        border: round #22c55e;
    }

    /* AMBER */

    .palette-amber {
        background: #181006;
    }

    .palette-amber #hero {
        color: #fde68a;
        border-bottom: solid #f59e0b;
    }

    .palette-amber .card,
    .palette-amber #memorization,
    .palette-amber #homework-today,
    .palette-amber .settings-box {
        border: round #f59e0b;
    }

    /* ROSE */

    .palette-rose {
        background: #1a0911;
    }

    .palette-rose #hero {
        color: #fbcfe8;
        border-bottom: solid #f472b6;
    }

    .palette-rose .card,
    .palette-rose #memorization,
    .palette-rose #homework-today,
    .palette-rose .settings-box {
        border: round #f472b6;
    }

    /* MONO */

    .palette-mono {
        background: #0c0c0c;
    }

    .palette-mono #hero {
        color: white;
        border-bottom: solid #a3a3a3;
    }

    .palette-mono .card,
    .palette-mono #memorization,
    .palette-mono #homework-today,
    .palette-mono .settings-box {
        border: round #a3a3a3;
    }

    """

    def __init__(self):

        super().__init__()

        self.db = Database(DB_FILE)

        self.current_schedule = None

        self.current_homework = {}

    # ========================================================
    # UI
    # ========================================================

    def compose(self) -> ComposeResult:

        yield Header()

        yield Static(
            "🏠 RICHMACK FAMILY OPERATING DASHBOARD",
            id="hero",
        )

        with TabbedContent(id="tabs"):

            # =================================================
            # TODAY
            # =================================================

            with TabPane(
                "Today",
                id="today-tab",
            ):

                with VerticalScroll():

                    with Horizontal(id="chore-top"):

                        with Vertical(classes="card"):

                            yield Static(
                                "👩‍🍳 COOK",
                                classes="card-title",
                            )

                            yield Static(
                                "",
                                id="cook-card",
                            )

                        with Vertical(classes="card"):

                            yield Static(
                                "🍽 KITCHEN",
                                classes="card-title",
                            )

                            yield Static(
                                "",
                                id="kitchen-card",
                            )

                        with Vertical(classes="card"):

                            yield Static(
                                "📅 TODAY",
                                classes="card-title",
                            )

                            yield Static(
                                "",
                                id="date-card",
                            )

                    with Horizontal(id="house-row"):

                        with Vertical(classes="card"):

                            yield Static(
                                "🛁 BATHROOMS",
                                classes="card-title",
                            )

                            yield Static(
                                "",
                                id="bathrooms-card",
                            )

                        with Vertical(classes="card"):

                            yield Static(
                                "🧹 KITCHEN CLEAN",
                                classes="card-title",
                            )

                            yield Static(
                                "",
                                id="deep-kitchen-card",
                            )

                        with Vertical(classes="card"):

                            yield Static(
                                "📦 BASEMENT",
                                classes="card-title",
                            )

                            yield Static(
                                "",
                                id="basement-card",
                            )

                        with Vertical(classes="card"):

                            yield Static(
                                "🧺 LAUNDRY",
                                classes="card-title",
                            )

                            yield Static(
                                "",
                                id="laundry-card",
                            )

                    with Vertical(id="memorization"):

                        yield Static(
                            "📚 MEMORIZATION",
                            classes="card-title",
                        )

                        yield Checkbox(
                            "Zara",
                            id="done-zara",
                        )

                        yield Checkbox(
                            "Jasmin",
                            id="done-jasmin",
                        )

                        yield Checkbox(
                            "Aria",
                            id="done-aria",
                        )

                    with Horizontal(id="buttons"):

                        yield Button(
                            "🎲 CHORES",
                            id="shuffle-chores",
                            variant="primary",
                        )

                        yield Button(
                            "🎓 HOMEWORK",
                            id="shuffle-homework-today",
                        )

                        yield Button(
                            "💾 SAVE ALL",
                            id="save-all",
                            variant="success",
                        )

                    yield Static(
                        "",
                        id="status",
                    )

            # =================================================
            # HOMEWORK
            # =================================================

            with TabPane(
                "Homework",
                id="homework-tab",
            ):

                with Vertical(id="homework-today"):

                    yield Static(
                        "🎓 TODAY'S SHUFFLED HOMEWORK",
                        classes="card-title",
                    )

                    yield DataTable(
                        id="today-homework-table",
                        zebra_stripes=True,
                        cursor_type="row",
                    )

                with Horizontal(id="homework-controls"):

                    yield Input(
                        placeholder=(
                            "Search assignments: "
                            "vocab, NotebookLM, reading..."
                        ),
                        id="assignment-search",
                    )

                    yield Select(
                        [
                            ("All Categories", "ALL")
                        ] + [
                            (category, category)
                            for category in HOMEWORK_CATEGORIES
                        ],
                        id="category-filter",
                        value="ALL",
                        allow_blank=False,
                    )

                with Horizontal(id="buttons"):

                    yield Button(
                        "🎲 SHUFFLE HOMEWORK",
                        id="shuffle-homework",
                        variant="primary",
                    )

                    yield Button(
                        "✅ TOGGLE DONE",
                        id="toggle-homework",
                    )

                    yield Button(
                        "💾 SAVE HOMEWORK",
                        id="save-homework",
                        variant="success",
                    )

                yield Static(
                    "",
                    id="homework-status",
                )

                yield Static(
                    "🔎 ASSIGNMENT LIBRARY",
                    classes="card-title",
                )

                yield DataTable(
                    id="assignment-table",
                    zebra_stripes=True,
                    cursor_type="row",
                )

            # =================================================
            # WEEK
            # =================================================

            with TabPane(
                "Week",
                id="week-tab",
            ):

                yield DataTable(
                    id="week-table",
                    zebra_stripes=True,
                    cursor_type="row",
                )

            # =================================================
            # HISTORY
            # =================================================

            with TabPane(
                "History",
                id="history-tab",
            ):

                yield DataTable(
                    id="history-table",
                    zebra_stripes=True,
                    cursor_type="row",
                )

            # =================================================
            # SETTINGS
            # =================================================

            with TabPane(
                "Settings",
                id="settings-tab",
            ):

                with VerticalScroll():

                    with Vertical(
                        classes="settings-box"
                    ):

                        yield Static(
                            "🎨 COLOR PALETTE",
                            classes="card-title",
                        )

                        yield Select(
                            [
                                (label, key)
                                for key, label
                                in PALETTES.items()
                            ],
                            id="palette",
                            allow_blank=False,
                        )

                        yield Button(
                            "💾 SAVE PALETTE",
                            id="save-palette",
                        )

                    with Vertical(
                        classes="settings-box"
                    ):

                        yield Static(
                            "🎓 SEARCHABLE STUDY CATEGORIES",
                            classes="card-title",
                        )

                        yield Static(
                            "\n".join(
                                f"• {category}"
                                for category
                                in HOMEWORK_CATEGORIES
                            )
                        )

        yield Footer()

    # ========================================================
    # STARTUP
    # ========================================================

    def on_mount(self):

        today_hw = self.query_one(
            "#today-homework-table",
            DataTable,
        )

        today_hw.add_columns(
            "Person",
            "Done",
            "Category",
            "Assignment",
            "Instructions",
        )

        catalog = self.query_one(
            "#assignment-table",
            DataTable,
        )

        catalog.add_columns(
            "ID",
            "Category",
            "Assignment",
            "Instructions",
        )

        week = self.query_one(
            "#week-table",
            DataTable,
        )

        week.add_columns(
            "Day",
            "Date",
            "Cook",
            "Counters/Stove",
            "Table/Chairs/Floor",
            "Bathrooms",
            "Kitchen",
            "Basement",
            "Laundry",
        )

        history = self.query_one(
            "#history-table",
            DataTable,
        )

        history.add_columns(
            "ID",
            "Date",
            "Cook",
            "Bathrooms",
            "Kitchen",
            "Basement",
            "Laundry",
        )

        self.load_palette()

        self.load_today()

        self.load_homework_today()

        self.refresh_assignment_library()

        self.refresh_week()

        self.refresh_history()

    # ========================================================
    # COOK
    # ========================================================

    def cook_for(self, target):

        cook = random.Random(
            f"cook-{ROTATION_ANCHOR.isoformat()}"
        ).choice(PEOPLE)

        current = ROTATION_ANCHOR

        if target >= current:

            while current < target:

                current += timedelta(days=1)

                choices = [
                    person
                    for person in PEOPLE
                    if person != cook
                ]

                cook = random.Random(
                    f"cook-{current.isoformat()}"
                ).choice(choices)

            return cook

        while current > target:

            current -= timedelta(days=1)

            choices = [
                person
                for person in PEOPLE
                if person != cook
            ]

            cook = random.Random(
                f"reverse-{current.isoformat()}"
            ).choice(choices)

        return cook

    # ========================================================
    # CHORES
    # ========================================================

    def build_day(self, target):

        cook = self.cook_for(target)

        others = [
            person
            for person in PEOPLE
            if person != cook
        ]

        kitchen_rng = random.Random(
            f"kitchen-{target.isoformat()}"
        )

        kitchen_rng.shuffle(others)

        return {
            "date": target.isoformat(),

            "day": target.strftime("%A"),

            "cook": cook,

            "dishes": cook,

            "counters_stove":
                others[0],

            "table_chairs_floor":
                others[1],

            "bathrooms":
                random.Random(
                    f"bathroom-{target.isoformat()}"
                ).choice(PEOPLE),

            "kitchen_clean":
                random.Random(
                    f"clean-kitchen-{target.isoformat()}"
                ).choice(PEOPLE),

            "basement":
                random.Random(
                    f"basement-{target.isoformat()}"
                ).choice(PEOPLE),

            "laundry":
                random.Random(
                    f"laundry-{target.isoformat()}"
                ).choice(PEOPLE),

            "books":
                self.books_for(target),
        }

    def books_for(self, target):

        shift = (
            target - ROTATION_ANCHOR
        ).days % len(BOOKS)

        return {
            person:
                BOOKS[
                    (index + shift)
                    % len(BOOKS)
                ]

            for index, person
            in enumerate(PEOPLE)
        }

    # ========================================================
    # TODAY
    # ========================================================

    def load_today(self):

        target = date.today()

        saved = self.db.get_chore_day(
            target.isoformat()
        )

        if saved:

            self.current_schedule = {
                "date": saved[1],
                "day": saved[2],
                "cook": saved[3],
                "dishes": saved[4],
                "counters_stove": saved[5],
                "table_chairs_floor": saved[6],
                "bathrooms": saved[7],
                "kitchen_clean": saved[8],
                "basement": saved[9],
                "laundry": saved[10],
                "books": self.books_for(target),
            }

            completions = (
                self.db.get_completions(
                    target.isoformat()
                )
            )

        else:

            self.current_schedule = (
                self.build_day(target)
            )

            completions = {}

        self.update_today(completions)

    def update_today(
        self,
        completions=None,
    ):

        s = self.current_schedule

        completions = completions or {}

        self.query_one(
            "#cook-card",
            Static,
        ).update(
            f"\n{s['cook']}\n\n"
            f"{s['cook']} cooks today.\n\n"
            f"🍽 {s['cook']} also does dishes."
        )

        self.query_one(
            "#kitchen-card",
            Static,
        ).update(
            f"🍽 Dishes\n{s['dishes']}\n\n"
            f"🧽 Counters + Stove\n{s['counters_stove']}\n\n"
            f"🪑 Table + Chairs + Floor\n"
            f"{s['table_chairs_floor']}"
        )

        self.query_one(
            "#date-card",
            Static,
        ).update(
            f"{s['day']}\n{s['date']}"
        )

        self.query_one(
            "#bathrooms-card",
            Static,
        ).update(
            s["bathrooms"]
        )

        self.query_one(
            "#deep-kitchen-card",
            Static,
        ).update(
            s["kitchen_clean"]
        )

        self.query_one(
            "#basement-card",
            Static,
        ).update(
            s["basement"]
        )

        self.query_one(
            "#laundry-card",
            Static,
        ).update(
            s["laundry"]
        )

        for person in PEOPLE:

            box = self.query_one(
                f"#done-{person.lower()}",
                Checkbox,
            )

            box.label = (
                f"{person} → "
                f"{s['books'][person]}"
            )

            box.value = completions.get(
                person,
                False,
            )

    # ========================================================
    # HOMEWORK SHUFFLE
    # ========================================================

    def shuffle_homework(self):

        tasks = self.db.search_assignments()

        if len(tasks) < len(PEOPLE):
            return

        chosen = random.sample(
            tasks,
            len(PEOPLE),
        )

        self.current_homework = {}

        for person, row in zip(
            PEOPLE,
            chosen,
        ):

            self.current_homework[person] = {
                "id": row[0],
                "category": row[1],
                "title": row[2],
                "description": row[3],
                "completed": False,
            }

        self.refresh_today_homework()

    def load_homework_today(self):

        saved = self.db.load_homework(
            date.today().isoformat()
        )

        if saved:

            self.current_homework = saved

        else:

            self.shuffle_homework()

        self.refresh_today_homework()

    def refresh_today_homework(self):

        table = self.query_one(
            "#today-homework-table",
            DataTable,
        )

        table.clear()

        for person in PEOPLE:

            task = self.current_homework.get(
                person
            )

            if not task:
                continue

            table.add_row(
                person,
                "✓" if task["completed"] else " ",
                task["category"],
                task["title"],
                task["description"],
                key=person,
            )

    # ========================================================
    # SEARCH ASSIGNMENTS
    # ========================================================

    def refresh_assignment_library(self):

        search = self.query_one(
            "#assignment-search",
            Input,
        ).value

        category = self.query_one(
            "#category-filter",
            Select,
        ).value

        if not isinstance(category, str):
            category = "ALL"

        rows = self.db.search_assignments(
            search,
            category,
        )

        table = self.query_one(
            "#assignment-table",
            DataTable,
        )

        table.clear()

        for row in rows:

            table.add_row(
                str(row[0]),
                row[1],
                row[2],
                row[3],
                key=str(row[0]),
            )

    def on_input_changed(
        self,
        event: Input.Changed,
    ):

        if event.input.id == "assignment-search":

            self.refresh_assignment_library()

    def on_select_changed(
        self,
        event: Select.Changed,
    ):

        if event.select.id == "category-filter":

            self.refresh_assignment_library()

        elif event.select.id == "palette":

            if isinstance(event.value, str):

                self.apply_palette(
                    event.value
                )

    # ========================================================
    # WEEK
    # ========================================================

    def refresh_week(self):

        table = self.query_one(
            "#week-table",
            DataTable,
        )

        table.clear()

        today = date.today()

        monday = (
            today
            - timedelta(
                days=today.weekday()
            )
        )

        for number in range(7):

            target = (
                monday
                + timedelta(days=number)
            )

            s = self.build_day(target)

            table.add_row(
                s["day"],
                target.strftime("%b %d"),
                s["cook"],
                s["counters_stove"],
                s["table_chairs_floor"],
                s["bathrooms"],
                s["kitchen_clean"],
                s["basement"],
                s["laundry"],
                key=target.isoformat(),
            )

    # ========================================================
    # HISTORY
    # ========================================================

    def refresh_history(self):

        table = self.query_one(
            "#history-table",
            DataTable,
        )

        table.clear()

        for row in self.db.chore_history():

            table.add_row(
                str(row[0]),
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                key=str(row[0]),
            )

    # ========================================================
    # ACTIONS
    # ========================================================

    def action_shuffle_chores(self):

        target = date.today()

        cook = self.cook_for(target)

        others = [
            person
            for person in PEOPLE
            if person != cook
        ]

        random.shuffle(others)

        self.current_schedule = {
            "date": target.isoformat(),
            "day": target.strftime("%A"),

            "cook": cook,
            "dishes": cook,

            "counters_stove":
                others[0],

            "table_chairs_floor":
                others[1],

            "bathrooms":
                random.choice(PEOPLE),

            "kitchen_clean":
                random.choice(PEOPLE),

            "basement":
                random.choice(PEOPLE),

            "laundry":
                random.choice(PEOPLE),

            "books":
                self.books_for(target),
        }

        self.update_today()

        self.query_one(
            "#status",
            Static,
        ).update(
            "🎲 Chores shuffled"
        )

    def action_shuffle_homework(self):

        self.shuffle_homework()

        self.query_one(
            "#tabs",
            TabbedContent,
        ).active = "homework-tab"

        self.query_one(
            "#homework-status",
            Static,
        ).update(
            "🎓 Homework shuffled • not saved"
        )

    def action_save_all(self):

        completions = {
            person:
                self.query_one(
                    f"#done-{person.lower()}",
                    Checkbox,
                ).value

            for person in PEOPLE
        }

        self.db.save_chore_day(
            self.current_schedule,
            completions,
        )

        self.db.save_homework(
            date.today().isoformat(),
            self.current_homework,
        )

        self.refresh_history()

        self.query_one(
            "#status",
            Static,
        ).update(
            "✓ Chores + homework saved"
        )

    def action_show_week(self):

        self.query_one(
            "#tabs",
            TabbedContent,
        ).active = "week-tab"

    # ========================================================
    # BUTTONS
    # ========================================================

    def on_button_pressed(
        self,
        event: Button.Pressed,
    ):

        button = event.button.id

        if button == "shuffle-chores":

            self.action_shuffle_chores()

        elif button in (
            "shuffle-homework",
            "shuffle-homework-today",
        ):

            self.action_shuffle_homework()

        elif button == "save-all":

            self.action_save_all()

        elif button == "save-homework":

            self.db.save_homework(
                date.today().isoformat(),
                self.current_homework,
            )

            self.query_one(
                "#homework-status",
                Static,
            ).update(
                "✓ Homework saved"
            )

        elif button == "toggle-homework":

            self.toggle_selected_homework()

        elif button == "save-palette":

            self.save_palette()

    # ========================================================
    # HOMEWORK DONE
    # ========================================================

    def toggle_selected_homework(self):

        table = self.query_one(
            "#today-homework-table",
            DataTable,
        )

        if table.row_count == 0:
            return

        try:

            key = table.coordinate_to_cell_key(
                table.cursor_coordinate
            ).row_key.value

        except Exception:
            return

        person = str(key)

        if person not in self.current_homework:
            return

        task = self.current_homework[
            person
        ]

        task["completed"] = (
            not task["completed"]
        )

        self.refresh_today_homework()

    # ========================================================
    # PALETTE
    # ========================================================

    def load_palette(self):

        palette = self.db.get_setting(
            "palette",
            "purple",
        )

        if palette not in PALETTES:
            palette = "purple"

        self.query_one(
            "#palette",
            Select,
        ).value = palette

        self.apply_palette(palette)

    def apply_palette(self, palette):

        for key in PALETTES:

            self.screen.remove_class(
                f"palette-{key}"
            )

        self.screen.add_class(
            f"palette-{palette}"
        )

    def save_palette(self):

        palette = self.query_one(
            "#palette",
            Select,
        ).value

        if not isinstance(palette, str):
            palette = "purple"

        self.db.set_setting(
            "palette",
            palette,
        )

        self.apply_palette(palette)

        self.notify(
            "Palette saved."
        )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    FamilyDashboard().run()
