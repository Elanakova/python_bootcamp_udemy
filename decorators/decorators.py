# lecture code
def new_decorator(original_func):
    def wrap_func():
        print("Line before the original function")
        original_func()
        print("Line after the original function")
    return wrap_func


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()