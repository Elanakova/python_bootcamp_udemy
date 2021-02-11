# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find_double_three(l):
    for i in range(len(l) - 1):
        if l[i] == 3 and l[i + 1] == 3:
            return True
    return False


r = find_double_three([1, 2, 3, 3])
print(str(r) + "\n")

r = find_double_three([1, 1, 1])
print(str(r) + "\n")

r = find_double_three([3, 1, 3, 5, 3])
print(str(r) + "\n")