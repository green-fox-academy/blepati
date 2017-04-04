class Person:
    def __init__(self, name = "John Boe", age = 25, gender = "male"):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my is " + self.name + ", " + str(self.age )+" years old, " + self.gender)

    def get_goal(self):
        print("My goal is: Live for the moment!")

dangerous_person = Person()
person2 = Person("Jane Doe", 30, "female")

dangerous_person.introduce()
person2.introduce()

class Student:
    def __init__(self, name = "Josh Moe", age = 45, gender = "male", previous_organization = "lollipop factory"):
        self.name = name
        self.age = age
        self.gender = gender
        self.previous_organization = previous_organization
        self.skipped_days = 0

    def introduce(self):
        print("Hello, my is " + self.name + ", " + str(self.age )+" years old, " + self.gender + " from " + self.previous_organization +" who skipped " + str(self.skipped_days) +" days from the course already.")

    def get_goal(self):
        print("My goal is: Be a junior software developer.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

student = Student()
student2 = Student("Gary Roe", 28, "male", "Gold Resources")
student.introduce()
student2.introduce()

class Mentor:
    def __init__(self, name = "Jill Zoe", age = 24, gender = "female", level = "junior"):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = "intermediate"

    def introduce(self):
        print("Hello, my is " + self.name + ", " + str(self.age )+" years old, " + self.gender + ", " + self.level + " mentor")

    def get_goal(self):
        print("My goal is: Educate brilliant junior software developers.")

mentor = Mentor()
mentor.introduce()

class Sponsor:
    def __init__(self, name = "Tom Jones", age = 35, gender = "male", company = "RGB"):
        self.name = name
        self.age = age
        self.gender = gender
        self.company = company
        self.hired_students = 0

    def introduce(self):
        print("Hello, my is " + self.name + ", " + str(self.age )+" years old, who represents " + self.company + " and hired " + str(self.hired_students) + " students so far.")

    def get_goal(self):
        print("My goal is: Hire brilliant junior software developers.")

    def hire(self):
        self.hired_students += 1

sponsor = Sponsor()
sponsor.introduce()
