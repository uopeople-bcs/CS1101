# Question 2: Storing a borrower's immutable personal details in a tuple
# Demonstrates: tuple creation, immutability, len(), iteration,
#               and mutability of a list NESTED inside a tuple

# Step 1: Create a tuple (name, library ID, membership date)
borrower = ("John Doe", "B1023", "2025-10-15")
print("Borrower tuple:", borrower)

# Step 2: Attempt to modify one element (expected to fail - tuples are immutable)
try:
    borrower[1] = "B2098"          # trying to change the library ID
except TypeError as error:
    print("Error:", error)

# The correct way to "change" a tuple is to create a new one:
borrower = ("John Doe", "B2098", "2025-10-15")
print("Updated borrower tuple:", borrower)

# Step 3: Print the length of the tuple
print("\nNumber of data fields:", len(borrower))

# Display each element using a loop
print("Borrower details:")
for field in borrower:
    print("-", field)

# Step 4: A LIST nested inside a tuple CAN be modified.
# The tuple is immutable in its first layer only: it always holds the same
# references, but a mutable object it points to (a list) can change.
borrower_record = ("John Doe", "B1023", "2025-10-15",
                   ["The Alchemist", "Moby Dick"])   # 4th field: borrowed books
print("\nBorrower record:", borrower_record)

try:
    borrower_record[3] = []            # replacing the whole list FAILS
except TypeError as error:
    print("Error:", error)

borrower_record[3].append("1984")      # editing the list INSIDE succeeds
print("After borrowing another book:", borrower_record)
