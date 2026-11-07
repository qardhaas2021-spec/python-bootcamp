import statistics

scores = [85, 90, 78, 92, 88]
print(statistics.mean(scores))
print(statistics.median(scores))
print(statistics.mode(scores))

grades = [60, 75, 80, 90, 55, 88, 72]
average = statistics.mean(grades)

if average >= 70:
    print("class doing well")
    print(f"Average: {average:.2f}")
    print("class doing well")
else:
    print("Need improvement")
