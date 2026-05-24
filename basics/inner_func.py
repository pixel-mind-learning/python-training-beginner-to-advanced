# Don't use production applications heavily
# helps with decorators

def outer():
    print("outer func")

    def inner(num):
        print("inner func", num)
    
    return inner


inner_res = outer()
inner_res(10)
