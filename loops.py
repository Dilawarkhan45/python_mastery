# Name: Dilawar khan
# Roll Number: TRN-2026-000961
# Date: 07/11/2026

# Part 3 · Loops (for / while)

# Warm-up — Times table





number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Build — ATM PIN check

correct_pin = "4321" #PIN is an identifier, not a number used for mathematical calculations, that why take as a string
tries_left = 3
while tries_left > 0:
  entered_pin = input("Enter your 4-digit PIN: ").strip()  #.strip() removes unnecessary spaces from the beginning and end
  if entered_pin == correct_pin:
    print("Welcome")
    break
  else:
    tries_left -= 1
    if tries_left > 0:
      print(f"Incorrect PIN. Tries left: {tries_left}")
    else:
      print("Card blocked")

# Challenge — Number guessing game
import random
while True:  #for multiple rounds of the game
  secret_number = random.randint(1, 100)
  guess = 0
  attempts = 0
  while guess != secret_number:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1
    if guess < secret_number:
      print("Too low! Try again.")
    elif guess > secret_number:
      print("Too high! Try again.")
    else:
      print(f"Got it in {attempts} guesses!")
  play_again = input("Do you want to play again? (yes/no): ").strip().lower()
  if play_again not in ("y", "yes"):
    print("Thanks for playing!")
    break
