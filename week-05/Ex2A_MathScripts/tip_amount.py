# Description: Calculate tip amount
# Author: Mohamed Mouatakid

bill_amount = 45.50
tip_percent = 0.20

tip_amount = bill_amount * tip_percent

print(f"The tip on a ${bill_amount} restaurant bill is ${format(tip_amount, '.2f')}")
