from prime_numbers import is_number_prime
from sort import sort

if __name__ == '__main__':
    while True:
        print("1. Is number prime")
        print("2. Sort sequence in ascending order")
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
        elif cmd == "2":
            print("Enter a sequence of numbers, enter * in the end: ")
            inp = input()
            lst = list()
            while inp != "*":
                lst.append(int(inp))
                inp = input()
            print ("Sorted sequence: ", sort(lst))

        elif cmd == "0":
            break
        else:
            print("You put wrong value")

