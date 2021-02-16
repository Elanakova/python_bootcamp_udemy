# Create a generator that yields "n" random numbers between a low and high number (that are inputs).

import random


def random_gen(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


print(list(random_gen(1, 10, 7)))