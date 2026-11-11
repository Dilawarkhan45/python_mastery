# Name: Dilawar khan
# Roll Number: TRN-2026-000961
# Date: 07/11/2026

#Part 1 · Variables, data types, input and output
# Warm-up — Student ID card
name = input("enter your name: ")
age = int(input("enter your age: "))
class_name = int(input("enter your class: "))
city = input("enter your city: ")

print("======== STUDENT CARD ========")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"Class: {class_name}")
print(f"City : {city}")
print("==============================")

print("\n=====Data Types=====")
print(f"  name  : {type(name)}")
print(f"  age   : {type(age)}")
print(f"  class : {type(class_name)}")
print(f"  city  : {type(city)}")
print("==============================")


# Build — Shop bill
item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter item quantity: "))

subtotal = price * quantity
discount = subtotal * 0.05
tax = (subtotal - discount) * 0.17
total = subtotal - discount + tax

print("========== SHOP BILL ==========")
print(f"Item Name         : {item}")
print(f"Price        : Rs {price:.2f}") 
print(f"Quantity          : {quantity}")
print(f"Subtotal          : Rs {subtotal:.2f}")
print(f"5% Discount       : -Rs {discount:.2f}")
print(f"17% Tax           : +Rs {tax:.2f}")
print(f"Total       : Rs {total:.2f}")
print("===============================")

# Challenge — Unit converter
Temperature = float(input("Enter temperature in Celsius: "))
fahrenheit = (Temperature * 9/5) + 32
print(f"{Temperature:.1f}°C is equal to {fahrenheit:.1f}°F")

km = float(input("Enter distance in km: "))
miles = km * 0.621371
metres = km * 1000
print(f"Miles: {miles:.1f} mi")
print(f"Metres: {metres:.1f} m")