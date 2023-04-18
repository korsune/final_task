from prime_numbers import is_number_prime

if __name__ == '__main__':
    while True:
        print("1. Is number prime")
        print("0. Exit")
        cmd = input("Choose item: ")

        if cmd == "1":
            print("Enter a number from 0 to 1000: ")
            inp = int(input())
            if inp < 0 or inp > 1000:
                print("Number is not in diapason")
            else:
                if is_number_prime(inp):
                    print ("Number is prime")
                else:
                    print ("Number is not prime")
        elif cmd == "0":
            break
        else:
            print("You put wrong value")

