names = ["Eric", "Tirelo", "Ncube"]

numbers = [5, 3, 4, 2, 0, 1]
print("Second name: "+names[1])
print(names)
numbers.sort()
names.append("Sibusiso")
names.remove("Tirelo")
names.pop()
names.insert(1, "Ricky")
print(names)
print(numbers)
names.sort()
for name in names:
    print(name)