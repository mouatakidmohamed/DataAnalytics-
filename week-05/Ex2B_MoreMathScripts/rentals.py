# Description: Calculate van rentals for a tour
# Author: Mohamed Mouatakid

import math

tourists = 38
van_capacity = 15
van_cost = 250

vans_needed = math.ceil(tourists / van_capacity)
total_cost = vans_needed * van_cost
cost_per_person = total_cost / tourists
amount_collected = round(cost_per_person, 2) * tourists

print(f"Number of tourists: {tourists}")
print(f"Vans needed: {vans_needed}")
print(f"Total van cost: ${format(total_cost, '.2f')}")
print(f"Cost per person: ${format(cost_per_person, '.2f')}")
print(f"If everyone pays the rounded amount, you collect ${format(amount_collected, '.2f')}")

# a) The script says to charge about $19.74 per person.
# b) If multiplied by 38, the collected amount is close to $750.
# c) The vans cost $750 total.
# d) There may be leftover money because the per-person amount is rounded to cents.
