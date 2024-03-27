import os
import shutil

file = "file.txt"
dir = "folder"
try:
    #os.remove(path)
    #os.rmdir(dir)
    shutil.rmtree(dir)
except FileNotFoundError as e:
    print(e)
    print("File not found")
except OSError as e:
    print(e)
    print("Can't delete that using that function")
else:
    print("File deleted")
