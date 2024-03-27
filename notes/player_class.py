from human_class import Human
class Player(Human):
    male = True

    def __init__(self, name, surname, club, number):
        super().__init__(name, surname)
        self.club = club
        self.number = number
    
    def kick(self, numb):
        print(f"{self.surname} kicks the ball {numb} times")
        return self

    def breathe(self):
        print(f"{self.surname} breathes")
        return self