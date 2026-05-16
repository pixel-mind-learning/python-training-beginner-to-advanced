# default argumaents
def add(a=0, b=0):
    print(a + b)


add(1, 2)  # Output: 3


# variable length arguments
def add(a, *b):
    sum = a
    for i in b:
        sum += i
    return sum


result = add(5, 6, 3, 8, 9)

print(result)


# keyword arguments
def add(name, age):
    print("name: ", name)
    print("age: ", age)


add("navin", age=30)


# keyword length arguments
def add(name, **kwrlargs):
    print("name: ", name)
    for k, v in kwrlargs.items():
        print(k, " : ", v)


add(name="navin", name1="maleesha", age=30, tech="python")
