def multiply(a, b):
    return a * b

#x = multiply(4, 5)
#print(x)
#times = multiply
#print(times(8, 5))

def quit(text):
    return text.lower()

def loud(text):
    return text.upper()

def hello(function):
    text = function("hello")
    print(text)

hello(loud)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))
#divisor is called with 2 and returns a fuction
#the fuction is aliased a divide
#divide is called with the value of 10
#10 is divide by 2
