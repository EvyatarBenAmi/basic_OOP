from math import pi
# Vehicles
class Vehicel:
    def __init__(self, brand, model):
        self.brand = brand
        self .model = model
    
    def move(self):
        print("The vehicle is moving")

class Car(Vehicel):

    def move(self):
        print("The car drives")

class Plane(Vehicel):

    def move(self):
        print("The plane flies")

# v = Vehicel("toyota", "RAV4")
# print(v.brand)
# print(v.model)
# v.move()

# c = Car("kia","sportath")
# print(c.brand)
# print(c.model)
# c.move()

# p = Plane("scoda", "supreb")
# print(p.brand)
# print(p.model)
# p.move()

# Animals
class Animal:
    def __init__(self):
        pass
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        return "woof"
    
class Cat(Animal):

    def sound(self):
        return "meow"
    
# animal = [Dog(), Cat()]
# for i in animal:
#     print(i.sound())

# Shape Area Calculation
class Shape:
    def __init__(self):
        pass
    def area(self):
        raise Exception ("NotImplementedError")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radus):
        self.radus = radus

    def area(self):
        return pi * (self.radus ** 2)

# s =Shape()
# print(s.area())

# r = Rectangle(4,2)
# print(r.area())

# c = Circle(15)
# print(c.area())

# Employee Payment
class Employee:
    def __init__(self, name, salary: int):
        self.name =name
        self.salary = salary

    def get_total_salary(self):
        return f"salary: {self.salary} ."
    
class AddBonus(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
        self.salary += self.bonus

    def get_total_salary(self):
        return f"bonus: {self.salary} ."
    
class AddOvertime(Employee):
    def __init__(self, name, salary, overtime):
        super().__init__(name, salary)
        self.overtime = overtime
        self.salary += overtime

    def get_total_salary(self):
        return f"overtime: {self.salary} ."


# e =Employee("evyatar", 100)
# print(e.name)
# print(e.get_total_salary())

# b = AddBonus("ori", 200, 10)
# print(b.name)
# print(b.bonus)
# print(b.get_total_salary())

# o = AddOvertime("tamar", 300,20)
# print(o.name)
# print(o.overtime)
# print(o.get_total_salary())