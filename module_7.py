
# Name: Dilawar Khan
# Roll Number: 45
# Date: November 10, 2026

# Part 10 · Iterators, generators and decorators
#Warm-up — Countdown generator
# Generator 1: Countdown
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# Generator 2: Even numbers
def evens(limit):
    for number in range(0, limit + 1, 2):
        yield number


# Main program
print("===== COUNTDOWN =====")
for number in countdown(5):
    print(number)

print("\n===== EVEN NUMBERS =====")
print(list(evens(10)))
print("===============================================")
# Build — Big file reader
from pathlib import Path
def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


def error_lines(path):
    for line in read_lines(path):
        if "ERROR" in line:
            yield line


# Main program
print("===== ERROR LINES =====")

log_path = Path(__file__).with_name("logs.txt")
for line in error_lines(log_path):
    print(line)
print("===============================================")
#challenge  Your own decorators
import time
from functools import wraps


# Decorator 1: Timer
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")

        return result

    return wrapper


# Decorator 2: Log Calls
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function name:", func.__name__)
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = func(*args, **kwargs)

        return result

    return wrapper


# Function with both decorators
@timer
@log_calls
def sum_numbers(start, end):
    total = 0

    for number in range(start, end + 1):
        total += number

    return total


# Main program
result = sum_numbers(1, 1_000_000)

print("Sum:", result)