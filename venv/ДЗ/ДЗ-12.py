# Q = lambda a, b, c: a * b * c
# print (Q(2,5,5))

# players = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Jennifer', 'final': 98}
# ]
#
# # res = sorted(players, key = lambda item: 'name')
# # res = sorted(players, key = lambda item:item['final'], reverse = True)
# res = sorted(players, key=lambda i: i['final'])
#
# print(res)
#
W = lambda a:  3.14*(a**2)
print (W(2))

W = lambda a,b:  (a*b)
print (W(10,13))

W = lambda a,b,c:  0.5*c*(a+b)
print (W(7,5,3))