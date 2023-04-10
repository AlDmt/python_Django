import math
from os import urandom


go=1
while go !="0":
        
    print("Операции которые выполняет калькулятор: Сложение +  Вычитание -    Умножение *  Деление / " )
    print('Возведение в степень ^  Модуль |  Рандомное число R  Факториал !  Арккосинус arc')
    print('Если хотите получить случайное число, введите первое любое число, ОПЕРАЦИЯ R , и второе люьое число')
    print('Вычисление факториала происходит только для первого числа ')

    print(' ')
    a=float(input("Введите первое число "))
    operation=input("Введите операцию ")
    b=float(input("Введите второе число "))
    
    match operation:
        case ("+"):
            print(' ')
            print('Результат: ', a+b)
            print(' ')

        case ('-'):
            print(' ')
            print('Результат: ', a-b)
            print(' ')

        case ('*'):
            print(' ')
            print('Результат: ', a*b)
            print(' ')

        case ('/'):
            print(' ')
            print('Результат: ', a/b)
            print(' ') 

        case ('^'):
            print(' ')
            print('Результат: ', a**b)
            print(' ') 

        case ('|'):
            print(' ')
            print('Результат: Модуль первого числа  ', abs(a), " модуль второго числа ", abs(b))
            print(' ')

        case ('R'):
            import random
            print(' ')
            print(random.randrange(1, 1000, 1))
            print(' ') 
        
        case ('!'): 
            factorial = 1
            while a > 1:
                factorial *= a
                a -= 1
            print('Результат: ', factorial)
        
        case ('arc'):
           
            print(' ')
            print(math.acos(a))
            print(' ') 
         

    go=input('Если хотите продолжить введите любую цифру, что бы закрыть программа введите 0 ')


