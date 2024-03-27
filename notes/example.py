def add(*args):
    sum = 0
    stuff = list(args)
    stuff[0] = 5
    for num in stuff:
        sum += num
    return sum

x = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(x)