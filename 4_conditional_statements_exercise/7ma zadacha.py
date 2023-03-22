a = float(input())
b = int(input())
c = int(input())
d = int(input())

b1 = b*250
c1 = (b1*0.35)*c
d1 = (b1*0.1)*d

sum = b1+c1+d1

if b>c:
    sum-=sum*0.15

if sum>a:
    print(f"Not enough money! You need {sum-a:.2f} leva more!")
else:
    print(f"You have {a-sum:.2f} leva left!")