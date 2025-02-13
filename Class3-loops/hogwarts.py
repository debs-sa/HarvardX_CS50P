##### LISTS #####

students = ["Hermione", "Harry", "Ron"]

print(students[1])


for student in students:
    print(student)


## or ## with length

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i]) 