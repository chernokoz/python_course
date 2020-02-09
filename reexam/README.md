11111




Реализуйте класс AppendAttribute, который при попытке установить уже существующий аттрибут будет создавать новый атрибут
с уникальным префиксом `id_`, отсчет можно начинать с буквы 'a'.

Например,

class AppendAttribute:
    ...
    
    def foo():
        print("foo")

a = AppendAttribute()
a.foo = lambda x: print("second foo")
a.a_foo() # second foo
a.foo() # foo





22222222



Реализуйте класс «последовательность c фильтрацией», который соответствует некоторой последовательности объектов и имеет 
следующие методы:
• Создать объект на основе произвольного итерируемого.
• Проитерироваться по элементам (__iter__) по элементам (не истощаемое).
• Отфильтровать последовательность с помощью некоторой функции и вернуть новую последовательность, в которой присутствуют  
только элементы, для которых эта функция вернула True.

Будем считать, что в данной задаче основным приоритетом является экономия памяти. Поэтому количество копирований данных 
нужно свести к минимуму (возможно, пожертвовав скоростью работы), а вычисления должны быть ленивыми.





333333333(Metaclasses)


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
