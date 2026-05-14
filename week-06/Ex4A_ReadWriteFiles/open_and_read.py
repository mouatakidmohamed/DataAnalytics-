f = open('about_me.txt', 'r')

# First I practiced reading the full file.
# print(f.read())

# Then I practiced reading 50 characters at a time. The second read continues from where the first read stopped.
# print(f.read(50))
# print(f.read(50))

# Then I practiced readline. Each readline continues from the current file position.
# print(f.readline(10))
# print(f.readline())
# for i in range(1, 5):
#     print(f.readline())

# Then I practiced readlines. It returns a list of lines.
# print(f.readlines(1))
# print(f.readlines(1))
# print(f.readlines(10))
# print(f.readlines(100))
# print(f.readlines(-1))

f.seek(0)
first_50 = f.read(50)
next_four_lines = []
for i in range(4):
    next_four_lines.append(f.readline())
next_100 = f.readlines(100)

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")

f.close()
