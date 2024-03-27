try:
    print("x =", end=" ")
    x = int(input())
    print("y =", end=" ")
    y = int(input())
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError as e:
    print(e)
    print("Enter a number")
except Exception:
    print("Something went wrong :(")
else:
    print(f"answer = {x / y}")
finally:
    print("This will always excecute")