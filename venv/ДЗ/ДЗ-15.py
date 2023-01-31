# S = "i am learning Python.hello,WORLD!"
# print("Исходная строка:" + S)
# result_S = ""
#
# for i in range(0, len(S)):
#     if i != 17:
#         if i != 18:
#             if i != 19:
#                 if i != 20:
#                     if i != 21:
#                       result_S = result_S + S[i]
#                       print("Строка после удаления i-ого элемента:" + result_S)


def qw(S):
 S2 = '.no'
 return S[0:18] + S2 + S[21:33]
print(qw("i am learning Python.hello,WORLD!"))