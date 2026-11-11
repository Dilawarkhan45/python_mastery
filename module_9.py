# Part 12 · Debugging and testing 
# Warm-up: Fix 3 bugs

marks = [90, 25, 70]
passing = []

for m in range(len(marks)):
    if marks[m] > 33:
        passing.append(marks[m])

print(sum(passing) / len(passing))
#Logic error
# First bug: range(len(marks) - 1) skips the last mark, 70. We need to check every mark.
# Second bug: passing = [marks[m]] replaces the existing list each time. append() adds a mark without removing previous marks.
# Third bug: We must divide by the number of passing marks, not the total number of marks.


# Build: Test your grade function
#grades.py
#test_grades.py

# Challenge — Test the bank account
# bank_account.py
#test_bank_accounts.py
