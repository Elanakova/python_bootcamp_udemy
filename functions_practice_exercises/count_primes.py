#Write a function that returns the number of prime numbers that exist up to and including a given number

def check_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False

    return True


def count_primes(n):
    counter = 0

    for num in range(n):
        if check_prime(num):
            counter += 1
    return counter


r = count_primes(100)
print(r)