import os
import subprocess

os.system("ls")

code = os.system("echo 'Hello Ahmed'")

print(code)

os.system("pwd")
os.system("mkdir notes")
os.system("python3 greet.py")

name = "Ahmed"
os.system(f"echo Hello, {name}")

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)