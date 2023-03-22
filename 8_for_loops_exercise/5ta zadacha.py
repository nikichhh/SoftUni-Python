n = int(input())
salary = int(input())

for i in range (1,n+1):
    website = input()
    if website == "Facebook":
        salary-=150
    elif website == "Instagram":
        salary-=100
    elif website == "Reddit":
        salary-=50

if salary>0:
    print(salary)
else:
    print(f"You have lost your salary.")