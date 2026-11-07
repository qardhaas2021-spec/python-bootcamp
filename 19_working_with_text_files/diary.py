# DIARY APP - practice read + write
from pathlib import Path
from datetime import date

diary_file = Path(__file__).parent / "diary.txt"

# 1) Ask for today's note
note = input("What happened today? ")

# 2) Save (append) the note with today's date
with open(diary_file, "a") as f:
    f.write(f"{date.today()}: {note}\n")

print("Saved!\n")

# 3) Read and show all notes
with open(diary_file) as f:
    print("--- My Diary ---")
    print(f.read())
