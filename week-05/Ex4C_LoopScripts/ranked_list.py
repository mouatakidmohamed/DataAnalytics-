# Description: Use enumerate to print a ranked list
# Author: Mohamed Mouatakid

skills = ["Python", "SQL", "Excel", "Data visualization", "Public speaking"]

for index, skill in enumerate(skills, start=1):
    if index == 1:
        print(f"{index}. {skill} <- top pick!")
    else:
        print(f"{index}. {skill}")

print("\nReverse order:")
for index, skill in enumerate(reversed(skills), start=1):
    print(f"{index}. {skill}")
