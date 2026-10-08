#  Insert a number in a list at 6th position this number
#  must be 1/3rd of number stored at 4th position
numbers = [1,2,3,4,5,6,7,8,9,10]
new_number = numbers[3]/3
numbers.insert(5,new_number)
print(numbers)

