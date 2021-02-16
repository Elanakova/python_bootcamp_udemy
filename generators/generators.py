# lecture code

def create_cubes(n):
    for i in range(n):
        yield i ** 3


print(list(create_cubes(6))) # [0, 1, 8, 27, 64, 125]


def gen_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

print(list(gen_fibonacci(10))) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# next method
# define a simple generator
def simple_gen():
    for i in range(5):
        yield i

#create a new instance of simple_gen
g = simple_gen()

# use next() method to get next generated value
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3
print(next(g)) # 4
# print(next(g)) # StopIteration

# iter()
s = "hello"
s_iter = iter(s)
print(next(s_iter)) # h
print(next(s_iter)) # e