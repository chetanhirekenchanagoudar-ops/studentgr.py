def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 55:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return "F"


def display_grade(name, marks):
    grade = calculate_grade(marks)
    print("Student name:", name)
    print("Marks:", marks)
    print("Grade:", grade)


name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if name == "":
    name = "Student"

display_grade(name, marks)