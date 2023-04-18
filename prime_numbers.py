def is_number_prime(number):
    count = 0
    if number == 0 or number == 1:
        return False
    else:
        for i in range(1, number):
            if number % i == 0:
                count = count + 1
        if count == 2:
            return True
        else:
            return False

