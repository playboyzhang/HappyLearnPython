# class Person():
#     # name = "aaa"
#     name = []
#
#
# p1 = Person()
# p2 = Person()
# # p1.name = "bbb"
# p1.name.append(5)
# print(p1.name)
# print(p2.name)
# print(Person.name)

# class MyClass():
#     def __int__(self):
#         self.__superprivate = "Hello"
#         self._semiprivate = ",world!"
#
#
#
# mc = MyClass()
# print(mc._semiprivate)
# print (mc.__dict__)



# def print_everything(*args):
#     for count,thing in enumerate(args):
#         print('{0}, {1}'.format(count,thing))
#
# print_everything('apple','banana','cabbage')


# def table_things(**kwargs):
#     for name,value in kwargs.items():
#         print('{0} = {1} '.format(name,value))
#
# table_things(apple = 'fruit' ,cabbage = 'vegetable')
#
# cabbage = vegetable
# apple = fruit




# def print_three_things(a, b, c):
#     print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
#
# mylist = ['aardvark', 'baboon', 'cat']
#
# print_three_things(*mylist)



# class Singleton(object):
#     def __new__(cls,*args,**kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton,cls)
#             cls._instance = orig.__new__(cls, *args,**kw)
#         return cls._instance
#
#
# class MyClass(Singleton):
#     a = 1


# def singleton(cls,*args,**kw):
#     isinstance = {}
#     def getinstance():
#         if cls not in isinstance:
#             isinstance[cls] = cls(*args,**kw)
#         return getinstance
#
# @singleton
# class MyClass:

fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)

print(fib(10))