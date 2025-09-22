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

* `todo.py` — the main script (or rename to `app.py` as you prefer)

---

## Setup & Run

1. Save the provided code into a file named `todo.py`.
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
python todo.py
# or
python3 todo.py
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

## Important notes & suggested fixes

* **Indexing bug / off-by-one:** The original `removetask` function calls `tasks.pop(tasknumber)`. When the user types `1` to remove the first task, `pop(1)` actually removes the second item (Python lists use 0-based indices). To fix this, subtract 1 before popping and validate the index. Example fix:

```python
def removetask(tasknumber):
    idx = tasknumber - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        print("task removed!!")
    else:
        print("invalid task number")
```

* **Input validation:** The script currently assumes valid input for integers. Consider wrapping conversions in `try/except` to handle bad input gracefully.
* **Persistence:** This app keeps tasks in memory only. To persist tasks between runs, save/load from a text file or a lightweight database (e.g., `json` file or SQLite).
* **Function / style suggestions:** Use consistent function naming (snake\_case) and add docstrings to improve readability and maintainability.

---

## Example session

```
1 Add Task
2.Show Tasks
3.Remove Task
4- Exit
enter choice : 1
enter task : Buy groceries
task added!
enter choice : 2
1 . Buy groceries
enter choice : 3
enter task no to remove: 1
task removed!!
```

---

## Contributing & License

Feel free to fork and improve. Add unit tests (`pytest`) and a small CLI parser if you want to expand the app. No license is set by default.

---

If you want, I can create an improved `todo.py` with the indexing fix and input validation, plus a simple persistence layer.
