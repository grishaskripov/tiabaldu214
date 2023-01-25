# Q = int(input("Введите колличество символов:"))
# S = input("Введите тип символа:")
# x = input("Ориентация: горизонтальная-0, вертикальная-1:")
#
# for i in range (Q):
#     if x == 0:
#      print (S, end=" ")
#     else:
#         print(S)

# Q = int(input("Введите ширину 1:"))
# S = int(input("Введите высоту 3:"))
#
# for i in range (S):
#     print ("++++++++++++++++")
#     if i == 2:
#         continue
#     for i in range(Q):
#         print("----------------")


try:
 Q = int(input("Введите число:"))
 W = int(input("Введите число:"))
 E = int(input("Введите число:"))

 if Q > W and Q > E:
    print(Q)
 if W > Q and W > E:
    print(W)
 if E > W and E > Q:
    print(E)
 S = Q + W + E
    print(S)

exceptValueError:
    print ("Нельзя вводить текст")






