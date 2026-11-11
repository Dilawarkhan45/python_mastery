
# school_tools.py

import math

# Function 1: Calculate average
def average(marks):
    return sum(marks) / len(marks)


# Function 2: Calculate grade
def grade(avg):
    if avg >= 90 and avg <= 100:
        return "A+"
    elif avg >= 80 and avg < 90:
        return "A"
    elif avg >= 70 and avg < 80:
        return "B"
    elif avg >= 60 and avg < 70:
        return "C"
    elif avg >= 50 and avg < 60:
        return "D"
    else:
        return "Fail"


# Function 3: Generate student report
def report(name, marks):
    avg = average(marks)
    student_grade = grade(avg)

    return f"{name}: Average = {avg:.2f}, Grade = {student_grade}"


# Function 4: Calculate circle area
def area_of_circle(r):
    return math.pi * r ** 2


# Function 5: Check even number
def is_even(n):
    return n % 2 == 0


# Test block
if __name__ == "__main__":
    print("Testing school_tools.py")

    print(report("Ali", [80, 90, 70]))
    print(report("Sara", [95, 88, 92]))

    print("Circle area:", area_of_circle(5))
    print("Is 10 even?", is_even(10))
