# Student Grades — practice rewrite
# Same style: helpers + main function

def student(score):
    """Return feedback message for one score."""
    if score >= 85:
        return "you did a wonderful job, keep going"
    elif score >= 75:
        return "you did a great job"
    elif score >= 65:
        return "you have to learn harder"
    elif score >= 55:
        return "you passed but you have to learn harder"
    else:
        return "you failed"


def student_average(*scores):
    """Return the average of all scores."""
    return sum(scores) / len(scores)


def show_report(*scores):
    """Show each score with feedback, then the average."""
    for score in scores:
        message = student(score)
        print(f"{score} is {message}")
    avg = student_average(*scores)
    print(f"average is {avg}")
    return avg


if __name__ == "__main__":
    show_report(100, 90, 95, 72, 65, 68, 50, 40)
