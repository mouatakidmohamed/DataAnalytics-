# Description: Display the smallest and largest of three numbers
# Author: Mohamed Mouatakid

a = 45
b = 12
c = 99

smallest = a
largest = a

if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

if b > largest:
    largest = b
if c > largest:
    largest = c

print(f"The smallest number is {smallest}.")
print(f"The largest number is {largest}.")
