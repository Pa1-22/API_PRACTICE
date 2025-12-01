class Student:
    school = "nbkr academy"

    def student_data(self):
        print("40 students present")

    def student_marks(self):
        print("student pass the exam")
    # access the class  varaible entire the class
    @classmethod  
    def student_course(cls):
        print(f"student completed course in {cls.school}")

    @staticmethod
    def student_department():
        print("student is in cse")

Student.student_course()
Student.student_department()


class Teacher(Student):
    @classmethod
    def teacher_ddetails(cls):
       print(f"teacher course completed in {cls.school}")
Teacher.teacher_ddetails()