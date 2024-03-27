human = ("Messi", 10, "Barcelona")

print(human.count(10)) #count returns the number of times var appears in the tuple
print(human.index("Barcelona")) #returns the index of the var

if "Messi" in human: #checks for the str in the tuple
    print("The GOAT")