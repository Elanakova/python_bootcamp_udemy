# Write a function that checks whether a number is in a given range (inclusive of high and low)

def is_in_range(n, low, high):
    return n >= low and n <= high


r = is_in_range(3, 1, 5)
print(str(r))

r = is_in_range(3, 5, 8)
print(str(r))


def is_in_range_str(n, low, high):
    if low <= n <= high:
        return "{} is in range between {} and {}".format(n, low, high)
    else:
        return "{} is NOT in range between {} and {}".format(n, low, high)


r = is_in_range_str(3, 1, 5)
print(r)
r = is_in_range_str(3, 5, 8)
print(r)