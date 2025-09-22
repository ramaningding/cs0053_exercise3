# Simple Python To‑Do App

A minimal, console-based To‑Do list application written in Python. This small script demonstrates basic list operations and a simple text menu for adding, viewing, and removing tasks.

---

## Features

* Add tasks (appends to an in-memory list)
* Show all tasks with numbering
* Remove a task by its number from the list
* Simple, zero-dependency script — good for learning Python basics

---

## Requirements

* Python 3.7+ (no external packages required)

---

## Files

* `todo_app.py` — the main script

---

## Setup & Run

1. Save the provided code into a file named `todo_app.py`.
2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# mac / linux
source venv/bin/activate
# windows
venv\Scripts\activate
```

3. Run the app:

```bash
python todo_app.py
# or
python3 todo_app.py
```

---

## Usage

When you run the script you will see a simple menu:

```
1 Add Task
2.Show Tasks
3.Remove Task
4- Exit
```

* Choose `1` to add a task, then type the task text and press Enter.
* Choose `2` to list tasks. Tasks are shown numbered starting at `1`.
* Choose `3` to remove a task: enter the task number shown in the list.
* Choose `4` to exit the program.

---
