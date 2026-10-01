# Question 3: Tuple packing and unpacking
# Demonstrates: packing, unpacking, and the zip() / zip(*) functions

# Step 1: Pack a book title, author, and publication year into a tuple.
# No parentheses are needed - it is the commas that create the tuple (packing).
book_info = "The Alchemist", "Paulo Coelho", 1988
print("Packed tuple book_info:", book_info)
print("Type of book_info:", type(book_info))

# Step 2: Unpack the tuple into separate variables
title, author, year = book_info

# Print them in a readable format
print("\nBook details:")
print("Title:", title)
print("Author:", author)
print("Publication year:", year)

# Step 3: zip() - pack two parallel tuples element by element (row view)
titles = ("The Alchemist", "1984", "Moby Dick")
authors = ("Paulo Coelho", "George Orwell", "Herman Melville")
catalog = tuple(zip(titles, authors))
print("\nPaired records (zip):", catalog)

# Step 4: zip(*) - the star unpacks the pairs into separate arguments,
# and zip() re-packs them by position (column view)
titles_again, authors_again = zip(*catalog)
print("Separated titles:", titles_again)
print("Separated authors:", authors_again)
