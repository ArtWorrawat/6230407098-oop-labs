class Vehicle:
    __speed = 0
    something = ""

    def __init__(self, name, speed, mileage, *args, **kwargs):
        self.name = name
        self.mileage = mileage
        self.set_speed(speed)

    def set_speed(self, speed):
        self.__speed = speed

    def __str__(self):
        return f"Name: {self.name} speed: {self.__speed} mileage: {self.mileage} {self.something}"


class Car(Vehicle):
    def __init__(self, name, speed, mileage, door):
        super(Car, self).__init__(name, speed, mileage)
        self.something = f"num doors: {door}"

class Bus(Vehicle):
    def __init__(self, name, speed, mileage, capacity):
        super(Bus, self).__init__(name, speed, mileage)
        self.something = f"capacity: {capacity}"


if __name__ == '__main__':
    car = Car("Toyota Vios", 90, 150000, 4)
    bus = Bus("School Volvo", 12, 200000, 100)
    print(car)
    print(bus)
    bus.set_speed(3)
    print(bus)
