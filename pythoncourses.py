class Dog:
   def __init__(self, name, age):
       self.name = name
       self.age = age
       print(name)
   def bark():
        print("bark")
   def add_one(self, x):
        return x + 1
   def get_name(self):
        return self.name
   def get_age(self):
        return self.age
   def set_age(self, age):
        self.age = age



class Student:
   def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
   def __init__(self, name, max_students):
         self.name = name
         self.max_students = max_students
         self.students = []
         #self.is_active = False

   def add_students(self, student):
         if len(self.students)< self.max_students:
             self.students.append(student)
             return True
         return False

   def get_averagge_grade():
       value = 0
       for student in self.students:
         value += student.get_grade()


      return value/len(self.students)



class Cat(Pet):
   def __init__(self, name, age):
        self.name= name
        self.age = age
   def speak(self):
        print("Meaow")



class Dog:
   def __init__(self, name, age):
        self.name = name
        self.age = age
   def speak(self):
        print("Bark")




class Pet:
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


p = Pet("Time", 19)
p.show()
c = Cat("Bill", 34)
c.show()
d = Dog("Jill", 25)
d.speak()



s1 = Student("Time", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)


course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)

#class Dog assign the d variable instatiate by creating a new instance class Dog
d = Dog("George", 34)
print(d.name)
print(d.age)
d.set_age(43)
print(d.get_name())
print(d.get_age())
print(d.get_age())

print(type(d))
#d.bark()
print(type(d))
d.add_one(5)
print(type(d))


d2 = Dog("Tim", 12)
print(d2.name)
print(d2.get_name())
print(d2.get_age())

dog1_name = "Time"
dog1_age = 34


dogs = ["Time", "Bill"]
dogs_age = [32, 14]

