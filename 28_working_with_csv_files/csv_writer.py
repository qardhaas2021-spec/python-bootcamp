import csv

with open("people.csv", "a", newline="") as f:
    writer = csv.writer(f)
    csvdata = (5, "Farah", "Amsterdam")
    writer.writerow(csvdata)


with open("numbers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "x*2", "x*3" ])
    for x in range(1, 11):
        writer.writerow([x, x*2, x*3])
        