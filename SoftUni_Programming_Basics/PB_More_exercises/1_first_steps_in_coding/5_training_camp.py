from math import floor

width = float(input())
height = float(input())

buro_na_red = (height * 100 - 100) / 70
broi_red = width * 100 / 120

print(f"{floor(buro_na_red) * floor(broi_red) - 3}")