
"""

class Foo(object):
    def __init__(self, func):
        self._func = self.func

    def __call__(self):
        print("class decorator runing")
        self._func()
        print("class decorator ending")

    @Foo
    def bar():
        print("bar")

def test():
    print("test")
a = Foo(test)
a.bar()

"""
from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args, **kvargs):
        print(func.__name__+" was called.")
        return func(*args, **kvargs)
    return with_logging

@logged
def f(x):
    return x**2

print(f(1))
print(f.__name__)
print(f.__call__)
