# Given a string, return a string where for every character in the original there are three characters

def paper_doll(s):
    res = ''
    for sym in s:
        res += sym*3
    return res


r = paper_doll("Hello")
print(r + "\n")

r = paper_doll("Mississippi")
print(r)