import shutil

shutil.copyfile("file.txt", "copyfile.txt") #src, dst. copies contents
shutil.copy("file.txt", "C:\\Users\\Eric\\Desktop\\New folder\\copy.txt") #destination can be directory
shutil.copy("file.txt", "C:\\Users\\Eric\\Desktop\\New folder\\copy2.txt") #copies metadata