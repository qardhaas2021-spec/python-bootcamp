# Student Grades Project
# Style: helper functions + one main function (show_report)

def get_letter(score):
    """Return the letter grade for one score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def average(*scores):
    """Return the average of all scores."""
    return sum(scores) / len(scores)


def show_report(*scores):
    """Show each score with its letter, then the average."""
    for score in scores:
        letter = get_letter(score)
        print(f"{score} is {letter}")
    avg = average(*scores)
    print(f"Average is {avg}")
    return avg


if __name__ == "__main__":
    show_report(90, 85, 70, 75, 60)
