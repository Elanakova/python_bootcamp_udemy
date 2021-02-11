# Handle the exception thrown by the code below by using try and except blocks.

for i in [1,'b','c']:
    try:
        print(i**2)
    except TypeError:
        print("This is not a number!")