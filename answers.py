# Activity 1

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"Battery charged to {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, {self.battery}% battery)"


# Inheritance: GamingPhone extends Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu_power):
        super().__init__(brand, model, storage, battery)
        self.gpu_power = gpu_power

    def play_game(self, game):
        if self.battery > 10:
            print(f"Playing {game} on {self.model} with GPU power {self.gpu_power}...")
            self.battery -= 10
        else:
            print("Battery too low to play games!")


# Example 
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 80)
print(phone1)
phone1.call("08065589988")
phone1.charge(15)

gaming_phone = GamingPhone("Redmi MI", "Redmi Note 13", 256, 50, "Adreno 610")
print(gaming_phone)
gaming_phone.play_game("PUBG Mobile")
gaming_phone.charge(30)

# Activity 2: Polymorphism

class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water.")


# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # Polymorphism in action
