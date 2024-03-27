from abc import ABC, abstractmethod

class Human(ABC):
    
    @abstractmethod
    def breath(self):
        pass

    @abstractmethod
    def kick(self):
        pass
    
class Player(Human):
    
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def breath(self):
        print(f"{self.surname} breathes")
        return self

    def kick(self):
        print(f"{self.surname} kicks the ball")
        return self

#human = Human()

ronaldo = Player("Cristiano", "Ronaldo", 7)
ronaldo.breath().kick()