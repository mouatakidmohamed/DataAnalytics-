# Description: Estimate how long savings will take to double using the rule of 72
# Author: Mohamed Mouatakid

current_savings = 1000
interest_rate = 0.06

years_to_double = 72 / (interest_rate * 100)
doubled_balance = current_savings * 2

print(f"Your current savings is {current_savings}.")
print(f"At a {format(interest_rate, '.0%')} interest rate, your savings account will be worth {format(doubled_balance, '.2f')} in {format(years_to_double, '.1f')} years")
