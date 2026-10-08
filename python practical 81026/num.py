# write a program to guess the number use random function
import random 
number = random.randint(1,10)
guess = int(input("Enter the number between 1 to 10:"))

if guess ==number:
    print("You earned 100 points!")
elif guess<number:
    print("Too low!")
else: 
    print("Too high!")        
print("The number was:" , number)    