# LearnPython homework for week two. Ex 3 (p. 1, 2, 3). 

# Цикл (p.1)
print('Цикл (p.1)')
# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.

ten_ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in ten_ints:
    print(i+1)

# Цикл (p.2)
print('\nЦикл (p.2)')
# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.

for l in 'string':
    print(l)

# Оценки (p.3)
print('\nОценки (p.3)')
# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

school_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]}, 
    {'school_class': '4b', 'scores': [2,3,3,5,4]}, 
    {'school_class': '4c', 'scores': [4,5,4,5,5]},
    {'school_class': '4d', 'scores': [4,4,5,3,3]},
]

school_mean_score = 0

for school_class in school_scores:
    class_mean_score = sum(school_class["scores"])/len(school_class["scores"])
    school_mean_score += class_mean_score
    print(f'Средняя оценка в классе {school_class["school_class"]}: {class_mean_score}')

school_mean_score /= len(school_scores)
print(f'Средняя оценка по школе: {round(school_mean_score, 2)}')




