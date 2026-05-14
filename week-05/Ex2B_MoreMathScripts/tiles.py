# Description: Calculate how many boxes of tiles are needed
# Author: Mohamed Mouatakid

import math

length = 12
width = 10
tiles_per_box = 12

room_area = length * width
extra_tiles = room_area * 1.10

boxes_needed = math.ceil(extra_tiles / tiles_per_box)

print(f"The room area is {room_area} square feet.")
print(f"With 10% extra, you need {extra_tiles} tiles.")
print(f"You need to buy {boxes_needed} boxes of tiles.")
