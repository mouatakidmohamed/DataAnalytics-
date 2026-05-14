# Description: Calculate tip amount using input
# Author: Mohamed Mouatakid

bill_amount = float(input("What is the restaurant bill amount? "))
tip_percent = float(input("What tip percentage do you want to leave? Example: enter 20 for 20% "))

tip_amount = bill_amount * (tip_percent / 100)

print(f"The tip on a ${format(bill_amount, '.2f')} restaurant bill is ${format(tip_amount, '.2f')}")

# Observation:
# input() always starts as a string, so I must convert it to float before doing math.
# A possible problem is that the program will error if the user types words instead of numbers.
