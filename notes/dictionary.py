rappers = {"Detroit":"Eminem", "New York":"Nas", "Chicago":"Kanye"}

#print(rappers["Detroit"])
#print(rappers.get("Detroit"))
#print(rappers.keys(), rappers.values())
#print(rappers.items())
rappers.update({"Durban":"Nasty C"})
rappers.update({"New York":"Jay-Z"})

print(rappers.get("Cape Town"))
rappers.update({"Cape Town":"Youngsta CPT"})
print(rappers.keys())
print("--------------------")

for x, y in rappers.items():
    print(x, y)