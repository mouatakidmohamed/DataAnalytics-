# Description: Calculate federal tax withholding
# Author: Mohamed Mouatakid

monthly_salary = 4000
tax_rate = 0.23

tax_withheld = monthly_salary * tax_rate

print(f"Monthly salary: ${format(monthly_salary, '.2f')}")
print(f"Federal tax withheld: ${format(tax_withheld, '.2f')}")
