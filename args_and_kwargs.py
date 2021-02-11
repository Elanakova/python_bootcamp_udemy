def use_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like to have {} {}".format(args[0], kwargs['food']))

use_args_and_kwargs(5, 6, 7, fruit="banana", food="korvapuusti", animal="cat")