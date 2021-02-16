# Create a generator that generates the squares of numbers up to some number N

def square_gen(n):
    for i in range(n):
        yield i ** 2


print(list(square_gen(10)))