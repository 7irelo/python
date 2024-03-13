def main():
    h = get_height()
    for i in range(h):
        print(i + 1)

def get_height():
    while True:
        try:
            n = int(input("input: "))
            if n > 0:
                return n
        except ValueError:
            print("invalid")
main()