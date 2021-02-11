def skyline(s):
    res = ''
    if s[0].isupper():
        res += s[0].lower()
    else:
        res += s[0].upper()
