# Description: This script cleans messy string data
# Author: Mohamed Mouatakid

name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

print("Lowercase names:")
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

print("\nTitle case names:")
print(name_1.title())
print(name_2.title())
print(name_3.title())

salary_1_no_dollar = salary_1.replace("$", "")
salary_2_no_dollar = salary_2.replace("$", "")

print("\nSalaries without dollar sign:")
print(salary_1_no_dollar)
print(salary_2_no_dollar)

print(type(salary_1_no_dollar))
print(type(salary_2_no_dollar))

# These values are still strings.
# To perform math, I need to remove the comma and convert them to integers.

salary_1_integer = int(salary_1.replace("$", "").replace(",", ""))

print("\nSalary 1 as an integer:")
print(salary_1_integer)
print(type(salary_1_integer))
