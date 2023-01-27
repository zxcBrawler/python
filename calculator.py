while True:
    def ChooseOperation(operations):
        match operations:
            case '+':
                return Plus()
            case '-':
                return Minus()
            case '*':
                return Multiply()
            case '/':
                return Divide()
            case '^':
                return Power()
            
    def Plus():
        num = 0
        q = 0
        while True:
            print('Введите число или = для окончания ввода')
            x = input()
            if x != "=":
                num += float(x)
                q += 1
            else:
                break
        print('Результат -', num)
        print('Количество введенных чисел - ' , q)

    def Minus():
        print('Введите первое число или = для окончания ввода')
        num = float(input())
        q = 0
        while True:
            print('Введите число или = для окончания ввода')
            x = input()
            if x != "=":
                num -= float(x)
                q += 1
            else:
                break
        print('Результат -', num)
        print('Количество введенных чисел - ', q)

    def Multiply():
        print('Введите первое число или = для окончания ввода')
        num = float(input())
        q = 0
        while True:
            print('Введите число или = для окончания ввода')
            x = input()
            if x != "=":
                num *= float(x)
                q += 1
            else:
                break
        print('Результат -', round(num, 3))
        print('Количество введенных чисел - ', q)

    def Divide():
        print('Введите первое число или = для окончания ввода')
        num = float(input())
        q = 0
        while True:
            print('Введите следующее число или = для окончания ввода')
            x = input()
            if x != "=":
                if float(x) != 0:
                    num /= float(x)
                    q += 1
                else:
                    print('На ноль делить нельзя')
            else:
                break
        print('Результат -', round(num, 3))
        print('Количество введенных чисел - ', q)

    def Power():
        result = 0
        print('Введите число, которое хотите возвести в степень')
        a = input()
        while a == "": 
            print("Введите правильное значение")
            a = input()
        print('Введите степень')
        b = input()
        while b == "": 
            print("Введите правильное значение")
            b = input()
        result = float(a) ** float(b)
   
        print('Результат -', result)
            
    print("Введите необходимую операцию +, -, *, /, ^. Введите stop, чтобы завершить работу")
    inputOperation = input()
    if (inputOperation != 'stop'):
        ChooseOperation(inputOperation)
    else :
        break