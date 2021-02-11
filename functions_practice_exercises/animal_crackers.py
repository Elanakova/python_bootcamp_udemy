# Function takes a two-word string and returns True, if both words begins with same letter

def animal_crackers(s):
    l = s.split(" ")

    if len(l) != 2:
        print("String should contain two words!")
        return s
    else:
        return l[0][0].lower() == l[1][0].lower()


r = animal_crackers("lush llama")
print(r)
r = animal_crackers("Crazy kangaroo")
print(r)
r = animal_crackers("Cute cat")
print(r)
r = animal_crackers("Big fluffy bear")
print(r)
