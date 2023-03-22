x = float(input())
y = float(input())
h = float(input())

area_down = 2 * (x * x + x * y) - 2 * (1.5 * 1.5 + 1.2)
area_up = (x * h) + 2 * (x * y)
green_paint = area_down / 3.4
red_paint = area_up / 4.3

print(f"{green_paint:.2f}\n{red_paint:.2f}")