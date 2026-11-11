# Name: Dilawar Khan
# Roll Number: 45
# Date: November 10, 2026

# Part 8 · Modules, packages and projects

# Warm-up — Standard library tour
# square root of 144
import math
number = 144
print(math.sqrt(number))
# pick random student from list
import random
students = ["ali","waqas","dilawar","babar"]
random_student = random.choice(students)
print(random_student)
print("==================================")
# days left until 31 December)
import datetime
today_date = datetime.date.today()
last_date = datetime.date(today_date.year,12,31)
days_left = (last_date - today_date).days
print(f"today date: {today_date}")
print(f"Days left until 31 december: {days_left}")
print("===========================================")
# Statistics: Mean and Median of 5 marks
import statistics
marks = [23, 24, 36, 46, 47]
mean = statistics.mean(marks)
median = statistics.median(marks)
print(f"Mean: {mean}")
print(F"Median: {median}")

# Build — Your own module
# school project directory
  #  main.py
  #school_tools.py
#Challenge — Real project setup
#school App