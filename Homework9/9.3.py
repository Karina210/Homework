def my_decorator(func):
    def wrap(n):
       b = [i for i in n if i % 2]
       return func(n)

    return wrap

@my_decorator
def real_func(x):
    print(x)


real_func([1, 2, 3, 4, 5, 6, 7, 8])
