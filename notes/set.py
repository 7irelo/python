#unordered, unindexed, no duplicate values
players = {"Messi", "Ronaldo", "Suarez", "Benzema"}
players.add("Eminem")
players.remove("Eminem")
rappers = {"Eminem", "Nas", "Jay-Z", "Andre 3000", "Ronaldo"}
#players.update(rappers)

icons = players.union(rappers)
print("Same: "+str(rappers.intersection(players)))
print("Diffrent: "+str(players.difference(rappers)))


for icon in icons:
    print(icon+", ", end='')