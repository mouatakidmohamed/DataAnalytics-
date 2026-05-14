# Description: Calculate net worth
# Author: Mohamed Mouatakid

cash = 1200
savings = 3500
car_value = 8000

credit_card_debt = 650
student_loan = 2500

total_assets = cash + savings + car_value
total_debts = credit_card_debt + student_loan
net_worth = total_assets - total_debts

print(f"Your total assets are {total_assets}")
print(f"Your total debts are {total_debts}")
print(f"Your net worth is {net_worth}")
