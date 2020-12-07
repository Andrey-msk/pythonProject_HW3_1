'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def mod(*args):
    try:
        poz_arg1 = int(input("Введите первое число "))
        poz_arg2 = int(input("Введите второе число "))
        res = poz_arg1 / poz_arg2
    except ValueError:
        return 'Ошиблись с вводом'
    except ZeroDivisionError:
        return "Вы не можете делить на ноль"
    return res
print(f'result  {mod()}')
