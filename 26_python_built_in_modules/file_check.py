import os
import sys

if len(sys.argv) < 2:
    print("Usage: python3 file_check.py greet.py")
else:

    name = sys.argv[1]
    if os.path.exists(name):
        print(f"File {name} exists")
        print(f"File size: {os.path.getsize(name)} bytes")
    else:
        print(f"File {name} does not found")
        
