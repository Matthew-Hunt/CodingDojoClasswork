class Car:

    all_cars = []

    def __init__(self, model, type):
        # Attributes
        self.model = model
        self.type = type
        self.year = 2023
        self.fuel = 100
        Car.all_cars.append(self)
        pass


    # Method
    def drive(self):
        self.fuel -= 20
        if self.fuel <= 0:
            print("out of gas")
            self.fuel = 0
        return self

    # Method
    def refill(self):
        self.fuel = 100
        return self

    # Method
    def car_specs(self):
        print(f"Car Make is a {self.model}, it's model is a {self.type} and it's year is a {self.year}")

    @classmethod
    def available_cars(cls):
        for car in cls.all_cars:
            print(f"Make: {car.model}, Model: {car.type}, Year: {car.year}")


car_one = Car("Ford", "Mustang")

car_two = Car("Mercedes", "GWagon")

car_three = Car("Volkswagon", "Beetle")

#car_one.drive().drive().drive().drive().drive().drive().drive().drive()
#print(car_one.fuel)

#car_one.refill()
#print(car_one.fuel)

#car_one.car_specs()

Car.available_cars()