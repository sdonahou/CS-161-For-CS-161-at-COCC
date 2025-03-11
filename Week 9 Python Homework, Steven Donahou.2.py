#1 Class of two students.
class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print()

student1 = Students("Raj", 16, "11th")
student2 = Students("Joe", 17, "11th")
student1.getinfo()
student2.getinfo()

#2 Child Class and Parent Class for Staff and Teacher.
class Staff:
    def __init__(self, name, department, role, salary):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary
class Teacher(Staff):
    def __init__(self, name, age, department, role, salary):
        super().__init__(name, department, role, salary)
        self.age= age
    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ROle: {self.role}")
        print(f"Department: {self.department}")
        print()
Staff1 = Teacher("Raj", 20, "Science", "Teacher", "60000" )
Teacher1 = Teacher("Joe", 58, "Science", "Teacher", "80000" )

Staff1.getinfo()
Teacher1.getinfo()

#3 Class Square that provides two methods of a square area, perimeter, and length of a side.
class Square:
    def __init__(self, sidelength):
        self.side = sidelength
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return self.side * 4
Square1 = Square(10)
Square2 = Square(20)

print("The area of square1 is: ", Square1.area())
print("The perimeter of square1 is", Square1.perimeter())
print("The area of square2 is: ", Square2.area())
print("The perimeter of square2 is: ", Square2.perimeter())


