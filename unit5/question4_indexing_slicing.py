# Question 4: Indexing and slicing to manage weekly borrowing statistics
# Demonstrates: slicing to extract records, indexing to modify a value

# Given list: books borrowed each day/week (7 records)
borrowed_books = [23, 19, 31, 27, 22, 30, 25]
print("Original list:", borrowed_books)

# Step 1: Extract the records from week 2 to week 5 using slicing.
# Week 1 is at index 0, so week 2 is index 1 and week 5 is index 4.
# Slice [1:5] returns indexes 1, 2, 3, 4 (upper bound is exclusive).
weeks_2_to_5 = borrowed_books[1:5]
print("\nRecords for weeks 2 to 5:", weeks_2_to_5)

# Step 2: Replace the number of books borrowed in week 1 with 20 using indexing.
# Week 1 is stored at index 0.
borrowed_books[0] = 20
print("\nWeek 1 record updated to 20.")

# Step 3: Display the updated list and the sliced portion
print("Updated full list:", borrowed_books)
print("Sliced portion (weeks 2-5):", borrowed_books[1:5])
