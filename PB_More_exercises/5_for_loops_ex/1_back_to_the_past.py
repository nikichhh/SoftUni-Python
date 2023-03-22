import pdb

ivan_year = 18

money = float(input())
year = int(input())

for i in range(1800, year+1):
    if i%2 == 0:
        money-=12000
    else:
        money-=12000
        money-=ivan_year*50
    ivan_year+=1

if money>=0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {-money:.2f} dollars to survive.")