# Remove the duplicates from list
arr = [1, 2, 2, 3, 4, 3, 5]

new_list = []

for i in arr:
    if i not in new_list:
        new_list.append(i)

print(new_list)