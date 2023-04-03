
import csv
#
# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter = ";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы:{', '.join(row)}")
#         else:
#             print(f"\t {row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#
#     print(f"Всего в файле {count} строки")
#
# import csv
#
# with open("data_1.csv") as f:
#     file_reader = csv.reader(f, delimiter = ";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"\t {', '.join(row)}")
#         else:
#             print(f"\t {row[0]} , {row[1]} , {row[2]} , {row[3]}")

with open("data.csv") as f:
    fn = ['Имя','Профессия','Год рождения']
    file_reader = csv.DictReader(f, delimiter = ";",fiel)
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы")


with open('student.csv','w') as f:
    writer = scv.writer(f, delimiter=";",lineterminator="\r")
    writer.writerow(["Имя","Класс","Возраст"])
    writer.writerow(["Женя", "9", "15"])
    writer.writerow(["Саша", "9", "15"])
    writer.writerow(["Маша", "9", "15"])
print("Hello \rWorld")

data = [[hostname,vendor,model,location]
[sw1,Cisco,3750,London]
[sw2,Cisco,3850,Liverpool]
[sw3,Cisco,3650,Liverpool]
[sw4,Cisco,3650,London]]

with open ('sw_data.csv,'w) as f:
