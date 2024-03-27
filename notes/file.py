import os

path = "C:\\programming\\python\\notes\\__pycache__"

if os.path.exists(path):
    print("Found")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("Not Found")