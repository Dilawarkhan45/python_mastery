
# Name: Dilawar Khan
# Roll Number: 45
# Date: November 10, 2026

# Part 5 - Functions and Comprehensions
# Type Hints Exercise


# ==================================
# 1. Warm-up - Small Helpers

# Area of circle
def area_of_circle(r: float) -> float:
    area = 3.14 * r ** 2
    return area


print(f"Area of circle: {area_of_circle(5)} cm²")

print("==================================")


# Check even number
def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

print("==================================")


# Greeting function
def greet(name: str, lang: str = "en") -> str:

    if lang == "en":
        return f"Hello, {name}!"
    elif lang == "ur":
        return f"Salaam, {name}!"
    else:
        return f"Hello, {name}!"


print(greet("Alice"))
print(greet("Ahmed", "ur"))
print(greet("John", "en"))

print("==================================")


# Build — Product dataclass

from dataclasses import dataclass, field, asdict
import json


# Define Product dataclass
@dataclass(order=True)
class Product:
    price: float
    name: str
    stock: int
    tags: list[str] = field(default_factory=list)

    # Validate price and stock
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative.")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative.")


# Create 5 products
products = [
    Product(120000, "Laptop", 5, ["Electronics", "Computer"]),
    Product(1500, "Mouse", 0, ["Electronics", "Accessory"]),
    Product(3000, "Keyboard", 8, ["Electronics"]),
    Product(5000, "Headphones", 0, ["Audio", "Accessory"]),
    Product(45000, "Monitor", 3, ["Electronics", "Display"])
]


# Print all products that are out of stock
print("===== OUT OF STOCK PRODUCTS =====")

for product in products:
    if product.stock == 0:
        print(f"Name: {product.name}")
        print(f"Price: {product.price}")
        print(f"Stock: {product.stock}")
        print(f"Tags: {product.tags}")
        print("-------------------------")


# Challenge: Save products to JSON

with open("products.json", "w") as file:
    json.dump(
        [asdict(p) for p in products],
        file,
        indent=4
    )

print("\nProducts saved successfully!")


# Load products from JSON

with open("products.json", "r") as file:
    data = json.load(file)

loaded_products = [Product(**d) for d in data]

print("Products loaded successfully!")


# Sort products by price

loaded_products.sort()

print("\n===== PRODUCTS SORTED BY PRICE =====")

for product in loaded_products:
    print(f"{product.name}: {product.price}")


# Display out-of-stock products after loading

print("\n===== OUT OF STOCK PRODUCTS AFTER LOADING =====")

for product in loaded_products:
    if product.stock == 0:
        print(product.name)
