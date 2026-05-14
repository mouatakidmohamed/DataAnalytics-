# ValueError example
try:
    number = int('abc')
except ValueError:
    print("ValueError: I tried to convert letters into an integer, and Python cannot do that.")
else:
    print(number)
finally:
    print("Let's try another one...")

# NameError example
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like I tried to use a variable that was not defined.")
else:
    print(m)
finally:
    print("Let's try another one...")

# TypeError example
try:
    result = 5 + 'apples'
except TypeError:
    print("TypeError: I tried to add an integer and a string together.")
else:
    print(result)
finally:
    print("Let's try another one...")

# SyntaxError example
try:
    # I use exec because a real SyntaxError would stop the whole script before it can run.
    exec('print("hello"')
except SyntaxError:
    print("SyntaxError: Python found code that is not written with correct syntax.")
else:
    print("No syntax error happened.")
finally:
    print("Let's try another one...")
