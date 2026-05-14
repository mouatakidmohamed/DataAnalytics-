# Description: Calculate weekly gross pay, tax withholding, and net pay
# Author: Mohamed Mouatakid

pay_rate = 17.30
hours_worked = 45
filing_status = "single"

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    weekly_gross_pay = regular_pay + overtime_pay
else:
    weekly_gross_pay = hours_worked * pay_rate

annual_gross_income = weekly_gross_pay * 52

if filing_status == "single":
    if annual_gross_income < 12000:
        tax_rate = 0.05
    elif annual_gross_income < 25000:
        tax_rate = 0.10
    elif annual_gross_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == "joint":
    if annual_gross_income < 12000:
        tax_rate = 0.00
    elif annual_gross_income < 25000:
        tax_rate = 0.05
    elif annual_gross_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
else:
    tax_rate = 0.20

tax_withholding = weekly_gross_pay * tax_rate
net_pay = weekly_gross_pay - tax_withholding

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${format(pay_rate, '.2f')} per hour, your gross weekly pay is ${format(weekly_gross_pay, '.2f')}")
print(f"Your filing status is {filing_status}")
print(f"Your estimated annual gross income is ${format(annual_gross_income, '.2f')}")
print(f"Your tax withholding for the week is ${format(tax_withholding, '.2f')}")
print(f"Your net pay is ${format(net_pay, '.2f')}")
