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
