print('Hello world!')


message = 'Hello world!'
print(message)

# "Hello world" prints twice because my code has two print statements

# Displaying dollars and cents 

dollars = 3
cents = 0.50

print (dollars + cents)

# I notice that the result shows 3.5 instead of 3.50 because Python does not show the extra zero after the decimal.

cents = cents + 0.25
print(dollars + cents)

# The new result is 3.75 because cents changed from 0.50 to 0.75.

d_str = '3 dollars'
c_str = '50 cents'

print(d_str + " " + c_str)