clip = "\n-----------------------\n"
text = "Line"
with open("file.txt", "a") as file: #r reads, w writes, a appends
    file.write(clip)
    file.write(text)