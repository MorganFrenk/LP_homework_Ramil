# LearnPython homework for week two. Ex 1. 

# Попросить пользователя ввести возраст при помощи input и положить результат в переменную
# Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
# Вызвать функцию, передав ей возраст пользователя, и положить результат работы функции в переменную
# Вывести содержимое переменной на экран

def should_do(age):

    if int(age) < 6:
        return 'Детский сад'
        
    elif 6 <= int(age) < 19:
        return 'Школа'

    elif 19 <= int(age) < 26:
        return 'Университет'

    elif 26 <= int(age) < 66:
        return 'Завод'

    elif 66 <= int(age) < 150:
        return 'Дом престарелых'
    
    return 'Кто принес компьютер на кладбище?'


while True:

    input_age = input('Введите свой возраст:\n')

    try:
        answer = should_do(input_age)
    except ValueError:
        print('Введите число')
        continue
    break

print(answer)