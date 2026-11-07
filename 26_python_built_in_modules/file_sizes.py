import os
from datetime import datetime
import shutil

print("_____files sizes in this folder_____")
for name in os.listdir("."):
    if name.endswith(".py"):
        size_kb = os.path.getsize(name) / 1024
        print(f"{name}: {size_kb:.1f} KB")


print("_____files modified time in this folder_____")
today = datetime.now().strftime("%Y-%m-%d")
folder = os.path.join("notes", today)
os.makedirs(folder, exist_ok=True)
print(f"folder created: {folder}, {today}")


note_path = os.path.join(folder, "note.txt")
with open(note_path, "w") as f:
    f.write("I practiced os and datetime.\n")
    f.write("I learned about the file sizes and the modified time.\n")
print(f"Saved: {note_path}")

os.makedirs("backup", exist_ok=True)
shutil.copy("greet.py", "backup/greet.py")
print("backup created: backup/greet.py")

