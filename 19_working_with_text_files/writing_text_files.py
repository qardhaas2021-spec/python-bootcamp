# WRITING TO TEXT FILES
from pathlib import Path

with open("myfile.txt", "w") as f:
    f.write("I am Ahmed Abdullahi qardhaas.\n")
    f.write("I am a student of computer science at the university of sligo.\n")
    print("file saved!")
    f.write("after finish python course i will be a software engineer.\n")
   

with open("myfile.txt", "a") as f:
    f.write("My age is 28 years old.\n")
    f.write("I am from somalia.")

with open("myfile.txt", "r") as f:
    print(f.read())
   
with open("myfile.txt", "a") as f:
    f.write("I started learning python in 2025.\n")

with open("myfile.txt", "r") as f:
    for line in f:
        print(line)

    lines = [
        "i am going to the gym today.\n",
        "i am going to the park today.\n",
        "i am going to the movie today.\n",
          ]
    with open("myfile.txt", "a") as f:
        for line in lines:
            f.write(line)
    
    with open("myfile.txt", "r") as f:
        for line in f:
            print(line)
    
    with open("myfile.txt", "a") as f:
        f.write("just a test line.\n")

    with open("myfile.txt", "a") as f:
        f.write("i started now for reading the files.\n")

    with open("myfile.txt", "a") as f:
        f.write("sometimes is hard to read the files.")
 
    with open("myfile.txt", "r") as f:
        for line in f:
            print(line)
            
    




