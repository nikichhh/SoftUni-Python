volume = int(input())
p1 = int(input())
p2 = int(input())
hour = float(input())

p1_1 = p1*hour
p2_2 = p2*hour
p3 = p1_1+p2_2

if volume>=p3:
    print(f"The pool is {(p3 / volume) * 100}% full. Pipe 1: {(p1_1 / p3) * 100}%. Pipe 2: {(p2_2 / p3) * 100}%.")
else:
    print(f"For {hour} hours the pool overflows with {p3-volume} liters.")