def calculate_grade(marks):
    percentage = sum(marks) / len(marks)

    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    return "Fail"


if __name__ == "__main__":
    marks = [85, 90, 95]
    print("Grade:", calculate_grade(marks))