class Student:
    def __init__(self,name,department):
        self.name = name
        self.department = department


    def play(self):
        print(f"Student {self.name} and {self.department}")

class Child(student):

    def __init__(self,name,department,course):
        self.course=course

    def course_details(self):
       print(f"Student {self.name} and {self.department} and {self.course} ")

cal=Student("pallavi","cse")=
cal = child("python")

cal.course()