# Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(l):
    for i in range(len(l) - 2):
        if l[i] == 0 and l[i + 1] == 0 and l[i + 2] == 7:
            return True
    return False


r = spy_game([0,0,7])
print(r)
r = spy_game([0,0,7,1,2,4])
print(r)
r = spy_game([1,2,3,0,0,7,1,2])
print(r)
r = spy_game([1,1,0,0,7])
print(r)
r = spy_game([1,1,1,1,1,1,2,0])
print(r)