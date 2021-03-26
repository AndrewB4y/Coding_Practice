"""
Write a decorator to cache function invocation results.
Store pairs arg:result in a dictionary in an attribute of the function object.
"""


def cache(function):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        if args not in cache_dict.keys():
            cache_dict[args] = function(*args)
        return cache_dict[args]
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))