# Description: This script practices using Python lists with movie titles
# Author: Mohamed Mouatakid

favorite_movies = [
    "Inception",
    "The Dark Knight",
    "Interstellar",
    "Avatar",
    "Black Panther"
]

print("The list favorite_movies includes my top " + str(len(favorite_movies)) + " favorite movies.")
print(favorite_movies)

print("\nUsing sorted():")
print(sorted(favorite_movies))
print(favorite_movies)

# Observation:
# sorted() prints a sorted version, but it does not permanently change the original list.

print("\nUsing .sort():")
favorite_movies.sort()
print(favorite_movies)

# Observation:
# .sort() permanently changes the original list.

favorite_movies.append("Spider-Man: No Way Home")

print("\nAfter adding one more movie:")
print("The list favorite_movies now includes my top " + str(len(favorite_movies)) + " favorite movies.")
print(favorite_movies)

# Group comparison:
# My group members should have similar results if they used len(), sorted(), sort(), and append() correctly.
