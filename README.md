# Python Bootcamp (course folders)

Folder numbers match the **Udemy course section numbers**.

```
python_bootcamp/
  03_python_basics/
  06_strings/
  08_program_flow_control/
  09_python_loops/
  11_lists/
  13_tuples/
  14_sets_and_frozensets/
  15_dictionaries/
  17_functions/
  19_working_with_text_files/
  20_errors_and_exceptions/     ← you are here
  _future_sections/             ← modules, classes (extra / later)
```

Each section can have:
- `lessons/` — practice scripts for videos
- `projects/` — section projects (e.g. phonetic alphabet, calculator)

## Outside this folder

- `../my_projects/` — your own apps (not course lessons)
- `../_archive_old/` — old mixed folders (safe backup, not deleted)

## Tip for file paths

When a `.txt` is next to your `.py` script:

```python
from pathlib import Path
f = open(Path(__file__).parent / "configuration.txt")
```
