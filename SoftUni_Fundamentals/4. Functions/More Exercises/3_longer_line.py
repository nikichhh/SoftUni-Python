import math


def get_distance(_x1, _y1, _x2, _y2):
    return (_x2-_x1)**2 + (_y2-_y1)**2


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))
x3 = math.floor(float(input()))
y3 = math.floor(float(input()))
x4 = math.floor(float(input()))
y4 = math.floor(float(input()))

dist1 = get_distance(x1, y1, 0, 0)
dist2 = get_distance(x2, y2, 0, 0)
dist3 = get_distance(x3, y3, 0, 0)
dist4 = get_distance(x4, y4, 0, 0)

line_1 = dist1 + dist2
line_2 = dist3 + dist4

if line_1 >= line_2:
    if dist1 <= dist2:
        print(f'({x1}, {y1})({x2}, {y2})')
    else:
        print(f'({x2}, {y2})({x1}, {y1})')
if line_1 < line_2:
    if dist3 <= dist4:
        print(f'({x3}, {y3})({x4}, {y4})')
    else:
        print(f'({x4}, {y4})({x3}, {y3})')