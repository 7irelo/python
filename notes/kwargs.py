def hello(**kwargs):
    #print("hello " + kwargs["first"] + " " + kwargs["second"] + " " + kwargs["last"])
    print("hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(first="Eric", second="Tirelo", last="Ncube")