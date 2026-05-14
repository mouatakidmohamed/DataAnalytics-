# Description: Calculate distance between two coordinates
# Author: Mohamed Mouatakid

import math

x1 = 2
y1 = 3
x2 = 8
y2 = 11

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"The distance between the two coordinates is {format(distance, '.2f')}")
