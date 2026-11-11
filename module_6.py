# Name: Dilawar Khan
# Roll Number: 45
# Date: November 10, 2026
# Part 9 · OOP — classes and objects 

# Warm-up — Student class
class student:
  def __init__(self,name,roll_no,marks):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks

  def average(self):
    return sum(self.marks) / len(self.marks)
    
  def add_mark(self,mark):
    self.marks.append(self.mark)

  def __str__(self):
    return f"{self.name} roll no: {self.roll_no} avg {self.average():.1f}"
student_1 = student("ali",12, [80,82,83])
print(student_1)
print("=================================================")
# Build — Bank account

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: {amount}")

    def print_history(self):
        print(f"\nTransaction History for {self.owner}:")
        for transaction in self.transaction_history:
            print(transaction)

        print("Current Balance:", self.balance)

account1 = BankAccount("Ali", 5000)

account1.deposit(2000)
account1.withdraw(1500)

print("Owner:", account1.owner)
print("Balance:", account1.balance)

account1.print_history()

print("=======================================")
# Challenge — Library system
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"Borrowed: {book.title}")
                else:
                    print("Book is already borrowed.")
                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"Returned: {book.title}")
                else:
                    print("Book is already available.")
                return

        print("Book not found.")

    def available_books(self):
        print("\n===== AVAILABLE BOOKS =====")

        for book in self.books:
            if book.available:
                print(book)


class EBook(Book):
    def __init__(self, title, author, file_size, available=True):
        super().__init__(title, author, available)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author} | File Size: {self.file_size} MB"


# ===== MAIN PROGRAM =====

my_library = Library()

book1 = Book("Python Basics", "John Smith")
book2 = Book("Machine Learning", "Andrew Ng")
ebook1 = EBook("Deep Learning", "Ian Goodfellow", 25)

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(ebook1)

my_library.available_books()

print("\n===== BORROW BOOK =====")
my_library.borrow("Python Basics")

my_library.available_books()

print("\n===== RETURN BOOK =====")
my_library.return_book("Python Basics")

my_library.available_books()