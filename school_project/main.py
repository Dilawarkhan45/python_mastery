
# main.py

from school_tools import average, grade, report, area_of_circle, is_even

# Student reports
print("===== STUDENT REPORTS =====")

print(report("Ali", [80, 90, 70]))
print(report("Sara", [95, 88, 92]))
print(report("Ahmed", [45, 55, 60]))

# Circle area
print("\n===== CIRCLE AREA =====")
print("Area:", area_of_circle(5))

# Even number
print("\n===== EVEN NUMBER =====")
print(is_even(12))
