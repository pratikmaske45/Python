# Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.

file = open(r"Class_assignment_13_-10-26/sample.txt", "r")
lines = file.readlines()
file.close()

print("Total number of lines:", len(lines))

if len(lines) >= 2:
    print("2nd line:", lines[1])

if len(lines) >= 4:
    print("4th line:", lines[3])