def f_func(n):
    if len(n) == 0:
        return 0
    else:
        QA = f_func(n[1:])

        if n[0] < 0:
            QA += 1
        return QA


w = [-2, 3, 8, -11, -4, 6,-234]
print(f_func(w))
