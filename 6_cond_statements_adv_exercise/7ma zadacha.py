month = input()
days = int(input())

apartment = 0
studio = 0

if month == "May" or month == "October":
    apartment = days*65
    studio = days*50
    if days>7 and days<=14:
        studio-=studio*0.05
    elif days>14:
        studio-=studio*0.3
        apartment-=apartment*0.1
elif month == "June" or month == "September":
    apartment = days*68.7
    studio = days*75.2
    if days>14:
        studio-=studio*0.2
        apartment-=apartment*0.1
else:
    apartment = days*77
    studio = days*76
    if days>14:
        apartment-=apartment*0.1

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")