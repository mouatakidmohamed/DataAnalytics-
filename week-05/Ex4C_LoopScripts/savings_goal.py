# Description: Practice using a while loop with a savings goal
# Author: Mohamed Mouatakid

bank_balance = 100
savings_goal = 500
weekly_savings = 75
treat_cost = 15
treated_myself = False

while bank_balance < savings_goal:
    bank_balance = bank_balance + weekly_savings

    if bank_balance >= savings_goal * 0.75 and not treated_myself:
        bank_balance = bank_balance - treat_cost
        treated_myself = True
        print(f"So close! After treating myself, my balance is up to {bank_balance}.")
    elif bank_balance > savings_goal / 2:
        print(f"Almost there! This week my balance is up to {bank_balance}.")
    else:
        print(f"This week my balance increased to {bank_balance}.")

print(f"Goal met! My current balance is {bank_balance}.")
