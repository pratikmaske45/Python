num = int(input("enter a number:"))
n=0
while num>0:
    num=num//10
    n+=1
print("number of digits:", n)
