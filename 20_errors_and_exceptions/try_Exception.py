from pathlib import Path

f = open("myfile.txt", "w")

try:
    f.write("Something to the file")

except:
    print("can not write to the file")

else:
    print("File written successfully")

finally:
    print("This code will always run")
    if not f.closed:
        f.close()
    print(f"file is closed: {f.closed}")

print("Some other code")