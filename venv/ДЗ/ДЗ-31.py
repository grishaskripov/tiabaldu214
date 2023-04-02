
# import csv
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
import csv

with open("data_1.csv") as f:
    file_reader = csv.reader(f, delimiter = ";")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"\t {', '.join(row)}")
        else:
            print(f"\t {row[0]} , {row[1]} , {row[2]} , {row[3]}")

