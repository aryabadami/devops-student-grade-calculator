"""Student grade calculator module."""


def calculate_grade(score_list):
    """Calculate grade from a list of marks."""
    percentage = sum(score_list) / len(score_list)

    if percentage >= 90:
        return "A"
    if percentage >= 75:
        return "B"
    if percentage >= 50:
        return "C"
    return "Fail"


if __name__ == "__main__":
    student_marks = [85, 90, 95]
    print("Grade:", calculate_grade(student_marks))