# Name: Dilawar Khan
# Roll Number: 45
# Date: November 7, 2026

# Part 4: Lists, dictionaries, tuples and sets 
# Warm-up — Shopping list

# items = ["milk", "bread", "eggs"]
# items.append("tea")
# items.remove("bread")
# print(f"Before sorting: {items}")
# sorted_items = sorted(items)
# print(f"After sorting: {sorted_items}")
# for index, item in enumerate(sorted_items):
#     print(f"{index}. {item}")


# # Build — Phone book

# contacts = {
#     "Alice": "123-456-7890",
#     "Bob": "987-654-3210",
#     "Charlie": "555-555-5555",
#     "David": "111-222-3333",
#     "Eve": "444-555-6666"
# }

# while True:
#     print("\nPhone Book Menu:")
#     print("1. Add contact")
#     print("2. Search contact")
#     print("3. Delete contact")
#     print("4. List all contacts")
#     print("5. Exit")

#     choice = input("Choose an option (1-5): ").strip()

#     if choice == "1":
#         name = input("Enter contact name: ").strip()
#         number = int(input("Enter contact number: ").strip())
#         contacts[name] = number
#         print(f"Added contact: {name} -> {number}")

#     elif choice == "2":
#         name = input("Enter contact name to search: ").strip()

#         number = contacts.get(name)

#         if number is not None:
#             print(f"Found: {name} -> {number}")
#         else:
#             print("Not found")

#     elif choice == "3":
#         name = input("Enter contact name to delete: ").strip()

#         if name in contacts:
#             del contacts[name]
#             print(f"Deleted contact: {name}")
#         else:
#             print("Not found")

#     elif choice == "4":
#         if contacts:
#             print("All contacts:")

#             for index, (name, number) in enumerate(contacts.items(), start=1):
#                 print(f"{index}. {name} -> {number}")
#         else:
#             print("No contacts found.")

#     elif choice == "5":
#         print("Exiting phone book.")
#         break

#     else:
#         print("Invalid option. Please choose again.")



# Challenge — Class result sheet
marks = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [65, 75, 82],
    "Ayesha": [35, 35, 45],
    "Bilal": [90, 92, 96]
}

topper = ""
highest_total = 0
below_40 = set()

print("===== CLASS RESULT SHEET =====")

for name, scores in marks.items():
    total = sum(scores)
    average = total / len(scores)

    print(f"{name}: Total = {total}, Average = {average:.2f}")

    # Find topper (average 90 or above)
    if average >= 90 and total > highest_total:
        highest_total = total
        topper = name

    # Find students with average below 40
    if average < 40:
        below_40.add(name)

print("\n===== CLASS TOPPER =====")

if topper:
    print(f"Topper: {topper}")
    print(f"Highest Total Marks: {highest_total}")
else:
    print("No student qualified as topper.")

print("\n===== STUDENTS WITH AVERAGE BELOW 40 =====")
if below_40:
    print("Students with average below 40:", below_40)
else:
    print("No student has an average below 40.")
