# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def make_unique_list(lst):

    dct = {}

    for n in lst:
        if n in dct:
            dct[n] += 1
        else:
            dct[n] = 0

    return dct.keys()

r = make_unique_list([1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4])
print(*r)

r = make_unique_list([3,7,8,9,13,66])
print(*r)