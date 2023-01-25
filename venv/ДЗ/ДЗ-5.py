def fn1():
    a = 2
    b = 4
    c = 6

    def fn2():
       a = 8
       b = 6
       c = 6
       print(a,b,c)

print((lambda x, y: x**2 + y**2)(2, 5))
