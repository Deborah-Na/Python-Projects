import pet
class Ninja:
    def __init__(self, first_name, last_name,pet):
        self.first_name= first_name
        self.last_name= last_name
        self.treats="apples"
        self.food="kibbles"
        self.pet=pet

    def walk(self):
        self.pet.play()
        print(f"walking {self.pet.name}")
        return self
    def feed(self):
        self.pet.eat()
        print(f"{self.pet.name} eats {self.treats}!")
        return self
    def bathe(self):
        self.pet.noise()
        return self

    def display(self):
        print(f"{self.pet.name} {self.pet.health} and {self.pet.energy}")

    def milks(self):
        self.pet.scratch()

brownie= pet.Pet("Brownie", "dog", "rolls over", "bark")

spot= pet.Cat("Spot", "cat", "meows", "meow")

deborah= Ninja("Deborah", "Na", brownie)

daniel= Ninja("Daniel", "Hern", spot)



deborah.walk()
deborah.feed()
deborah.bathe()
daniel.milks()












