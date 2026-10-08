student={
101:{"name":"aditi","scores":[78,85,90]},
102:{"name":"rahul","scores":[45,60,50]},
103:{"name":"karan","scores":[56,35,79]},
104:{"name":"mahesh","scores":[78,98,74]}
}

for sid, details in student.items():
    avg=sum(details["scores"])/len(details["scores"])
    details["average"]=avg
    details["passed"]=avg>=50
    

#print name of student who passed
print("student who passed:")
for sid,details in student.items():
    if details["passed"]:
        print(details["name"])

    