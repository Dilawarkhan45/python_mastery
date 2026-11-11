# Name: Dilawar Khan
# Roll Number: 45
# Date: November 7, 2026

# Part 5 · Functions and comprehensions 
# Warm-up — Small helpers

def area_of_circle(r):
  area = 3.14 * r ** 2
  return area
print(f'Area of circle: {area_of_circle(5)} cm²')

print("==================================")

def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False

print(f'Is 4 even? {is_even(4)}')
print(f'Is 7 even? {is_even(7)}')

print("==================================")

def greet(name, lang="en"):

  if lang == "en":
    return f"Hello, {name}!"
  elif lang == "ur":
    return f"Salaam, {name}!"
  else:
    return f"Hello, {name}!"  # Default to English if unknown language code
print(greet("Alice"))
print(greet("Ahmed", "ur"))
print(greet("John", "en")) 
print("==================================")
# Build — Marks toolkit

def average(marks):
  return sum(marks) / len(marks)


def grade(avg):
  if avg >= 90 and avg <= 100:
    return "Grade: A+"
  elif avg >= 80 and avg <= 89:
    return "Grade: A"
  elif avg >= 70 and avg <= 79:
    return "Grade: B"
  elif avg >= 60 and avg <= 69:
    return "Grade: C"
  elif avg >= 50 and avg <= 59:
    return "Grade: D"
  else:
    return "Fail"

def report(name,marks):
  avg = average(marks)
  grd = grade(avg)
  return f"Report for {name}: Average Marks = {avg:.2f}, {grd}"
print(report('Alice', [85, 90, 78]))
print(report('Bob', [45, 55, 60]))
print(report('Charlie', [95, 92, 88]))
print("==================================")

# Challenge — Comprehensions
#Squares of 1-10 in one line
squares = [x**2 for x in range(1, 11)]
print(f"Squares of 1-10: {squares}")
print("==================================")
# only the names longer than 4 letters from a list
names = ["Ali", "Ahmed", "Sara", "Fatima", "Hassan"]
long_names = [name for name in names if len(name) > 4]
print(f"Names longer than 4 letters: {long_names}")
print("=========================================")
#a dict of {name: average} from your Part 4 result sheet
marks = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [65, 75, 82],
    "Ayesha": [35, 35, 20],
    "Bilal": [90, 92, 96]
}

averages = {name: f"{sum(scores) / len(scores):.2f}" for name, scores in marks.items()}

print(f"averages: {averages}")
print("========================================================")
# Passing students only (average >= 33)
passing_students = {name: f"{sum(scores) / len(scores):.2f} "for name, scores in marks.items() if sum(scores) / len(scores) >= 33}

print(f"passing_students average >=33: {passing_students}")