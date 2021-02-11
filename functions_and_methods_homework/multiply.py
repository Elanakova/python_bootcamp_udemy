# Write a Python function to multiply all the numbers in a list.

def multiply(lst):
    res = 1
    for n in lst:
        res *= n
    return res


r = multiply([1, 2, 3])
print(str(r))
r = multiply([1, 2, 3, -4])
print(str(r))