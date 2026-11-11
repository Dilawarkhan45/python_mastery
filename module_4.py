# Name: Dilawar Khan
# Roll Number: 45
# Date: November 10, 2026

# Part 7 · Exceptions and files
# Warm-up — Safe division

def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return result
    except ValueError:
        print("Error: Invalid numeric format. Please enter valid numbers.")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Denominator must be non-zero.")
        return None
print(safe_divide((input("Enter numerator: ")),(input("Enter denominator: "))))
print("================================")

# Build — Daily diary
import datetime

import json
while True:
    print("\n======Daily Diary======")
    print("1. Add Notes")
    print("2. Show Notes")
    print("3. exit")
    choice = input("Enter option(1-3):")

    if choice == "1":
        notes = input("enter notes")
        today = datetime.date.today()
        with open("diary.txt", "a") as file: #create a .txt file automatically 
            file.write(f"\nDate: {today}\n")
            file.write(f"Note: {notes}\n")
            file.write("------------------------\n")
        print("notes added")
    elif choice == "2":
        try:
            with open("diary.txt", "r") as file:
                entries = file.read()

                if entries:
                    print("\n===== YOUR DIARY ENTRIES =====")
                    print(entries)
                else:
                    print("No entries yet")

        except FileNotFoundError:
            print("No entries yet")
    elif choice == "3":
        print("Exit")
        break
    else:
        print("Invalid input")
print("==============================")

# Challenge — CSV result sheet
import csv
import json
marks = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [65, 75, 82],
    "Ayesha": [35, 35, 45],
    "Bilal": [90, 92, 96]
}
students = []
for name, scores in marks.items():
    average = sum(scores) / len(scores)

    students.append({
        "name": name,
        "marks": scores,
        "average": round(average, 2)
    })

topper = max(students, key=lambda student: student["average"], default=None)

# Save student results and the topper section to CSV
with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Mark1", "Mark2", "Mark3", "Average"])

    for student in students:
        writer.writerow([
            student["name"],
            student["marks"][0],
            student["marks"][1],
            student["marks"][2],
            student["average"]
        ])

    if topper:
        writer.writerow([])
        writer.writerow(["Topper"])
        writer.writerow(["Name", "Average"])
        writer.writerow([topper["name"], topper["average"]])

# Save data to JSON
with open("results.json", "w") as file:
    json.dump(students, file, indent=4)

print("Results saved successfully!")

if topper:
    print("Topper:", topper["name"])
    print("Average:", topper["average"])
else:
    print("No student records found.")
