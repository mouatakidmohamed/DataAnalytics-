# Description: This script practices using tuples and sets
# Author: Mohamed Mouatakid

candy_types = ("lollipop", "gummy bear", "hard candy")
fruit_flavors = ("mango", "strawberry", "watermelon")

candy_combinations = set()

candy_combinations.add(fruit_flavors[0] + " " + candy_types[0])
candy_combinations.add(fruit_flavors[1] + " " + candy_types[1])
candy_combinations.add(fruit_flavors[2] + " " + candy_types[2])

print("Today's candy options include:")
print(candy_combinations)

# Observation:
# Sets are unordered collections, so the order may not always display the same way.
