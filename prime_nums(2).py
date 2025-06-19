def is_prime(num):
    if num == 0 or num == 1:
        print("not prime.")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("not prime")
                return
        print("prime")
a = int(input("enter num: "))
is_prime(a)
