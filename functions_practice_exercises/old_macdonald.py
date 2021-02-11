# Function capitalizes first and fourth symbols in string and return it

def old_macdonald(s):
    res = ''
    if len(s) >= 4:
        for i in range(len(s)):
            if i == 0 or i == 3:
                res += s[i].upper()
            else:
                res += s[i]
    else:
        print("String is too short :(")
        res = s
    return res


r = old_macdonald("macdonald")
print(r)
print()

r = old_macdonald("smith")
print(r)
print()

r = old_macdonald("pop")
print(r)