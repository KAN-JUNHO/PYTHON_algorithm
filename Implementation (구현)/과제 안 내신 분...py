student = [i for i in range(1,31)]
for i in range(28):
    a=int(input())
    if a in student:
        student.remove(a)
print(min(student))
print(max(student))