
name = input("Enter student name: ")

marks = []

for i in range(1, 4):
    mark = int(input("Enter subject marks: "))
    marks.append(mark)

total = sum(marks)
average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
