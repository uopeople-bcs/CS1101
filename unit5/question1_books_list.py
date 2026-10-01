# Question 1: Managing a list of books in the library
# Demonstrates: creating, adding (append), removing (remove), sorting (sort)

# Step 1: Create a list of book titles
books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]
print("Initial list of books:", books)

# Step 2: Add two more books using append()
books.append("To Kill a Mockingbird")
books.append("The Great Gatsby")
print("After adding two books:", books)

# Step 3: Remove one book that has been damaged using remove()
books.remove("Moby Dick")
print("After removing the damaged book:", books)

# Step 4: Sort the list alphabetically and display the final list
books.sort()
print("\nFinal sorted list of books:")
for book in books:
    print("-", book)
