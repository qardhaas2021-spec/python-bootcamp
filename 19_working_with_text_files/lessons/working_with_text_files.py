# working with text files in python
# open() opens a file
# "w" = write (creates / overwrites)
# "r" = read
# "a" = append (add to the end)
# always close the file, or use "with" so Python closes it for you


# write to a file
with open("notes.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("I am learning text files\n")


# read the whole file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)


# append more text
with open("notes.txt", "a") as file:
    file.write("This line was added later\n")


# read line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
