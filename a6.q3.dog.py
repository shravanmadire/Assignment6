class Dog:
    def __init__(self,name,age,coat_colour):
        self.name = name
        self.age =age
        self.coat_colour = coat_colour
    
    def description(self):
        print(f"Name : {self.name} \nAge : {self.age}")

    def get_info(self):
        print(f"Coat Colour : {self.coat_colour}")

class JackRussellTerrier(Dog):
    def __init__(self,name,age,coat_colour,owner):
        super().__init__(name,age,coat_colour)
        self.owner =owner
    
    def display(self):
        print(f"Owner : {self.owner}")

class Bulldog(Dog):
    def __init__(self,name,age,coat_colour,nickname):
        super().__init__(name,age,coat_colour)
        
        self.nickname = nickname

    def view(self):
        print(f"Nick name : {self.nickname}")


jack_russell_terrier = JackRussellTerrier("Rony",4,"black","Sam")
jack_russell_terrier.description()
jack_russell_terrier.get_info()
jack_russell_terrier.display()

bull_dog = Bulldog("Rony",4,"black","Sam")
bull_dog.description()
bull_dog.get_info()
bull_dog.view()