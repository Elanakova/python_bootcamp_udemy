# Function returns True if sum of arguments is 20 OR one of the arguments is 20

def makes_twenty(a, b):
    if a + b == 20 or a == 20 or b == 20:
        return True
    return False


r = makes_twenty(2, 2)
print(r)
r = makes_twenty(20, 1)
print(r)
r = makes_twenty(1, 20)
print(r)
r = makes_twenty(13, 7)
print(r)
r = makes_twenty(20, 20)
print(r)