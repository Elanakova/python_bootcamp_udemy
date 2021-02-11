# Write a function that returns a lesser of two numbers, if both numbers are even.
# Otherwise return the greater one
# Input: 2, 4, output: 2
# Input: 2, 3, output: 3

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


r = lesser_of_two_evens(2, 4)
print(r)

r = lesser_of_two_evens(3, 6)
print(r)


