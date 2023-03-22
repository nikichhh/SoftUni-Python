w = int(input())
l = int(input())
h = int(input())

cubics = w*h*l

putting = input()
baggage = 0

while putting != "Done":
    baggage = int(putting)
    if baggage > cubics:
        print(f"No more free space! You need {abs(baggage-cubics)} Cubic meters more.")
        exit()

    cubics -= baggage
    putting = input()

if cubics > 0:
    print(f"{cubics} Cubic meters left.")