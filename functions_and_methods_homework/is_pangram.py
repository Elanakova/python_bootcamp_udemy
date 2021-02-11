# Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)
# Pangrams are words or sentences containing every letter of the alphabet at least once.

import string


def is_pangram(s):
    alphabet_set = set(list(string.ascii_lowercase))
    string_set = set(list(s.replace(" ", "").lower()))
    return alphabet_set.issubset(string_set) and string_set.issubset(alphabet_set)


r = is_pangram("The quick brown fox jumps over the lazy dog")
print(str(r))
r = is_pangram("tralalala")
print(str(r))