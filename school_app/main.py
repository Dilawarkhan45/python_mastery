from school import average, grade, attendance_percentage, student_info

# Student marks
marks = [80, 90, 70]

avg = average(marks)
student_grade = grade(avg)

print("===== STUDENT RESULT =====")
print("Average:", round(avg, 2))
print("Grade:", student_grade)

# Attendance
attendance = attendance_percentage(30, 25)

print("\n===== ATTENDANCE =====")
print("Attendance:", f"{attendance:.2f}%")

print("\n===== STUDENT INFO =====")
print(student_info("Ali", 101))