# Student Grade System

print("===== STUDENT GRADE SYSTEM =====")

name = input("Enter student name: ")
marks = float(input("Enter your marks (0-100): "))

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter 0 to 100.")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")

print("==============================")
