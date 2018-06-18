def log(func):
    def wrapper(*args, **kvargs):
        print("start ", func.__name__)
        return func(*args, **kvargs)
    return wrapper

@log
def func_a(): pass

@log 
def func_b():pass


func_a()
func_b()
