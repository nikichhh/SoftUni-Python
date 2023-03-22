weight = float(input())
type = input()
kilometers = int(input())

price = 0

if type == "standard":
    if weight < 1:
        price = kilometers * 0.03
    elif weight < 10:
        price = kilometers * 0.05
    elif weight < 40:
        price = kilometers * 0.1
    elif weight < 90:
        price = kilometers * 0.15
    elif weight < 150:
        price = kilometers * 0.2
elif type == "express":
    if weight < 1:
        price = kilometers * 0.03 + (0.024 * weight * kilometers)
    elif weight < 10:
        price = kilometers * 0.05 + (0.02 * weight * kilometers)
    elif weight < 40:
        price = kilometers * 0.1 + (0.005 * weight * kilometers)
    elif weight < 90:
        price = kilometers * 0.15 + (0.003 * weight * kilometers)
    elif weight < 150:
        price = kilometers * 0.2 + (0.002 * weight * kilometers)

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")