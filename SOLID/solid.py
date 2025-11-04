from abc import ABC, abstractmethod
from math import pi
class Book:
    def __init__(self, titel: str, author: str, content: str):
        self.titel = titel
        self.author = author
        self.content = content

    # def save_to_list(self, filename):
    #     self.filename = filename
    #     self.saving_book = []
    #     self.saving_book.append(self.content)
    #     return self.saving_book


class Save_to_list:
    def __init__(self):
        self.book_list = []
    def save_book_in_list(self, content: Book):
        self.book_list.append(content)  
        return self.book_list

# a =Book("nimlatim", "shalom", "is good book")
# b = Save_to_list()
# print(b.save_book_in_list(a.content))


class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    # def average_grades(self):
    #     return sum(self.grades) / len(self.grades) 

class GradesCalculator:
    def __init__(self):
        pass
    @staticmethod
    def average_grades(grades: Student):
        return sum(grades) / len(grades)
    

# a = Student("ori", [100,90,80,75])
# b = GradesCalculator()
# print(b.average_grades(a.grades))

class Order:
    def __init__(self, items: list[str], total_price: float):
        self.items = items
        self.total_price = total_price

    # def print_invoice(self):
    #     print(f"items: {self.items}. total price: {self.total_price}.")

class InvoicePrinter:
    def __init__(self):
        pass
    @staticmethod
    def print_invoice(tow_parameters:Order):
        print(f"items: {tow_parameters.items}. total price: {tow_parameters.total_price}.")

# a = Order(["milk","chery"],25.3)
# b = InvoicePrinter()
# b.print_invoice(a)

class Shape(ABC):
    @abstractmethod
    def area():
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r 

    def area(self):
        return pi * (self.r ** 2)

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2
    
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h 
    
# a = Rectangle(5,7)
# print(a.w)

class Payment(ABC):

    @abstractmethod
    def pay(amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"payment in credit card: {amount}")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"payment in paypal: {amount}")

# a = CreditCardPayment()
# a.pay(12)
