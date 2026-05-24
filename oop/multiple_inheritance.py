# Every class in python is a child class of object class
class A(object):
    def f1(self):
        print("f1 works")

    def f2(self):
        print("f2 works")

    def show(self):
        print("in A show")


class B(A):
    def f3(self):
        print("f3 works")

    def f4(self):
        print("f4 works")

    def show(self):
        print("in B show")


# Cannot create a consistent method resolution order (MRO) for bases A, B
# Swap B & A
class C(B, A):
    def f5(self):
        print("f5 works")

    # def show(self):
    #     print("in C show")


obj1 = C()
obj1.f5()
obj1.f1()
obj1.show()
