n = int(input())

a = 0
b = 0
c = 0
d = 0
e = 0

for i in range (1,n+1):
    num = int(input())
    if num<200:
        a+=1
    elif num<400:
        b+=1
    elif num<600:
        c+=1
    elif num<800:
        d+=1
    elif num>=800:
        e+=1

percentA = (a/n)*100
percentB = (b/n)*100
percentC = (c/n)*100
percentD = (d/n)*100
percentE = (e/n)*100

print(f"{percentA:.2f}%\n{percentB:.2f}%\n{percentC:.2f}%\n{percentD:.2f}%\n{percentE:.2f}%")