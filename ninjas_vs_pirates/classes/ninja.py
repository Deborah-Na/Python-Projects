def throw( self , pirate ):
        print(f"{self.name} has threw his kunai!! You can't strike me.")
        pirate.health -= 20
        return self

def special(self,pirate):
        print(f"{self.name} uses special attack, 'Rasengan'!! Die!!!")
        pirate.health -= 50

def eat_vitaminc(self,_):
        if self.health <= 50:
            print("Increases speed by 3!!")
            self.speed += 5 
            return self
class Ninja:

    def __init__( self , name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    attacks = {
        "throw": throw,
        "special": special,
        "eat_vitaminc": eat_vitaminc
    }
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")


    def drink_water(self):
        if self.health < 15:
            self.health += 20
            return self

    def dodging_attack(self):
        if self.health < 20:
            print(f"muahahaha {self.name} dodges the sword attack!")
            self.health += self.health
            return self

    def use_attack(self, attack_name, pirate):
        self.attacks[attack_name](self,pirate)
    
    def list(self):
        print("ninja.show_stats, ninja.attack, ninja.special, ninja.eat_vitaminc, ninja.drink_water, ninja.dodgin_attack")


# class Tiger(Ninja):
#     def __init__(self,name, favorite_toy="dagger"):
#         super().__init__(name)
#         self.favorite_toy= favorite_toy

#     def attack(self, pirate):
#         print(f"{self.name} clawed at your face")
#         pirate.health -= self.strength
#         return self


