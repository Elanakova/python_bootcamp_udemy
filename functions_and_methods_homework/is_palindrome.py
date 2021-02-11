# Write a Python function that checks whether a word or phrase is palindrome or not

def is_palindrome(s):
    return s.lower() == s[::-1].lower()


r = is_palindrome("Abba")
print(str(r))

r = is_palindrome("Aab")
print(str(r))