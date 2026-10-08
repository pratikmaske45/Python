# create dictionary with liabrary details:
library = {
    101:{"title":"Python Basics", "author": "John Smith", "price": 450 },
    102:{"title":"Data Structure", "author": "Robert Brown", "price": 600},
    103:{ "title":"Web Developement", "author": "David Lee", "price": 500},
    104: {"title": "Machine Learning", "author": "Alice Johnson", "price": 750},
    105: {"title": "Database Systems", "author": "Mark Wilson", "price": 550}
}


print("Titles of Books:")
for lid, details in library.items():
    print(details["title"])

total = 0

for lid, details in library.items():
    total = total +(details["price"])
    average = total/len(library)
print(average)    

for lid, details in library.items():
    details["available"] = True
    print(details)

print("Books with price higher than 550:")
for lid, details in library.items():
    if details["price"]>550:
        print(details["title"])   