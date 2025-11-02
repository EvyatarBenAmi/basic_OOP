class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_car_info(self):
        return f"make: {self.make}, model: {self.model}, year: {self.year}."
    
new_car = Car("Toyota","RAV4","2025")
# print(new_car.make)
# print(new_car.model)
# print(new_car.year)
# print(new_car.get_car_info())
# new_car.color = "red"
# print(new_car.color)
# del new_car.color
# print(new_car.color)
