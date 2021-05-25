import csv

# CSV
# Создайте список словарей
# Запишите содержимое списка словарей в файл в формате csv

name_job= [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('jobs.csv', 'w', encoding='utf8', newline='') as file:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(file, fields, delimiter=';')
    writer.writeheader()
    
    for member in name_job:
        writer.writerow(member)