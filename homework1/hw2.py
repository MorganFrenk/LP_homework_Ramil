# LearnPython homework for week two. Ex 2. 

# Сравнение строк
# Написать функцию, которая принимает на вход две строки
# Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
# Если строки одинаковые, вернуть 1
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

def str_compare (str1, str2):

    if not (isinstance(str1, str) and isinstance(str2, str)):
        return 0

    elif str1 == str2:
        return 1

    elif len(str1) > len(str2):
        return 2

    if str2 == 'learn':
        return 3
    

print(str_compare('hello', 2021))
print(str_compare('hello', 'hello'))
print(str_compare('hello', 'world'))
print(str_compare('hello!', 'world'))
print(str_compare('hello', 'learn'))