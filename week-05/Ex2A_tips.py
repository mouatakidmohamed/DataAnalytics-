# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# str() converts a number to a string so it can be combined with text in print().
# print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))

# Example using an f-string
print(f"The total due is {total_due}")
