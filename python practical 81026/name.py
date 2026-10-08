# Replace all the vowels in your name by z:
name = input("Enter your Name:")
result =""
for char in name:
    if char in "aeiouAEIOU":
        result = result+"z"
    else:
        result =result+char  
print(result)       
