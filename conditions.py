# Name: Dilawar khan
# Roll Number: TRN-2026-000961
# Date: 07/11/2026

# Part 2 · Conditions (if / elif / else)
# Warm-up — Even, odd and sign, negative, positive, zero

#negative, positive, zero
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")
print("--------------------------------------------------")
#even, odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
print("--------------------------------------------------")

# Build — Grade calculator
marks = float(input("Enter marks: "))
if marks >=90 and marks <= 100:
    print("Grade: A+")
elif marks >= 80 and marks <= 89:
    print("Grade: A")
elif marks >= 70 and marks <= 79: 
    print("Grade: B")
elif marks >= 60 and marks <= 69:
    print("Grade: C")
elif marks >= 50 and marks <= 59:
    print("Grade: D")
else:
    print("Fail")
print("--------------------------------------------------")

# Challenge — Electricity bill
unit = int(input("Enter electricity units consumed: "))
fixed_charges = 50
if unit < 0:
    print("Invalid input")
else:
    if unit <= 100:
        bill = unit * 10
    elif unit <= 200:
        bill = unit * 15
    else:
        bill = unit * 20

    print(f"Bill: Rs {bill}")
    print(f"Total Bill: Rs {bill + fixed_charges}")
