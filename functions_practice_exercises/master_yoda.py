# Given a sentence, return it with words reversed

def master_yoda(s):
    l = s.split(" ")
    l.reverse()
    return " ".join(l)


r = master_yoda("We are home")
print(r + "\n")

r = master_yoda("I am master Yoda")
print(r)