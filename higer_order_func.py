from math import sqrt, pow


def square(num):
    return sqrt(num)


def cube(num):
    return pow(num, 3)


def operate(num, operation):
    print(operation(num))


operate(5, cube)
