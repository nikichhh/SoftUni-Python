days = int(input())

rakia_kol = 0
degrees_kol = 0

for _ in range (1, days + 1):
    rakia = float(input())
    degrees = float(input())

    rakia_kol += rakia
    degrees_kol += rakia * degrees

print(f"Liter: {rakia_kol:.2f}\nDegrees: {degrees_kol/rakia_kol:.2f}")
if degrees_kol/rakia_kol < 38:
    print("Not good, you should baking!")
elif degrees_kol/rakia_kol <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")