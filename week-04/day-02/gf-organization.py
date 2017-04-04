class Person:
    def __init__(self, name = "John Boe", age = 25, gender = "male"):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my is " + self.name + ", " + str(self.age )+" years old, " + self.gender)

    def get_goal(self, goal):
        print("My goal is: "+ goal)

dangerous_person = Person()
person2 = Person("Jane Doe", 30, "female")

dangerous_person.introduce()
person2.introduce()
person2.get_goal("Live for the moment!")

class Student(Person):
    def __init__(self,  name = "Josh Moe", age = 45, gender = "male", previous_organization = "lollipop factory"):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = 0

    def introduce(self):
        print("Hello, my is " + self.name + ", " + str(self.age )+" years old, " + self.gender + " from " + self.previous_organization +" who skipped " + str(self.skipped_days) +" days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

student = Student()
student2 = Student("Gary Roe", 28, "male", "Gold Resources")
student.introduce()
student2.introduce()
student2.get_goal(" Be a junior software developer.")


class Mentor(Person):
    def __init__(self, name = "Jill Zoe", age = 24, gender = "female", level = "junior"):
        super().__init__(name, age, gender)
        self.level = "intermediate"

    def introduce(self):
        print("Hello, my is " + self.name + ", " + str(self.age )+" years old, " + self.gender + ", " + self.level + " mentor")


mentor = Mentor()
mentor.introduce()
mentor.get_goal(" Educate brilliant junior software developers.")

class Sponsor(Person):
    def __init__(self, name = "Tom Jones", age = 35, gender = "male", company = "RGB"):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = 0

    def introduce(self):
        print("Hello, my is " + self.name + ", " + str(self.age )+" years old, who represents " + self.company + " and hired " + str(self.hired_students) + " students so far.")

    def hire(self):
        self.hired_students += 1

sponsor = Sponsor()
sponsor.introduce()
sponsor.get_goal(" Hire brilliant junior software developers.")

class LagopusClass(Student, Mentor):
    def __init__(self, class_name, students = 0, mentors = 0):
        self.class_name = class_name
        self.students = []
        self.mentors = []

    def add_student(self, student):
        self.students.append(student)

    def add_mentor(self, mentor):
        self.mentors.append(mentor)

    def info(self):
        print("Lagopus " + self.class_name + " class has " + str(len(self.students)) + " students and " + str(len(self.mentors)) + " mentors.")

lagopus = LagopusClass("zodiac")
lagopus.add_student("John")
lagopus.add_student("Ron")
lagopus.add_mentor("John")
lagopus.add_mentor("Ron")
lagopus.info()
