import random

x = random.randint(1, 6)
y = random.random() #generates a random number between 0 and 1

myList = ["Rock", "Paper", "Scissors"]
z = random.choice(myList)
print(z)

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "King", "Queen"]
random.shuffle(cards)
print(cards)