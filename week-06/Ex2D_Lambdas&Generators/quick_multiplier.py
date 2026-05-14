doubler = lambda n: n * 2
tripler = lambda n: n * 3

# I am testing with positive number, negative number, and a string.
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))


def multiplier(times):
    # This function returns a lambda, so I can make many multipliers without repeating code.
    return lambda n: n * times

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(quadrupler(2))
print(quintupler(2))
print(sextupler(2))
print(septupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))
