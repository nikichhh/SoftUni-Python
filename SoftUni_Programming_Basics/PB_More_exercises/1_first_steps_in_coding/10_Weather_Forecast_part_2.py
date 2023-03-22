weather = float(input())
if weather >= 5 and weather < 12:
    print("Cold")
elif weather < 15:
    print("Cool")
elif weather <= 20:
    print("Mild")
elif weather < 26:
    print("Warm")
elif weather <= 35:
    print("Hot")
else:
    print("unknown")