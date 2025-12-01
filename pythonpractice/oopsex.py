class Students:
    def __init__(self,name,age):
        self.name=input("enter the name of the person:")
        self.age=int("emter the age:" )
    def run(self):

        
       print(f"Students name is {self.name} and age is {self.age}")

    def __init__(self,course):
        self.course=input("enter the course")
    def course_details(self):
        print(f" student course is {self.course}")

stu=Students()
print(stu)
stu.run()
stu.course_details()