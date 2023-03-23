def prime_checker(number):
    if number == 1:
        print("It's not a prime number.")
    elif number > 1:
        p = True
        for i in range(2, number):
            if number % i == 0:
                p = False
        if p:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)


