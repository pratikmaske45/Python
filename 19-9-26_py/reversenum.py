num = int(input("Enter a number:"))
rev=0
while num>0:
    r=num % 10
    num=num//10
    rev= rev*10+r
    
print("reverse number is:",rev)

