from player_class import Player

messi = Player("Lionel", "Messi", "Barcelona", 10)
messi.breathe().kick(10)

ronaldo = Player("Cristiano", "Ronaldo", "Real Madrid", 7)
ronaldo.breathe().kick(7)

riveria = Player("Maile", "Riveria", "AC Milan", 8)
riveria.male = False
print("Players are male: ", Player.male)
print(riveria.surname + " is male: " + str(riveria.male))