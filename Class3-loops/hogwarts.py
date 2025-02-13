##### LISTS #####

students = ["Hermione", "Harry", "Ron"]

print(students[1])


for student in students:
    print(student)


## or ## with length

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])




## dict ## dictionary
 
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students)

print(students["Harry"])

for student in students:
     print(student, students[student], sep=", ") # python feature for loops
     
     
     #
############# DICTIONARY #################
# uses {}
# word and definition
#a list just uses []

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},    #absense of a value
]

for student in students:
    print(student["name"])
    print(student["name"], student["house"], student["patronus"], sep=", ")

