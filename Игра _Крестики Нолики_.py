import time
def greet():


    print(' * ' * 8)
    print(' * ДОБРО ПОЖАЛОВАТЬ!  * ')
    print(' *      в игру        * ')
    print(' *  КРЕСТИКИ-НОЛИКИ   * ')
    print(' * ' * 8, end='\n\n')

    time.sleep(2)

    print(" Правила игры: ", ' Ходы осуществляются сперва вводом номера строики (горизонтально), затем столбца(вертикально). '
                         'Вводятся два Числа от 0 до 2 через пробел!', sep='\n', end='\n\n')


    print(' * ' * 8, end='\n\n')

    time.sleep(5)
    print(" ЖЕЛАЮ ПОБЕДЫ И ПРИЯТНОЙ ИГРЫ!", end='\n\n')

field = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def show():
    print(f'  | 0 | 1 | 2 |')
    print('-- --- --- --- ')
    for i, row in enumerate(field):    # enumerate функция которая пронумеровывает индекс списка и его элемент
        row_info = f"{i} | {' | '.join(row)} |"
        print(row_info)
        print('-- --- --- --- ')

def ask():   # Спрашиваем у игрока номер строки и интекс элемента куда ввести Х или 0
    while True:

        cords = input('  Ваш ход: ').split()

        if len(cords) != 2:
            print('Введите 2 числа от 0 до 2 через пробел!')
            continue    # При не выполнении операции переводит на следующую итерацию

        x, y = cords

        # Проверка х и у на числа:
        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите 2 ЧИСЛА от 0 до 2 через пробел! А не буквы или знаки')
            continue

        x, y = int(x), int(y)

        # Проверка вхождения х и у в диапозан двумерного массива
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == ' ':    # Проверяем пустали клетка в массиве
                return x, y
            else:
                print('Клетка уже занята выбирите другие строчку и столбец')
        else:
            print('такие значения строк или столбцов не принемаются. Указывайте от 0 до 2!')

def check_win():

    for i in range(3):    # Цикл поиска нужных точек для установления победы
        symbols = []    # список где сравниваютя равныли ли символы в трех точка
        for j in range(3):
            symbols.append(field[i][j])     # смотрим по строке совпадают ли
        if symbols == ['X', 'X', 'X']:
            print("ПОЗДРАВЛЯЮ ПОБЕДУ ОДЕРЖАЛ X!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])     # смотрим по столбцу совпадают ли
        if symbols == ['X', 'X', 'X']:
            print("ПОЗДРАВЛЯЮ ПОБЕДУ ОДЕРЖАЛ X!")
            return True

    for i in range(3):
        symbols = []
        symbols.append(field[i][2-i])     # смотрим по правой диагонали совпадают ли
    if symbols == ['X', 'X', 'X']:
        print("ПОЗДРАВЛЯЮ ПОБЕДУ ОДЕРЖАЛ X!")
        return True

    for i in range(3):
        symbols = []
        symbols.append(field[i][i])     # смотрим по правой диагонали совпадают ли
    if symbols == ['X', 'X', 'X']:
        print("ПОЗДРАВЛЯЮ ПОБЕДУ ОДЕРЖАЛ 0!")
        return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ['0', '0', '0']:
            print("ПОЗДРАВЛЯЮ ПОБЕДУ ОДЕРЖАЛ 0!")
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ['0', '0', '0']:
            print("ПОЗДРАВЛЯЮ ПОБЕДУ ОДЕРЖАЛ 0!")
            return True


    for i in range(3):
        symbols = []
        symbols.append(field[i][i])
    if symbols == ['0', '0', '0']:
        print("ПОЗДРАВЛЯЮ ПОБЕДУ ОДЕРЖАЛ 0!")
        return True


    for i in range(3):
        symbols = []
        symbols.append(field[i][2 - i])
    if symbols == ['0', '0', '0']:
        print("ПОЗДРАВЛЯЮ ПОБЕДУ ОДЕРЖАЛ 0!")
        return True
    return False


greet()


num = 0   # Переменная которая считает ходы
while True:
    num += 1

    show()    # Отображаем функцию поля


    if num % 2 == 1:
        print('                ХОДИТ ИГРАЮЩИЙ Х')
    else:
        print('                ХОДИТ ИГРАЮЩИЙ 0')

    x, y = ask()    # Запрашиваем значения с помощью функции ask и заносим возвращенные(return x, y)
    # в переменные х и у

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'


    if check_win():

        break


    if num == 9:

        print('ПОЗДРАВЛЯЮ ПОБЕДИЛА ДРУЖБА!!')

        break
