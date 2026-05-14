# Description: Calculate gross pay with overtime
# Author: Mohamed Mouatakid

pay_rate = 17.30
hours_worked = 45

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

print(f"Pay rate: ${format(pay_rate, '.2f')}")
print(f"Hours worked: {hours_worked}")
print(f"Gross pay: ${format(gross_pay, '.2f')}")
