import os

source = "folder"
destination = "C:\\Users\\Eric\\Desktop\\New folder\\moved"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError as e:
    print(e)
    print("file was not found")
