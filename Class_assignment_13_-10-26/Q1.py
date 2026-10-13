# Write a program to read a file and count how many vowels are present in its content.

file = open("Class_assignment_13_-10-26/sample.txt", "r") 
content = file.read() 
file.close()
count = 0 

for ch in content: 
    if ch.lower() in "aeiou":
         count += 1 
print("Total vowels:", count)