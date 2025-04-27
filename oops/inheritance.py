from datetime import datetime
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def  start_engine(self):
        print("Engine started")
        print(datetime.now())

class Car(Vehicle):
    def open_roof(self):
        print("Sun Roof opened")




car = Car("Toyota")
car.start_engine()  # Output: Car Engine started
car.open_roof()  # Output: Sun Roof opened