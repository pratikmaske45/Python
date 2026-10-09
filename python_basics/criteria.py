age = int(input("Enter your age: "))
student = (input("Are you a student?, please enter yes or no: "))
print("you are eligible for discount:", age <= 21 and student == "yes")