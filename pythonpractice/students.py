from collections import namedtuple

Student=namedtuple('Student',["id","name","score"])

choice=0

students=[]

while choice != -1:
    id=int(input("Enter the student id:"))
    name=input("Enter the student name: ")
    score=int(input("Enter the marks: "))
    choice=int(input("enter the number 0 or -1:"))

    # its give tuple as given values so we have to convert to list
    students.append(Student(id,name,score))
    top=sorted(students,key=lambda x: x.score)[-1:]
print(top)









