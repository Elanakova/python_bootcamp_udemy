# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

x = 5
y = 0
try:
    z = x / y
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("All done")