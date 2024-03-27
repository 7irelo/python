try:
    with open("file.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")

print("File closed: "+str(file.closed))