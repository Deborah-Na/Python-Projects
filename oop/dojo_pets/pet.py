class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=75
        self.energy=25
        self.sound=sound
        
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health +=10
        return self
    def play(self):
        self.health +=5
        return self
    def noise(self):
        print(self.sound) 
        return self

class Cat(Pet):
    def __init__(self, name, type, tricks, sound):
        super().__init__(name, type, tricks, sound)
    
    def scratch(self):
        print(f"{self.name} scratches")
    
    