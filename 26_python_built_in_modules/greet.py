import sys

if len(sys.argv) < 2:
    print("please give a name: python greet.py Ahmed")
else:
    print(f"Hello, {sys.argv[1]}!")

if len(sys.argv) < 2:
    print("Usage: pythonn report.py 26-09-25")
else:
    date = sys.argv[1]
    print(f"Building sales report for {date}")
