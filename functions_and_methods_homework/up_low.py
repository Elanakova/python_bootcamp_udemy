# Write a Python function that accepts a string and calculates the number of upper case letters
# and lower case letters

def up_low(s):
    upper_count = 0
    lower_count = 0
    for sym in s:
        if sym.isalpha() and sym.isupper():
            upper_count += 1
        else:
            if sym.isalpha and sym.islower():
                lower_count += 1

    print("Original string: {}".format(s))
    print("No. of uppercase characters: {}".format(upper_count))
    print("No. of lowercase characters: {}".format(lower_count))


up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
up_low("Goodbye!")