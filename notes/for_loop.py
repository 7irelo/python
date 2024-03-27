import time
#for doc in range(5):
    #print(doc + 1)

#for doc in range(2, 9, 2): #11 is exclusive
    #print(doc)

#for doc in "Eric Ncube":
    #print(doc)

#for seconds in range(10, 0, -1):
    #print(seconds)
    #time.sleep(1)
#print("Happy New Year!")

height = 0
while height < 1:
    height = int(input("Height: "))
for i in range(height):
    for k in range(height - i - 1):
        print(' ', end="")
    for j in range(i + 1):
        print('#', end="")
    print('')