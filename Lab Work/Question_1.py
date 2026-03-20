#Student Grade Analyzer

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Loop for 5 students
for i in range(5):
    marks = int(input("Enter marks: "))
    grade = calculate_grade(marks)
    print("Grade:", grade)