# LearnPython homework for week two. Ex 5 (p. 1, 2). 

# p. 1
# Перепишите функцию hello_user() из задания про while, 
# чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
# и завершала работу при помощи оператора break

def hello_user():
    try:
        while True:
            if input('Как дела?\n') == 'Хорошо':
                break
    except KeyboardInterrupt:
        print('\nПока')

hello_user()

# p. 2
# Перепишите функцию discounted(price, discount, max_discount=20) 
# из урока про функции так, чтобы она перехватывала исключения, 
# когда переданы некорректные аргументы.
# Первые два нужно приводить к вещественному числу при помощи float(), 
# а третий - к целому при помощи int() и перехватывать исключения ValueError и TypeError, 
# если приведение типов не сработало.

def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount) 

    except (ValueError, TypeError):
        print('Введены некорректные аргументы (введите числа)')
        return

    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

discounted('haha', 10, 30)

