@Version(1.7)
class B:
    def __init__(self, x):
        print("B version 1.7" + str(x))

@Version(1.6)
class A:
    def __init__(self):
        print("A version 1.6")


@Version(1.5)
class A:
    def __init__(self):
        print("A version 1.5")


        
a = A()
a = A(version=1.5)()


class X(A):
    pass


x = X()


class X(A(version=1.6)):
    pass


x = X()

b = B(3)

-------- 
@Version(1.6)
class A():
    def __init__(self):
        self.a = 6


@Version(1.7)
class A():
    def __init__(self):
        self.a = 7


@Version(1.5)
class A():
    def __init__(self):
        self.a = 5


a = A()
print(a.a) # 7

a = A(version=1.6)()
print(a.a) # 6


class B(A): 
    pass


b = B()
print(b.a) # 7


class C(A(version=1.5)):
    pass


c = C()
print(c.a) # 5
