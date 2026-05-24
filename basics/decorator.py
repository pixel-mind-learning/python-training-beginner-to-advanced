# decorator takes the function as a parameter and return the function


def log_deco(func):
    # inner fucntion
    def wrap(*args):
        print("values ", args)
        result = func(*args)
        print("Result ", result)
        return result

    return wrap


def greater_first(func):
    # inner fucntion
    def wrap(a, b):
        if a < b:
            a, b = b, a
            return func(a, b)

    return wrap


@log_deco
@greater_first
def divide(a, b):
    return a / b


@log_deco
@greater_first
def sub(a, b):
    return a - b


@log_deco
def add(a, b):
    return a + b


result1 = divide(8, 20)
print(result1)

result2 = sub(2, 4)
print(result2)

# result3 = add(5,7,6)
# print(result3)
