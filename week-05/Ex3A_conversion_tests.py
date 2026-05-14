# Description: This script tests various numeric
# conversion techniques
# Author: Mohamed Mouatakid

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print("Original variables:")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print("\nConversion tests:")

# Variable a
# a_int = int(a)  # ValueError: string is a decimal, not a whole number
a_float = float(a)  # Works
a_float_then_int = int(float(a))  # Works
a_slice = a[1:6]  # Gets 101.1
a_slice_float = float(a_slice)

print("a_float:", a_float, type(a_float))
print("a_float_then_int:", a_float_then_int, type(a_float_then_int))
print("a_slice:", a_slice, type(a_slice))
print("a_slice_float:", a_slice_float, type(a_slice_float))
print("a stripped:", a.strip())

# Variable b
b_int = int(b)  # Works
b_float = float(b)  # Works
b_slice = b[0:2]
b_slice_int = int(b_slice)

print("b_int:", b_int, type(b_int))
print("b_float:", b_float, type(b_float))
print("b_slice:", b_slice, type(b_slice))
print("b_slice_int:", b_slice_int, type(b_slice_int))

# Variable c
# c_int = int(c)  # ValueError: string contains letters
# c_float = float(c)  # ValueError: string contains letters
c_slice = c[0:3]
c_slice_int = int(c_slice)

print("c_slice:", c_slice, type(c_slice))
print("c_slice_int:", c_slice_int, type(c_slice_int))

# Variable d
# d_int = int(d)  # ValueError: string contains letters
# d_float = float(d)  # ValueError: string contains letters
d_slice = d[7:8]
d_slice_int = int(d_slice)

print("d_slice:", d_slice, type(d_slice))
print("d_slice_int:", d_slice_int, type(d_slice_int))
print("d stripped:", d.strip())
