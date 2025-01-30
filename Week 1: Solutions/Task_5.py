class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price


class Car(Vehicle):
    def __init__(self, make, model, year, price, num_doors):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors

    def __str__(self):
        return (f"{self.year} {self.make} {self.model} - ${self.price} (Car, {self.num_doors} doors)")
    # 2023 Toyota Camry - $24000 (Car, 4 doors)

class Truck(Vehicle):
    def __init__(self, make, model, year, price, payload_capacity):
        super().__init__(make, model, year, price)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return (f"{self.year} {self.make} {self.model} - ${self.price} (Truck, Payload Capacity: {self.payload_capacity} kg)")


car1 = Car("Toyota", "Camry", "2023", 24000,4)
car2 = Car("Honda", "Civic", "2021", 22000,4)
truck1 = Truck("Ford", "Focus", "2021", 35000,1000)

inventory = [car1, car2, truck1]

total_value = 0

for vehicle in inventory:
    print(vehicle.__str__())
    total_value += vehicle.price

print(f"Total value: ${total_value}")