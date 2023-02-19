# with open('text2.txt','w+') as f:
#     f.write('\n Замена строки в текстовом файле;\n Изменить строку в списке;\n Записать список в файл;')
#     print(f)
#
# with open('text2.txt','r') as text:
#     w = text.read()
#     print(w)
#
# with open('text2.txt','w+') as f:
#     f.write('\n Замена строки в текстовом файле;\n Записать список в файл;\n Изменить строку в списке;')
#     print(f)

# with open('text2.txt','r') as text:
#     w = text.read()
#     print(w)


with open('text2.txt','w+') as f:
    Q = '\n Замена строки в текстовом файле;\n Изменить строку в списке;\n Записать список в файл;'
    reversed = Q[::-1]
    f.write(Q)
    print(reversed)










