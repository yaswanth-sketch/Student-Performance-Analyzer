name = 'yaswanth'
name_length = len(name)
n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)
valid_count = 0
fail_count = 0
print("Result")

for mark in marks:
    if mark < 0 or mark > 100:
        print(mark, "→ Invalid")
    else :
        valid_count += 1
        if mark >= 90:
            result = "Excellent"
        elif mark >= 75:
            result = "Very Good"
        elif mark >= 60:
            result = "Good"
        elif mark >= 40:
            result = "Average"
        else:
            result = "Fail"
            fail_count += 1
        if name_length % 2 == 0:
            print(mark, "->", result, "(Checked)")
        else:
            print(mark, "->", result)
print("Final Summary")
print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)

