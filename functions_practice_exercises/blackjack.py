# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
    res = 0

    if a + b + c > 21 and (a == 11 or b == 11 or c == 11):
        res = a + b + c - 10
    else:
        res = a + b + c

    if res > 21:
        return "BUST"

    return res


r = blackjack(9, 9, 9)
print(r)
r = blackjack(5,6,7)
print(r)
r = blackjack(7, 11, 10)
print(r)