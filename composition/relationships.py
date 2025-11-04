from abc import ABC, abstractmethod 
class Vehicles:
    def __init__(self, max_speed):
        self.max_speed = max_speed 

    def drive(self):
        print(self.max_speed)
        
class Car(Vehicles):
    pass

class Motorcycle(Vehicles):
    pass


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
     def manager(self):
        print(f"my name: {self.name}. i'm manager. salary: {self.salary}.")

class Developer(Employee):
    def write_code(self):
        print(f"my name: {self.name}. i'm developer. salary: {self.salary}.")


class Shape:
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
