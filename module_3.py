# Name: Dilawar Khan
# Roll Number: 45
# Date: November 7, 2026

# Warm-up — Predict, then run
# Write your prediction as a comment first, then run the code and explain any surprise.
a = [1, 2, 3]
b = a
b.append(4)
print(a)  #[1, 2, 3, 4] a and b refer to the same list in th memory, so appending to b also affects a.
print("===============================")
c = a.copy()
c.append(5)
print(a, c)       # [1, 2, 3, 4] [1, 2, 3, 4, 5] .copy create a new list with the same elements, so appending to c does not affect a.
print(a is b, a is c, a == a[:]) #True False True
print("===============================")

# Build — Fix the cart bug
# This function shares one cart between all customers. Show the bug with two calls, then fix
# it using none
def add_item(item, cart=[]):
  cart.append(item)
  return cart
customer_1= add_item("apple")
print(customer_1)
customer_2 = add_item("banana")
print(customer_2)
print("===============================")
# fix version:
print("======fix version======")
def add_item_fixed(item, cart=None):
  if cart is None:
    cart = []
  cart.append(item)
  return cart

customer1_fixed= add_item_fixed("apple")
print(customer1_fixed)
customer2_fixed = add_item_fixed("banana")
print(customer2_fixed)

print("===============================")

# Challenge — Safe class copy
import copy
classes = {"A": ["Ali", "Sara"]}
# shallow copy
shallow_copy = classes.copy()
classes["A"].append("dilawar")

# deep copy
deep_copy = copy.deepcopy(classes)
classes["A"].append("khan")

print("Original classes:", classes)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)