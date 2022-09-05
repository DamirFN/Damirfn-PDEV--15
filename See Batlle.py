from random import randint
import time


# КЛАСС ТОЧКИ И ИХ СРАВНИЯ
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):    # Метод сравнения
        return self.x == other.x and self.y == other.y    # Проверяем равны ли точки между собой

    def __repr__(self):    # Вывод точек в консоль для проверки
        return f"({self.x}, {self.y})"


# ОБЩИЙ КЛАСС ИСКЛЮЧЕНИЙ BoardException
class BoardException(Exception):
    pass

class BoardOutException(BoardException):     # Исключения на доске
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class BoardUsedException(BoardException):    # Пользовательские исключения
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):  # служит для расположения кораблей
    pass


# ОБЩИЙ КЛАСС КОРАБЛЯ
class Ship:
    def __init__(self, bow, dsh, o):    # dsh - длина корабля; о - ориентация корабля; bow - нос корабля
        self.dsh = dsh
        self.bow = bow
        self.o = o
        self.lives = dsh

    @property
    def dots(self):
        ship_dots = []    # Пустой список точек корабля для наполнения
        for i in range(self.dsh):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:      # Вертикальная ориентация корабля; увеличивается по X
                cur_x += i

            elif self.o == 1:    # Вертикальная ориентация корабля; увеличивается по Y
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))   # заполняем список ship_dots циклом for

        return ship_dots

    def shooten(self, shot):     # Выстрелы по координатам корабля
         return shot in self.dots    # есть ли shot в координатах s


# ОБЩИЙ КЛАСС ИГРОВОЕ ПОЛЕ
class Board:
    def __init__(self, hid=True, size=6):
        # hid - где скрыто поле или нет; size - размер поля по вертикали и горизонтали
        self.size = size
        self.hid = hid

        self.count = 0    # количество пораженных кораблей

        self.field = [['~'] * 6 for i in range(6)]

        self.busy = []   # точки занятые кораблем или точки куда стреляли
        self.ships = []    # список кораблей доски


# ОБЩИЙ КЛАСС ДОБАВЛЕНИЕ КОРАБЛЕЙ НА ПОЛЕ CLASS BOARD
    def add_ship(self, ship):

        for d in ship.dots:
            if self.out(d) or d in self.busy:   # проверяем не уходит ли точка за границы или на занятость
                raise BoardWrongShipException()   # если да, то вызываем исключение
        for d in ship.dots:
            self.field[d.x][d.y] = "O"   # Проходимся по точкам корабля и ставим в них O
            self.busy.append(d)

        self.ships.append(ship)    # Список собственных кораблей
        self.contour(ship)      # Контур собственных кораблей


    # Создание контура в который будут входить точки вокруг корабля
    def contour(self, ship, verb=False):  # где ship - точка корабля, verb - точка попадания в контур корабля
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]  # Список точек во круг каждой точки корабля, где точка (0, 0)- сама точка корабля
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)  # В эти точки корабли ставить нельзя
                if not (self.out(cur)) and cur not in self.busy:    # если точка не занята
                    if verb:
                        self.field[cur.x][cur.y] = "."    # На место занятой точки ставит точку
                    self.busy.append(cur)   # Добавляем в список занятых



    # Строим сетку нашей доски с номерами столбцов
    def __str__(self):
        res = ""
        print(f'  | 1 | 2 | 3 | 4 | 5 | 6 |')
        print('-- --- --- --- --- --- ---')
        for i, row in enumerate(self.field):  # enumerate функция, которая пронумеровывает индекс списка и его элемент
            res = f"{i + 1} | {' | '.join(row)} |"
            print(res)
            print('-- --- --- --- --- --- ---')

        if self.hid:
            res2 = res.replace("O", "■")
        return ''

    def out(self, d):
        return not((0 <= d.x < self.size) and (0 <= d.y < self.size))


    # Делаем выстрелы по кораблю
    def shot(self, d):
        if self.out(d):    # Проверка точки за границей
            raise BoardOutException()

        if d in self.busy:  # Проверка точки на занятость
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.shooten(d):
                ship.lives -= 1    # Вычитаем жизнь с корабля при попадании
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1    # Прибавляем количество пораженных кораблей
                    self.contour(ship, verb=True)    # Обводим контур кораблей
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False
    def begin(self):
        self.busy = []


# ДОБАВЛЯЕМ CLASS PLAYER
class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):   # Функция хода
        while True:
            try:
                target = self.ask()   # Опрашиваем сделать ход
                repeat = self.enemy.shot(target)    # Опрашиваем повторить ли ход
                return repeat
            except BoardException as e:    # При ошибке хода
                print(e)


# ДОБАВЛЯЕМ CLASS AI ИСКУССТВЕННЫЙ ИНТЕЛЕКТ
class AI(Player):
    def ask(self):    # Опрашиваем ai сделать выстрел
        d = Dot(randint(0, 5), randint(0, 5))    # ai ходит на случайные координаты в пределах сетки
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


# ДОБАВЛЯЕМ CLASS USER
class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:  # Проверка количества введенных координат точки
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):    # Проверка на числа
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)    # Убираем отступ для сопоставления координат точки и выстрела

# ДОБАВЛЯЕМ CLASS GAME
# Создаем доски для игры уже с кораблями
class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()    # Генерируем доску для игрока
        co = self.random_board()    # Генерируем доску ai
        co.hid = True               # Прячем доску ai

        self.ai = AI(co, pl)        # Создаем доску ai
        self.us = User(pl, co)      # Создаем доску для игрока

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    # Функция приветствия
    def greet(self):

        print(' * ' * 8)
        print(' * ДОБРО ПОЖАЛОВАТЬ!  * ')
        print(' *      в игру        * ')
        print(' *    МОРСКОЙ БОЙ     * ')
        print(' * ' * 8, end='\n\n')

        time.sleep(2)

        print(" Правила игры: ",
              ' Ходы осуществляются сперва вводом номера строки (горизонтально), затем столбца(вертикально). '
              'Вводятся два Числа от 1 до 6 через пробел!', sep='\n', end='\n\n')

        print(' * ' * 8, end='\n\n')

        time.sleep(5)
        print(" ЖЕЛАЮ ПОБЕДЫ И ПРИЯТНОЙ ИГРЫ!", end='\n\n')



    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]   # Список длин всех кораблей на доске
        board = Board(size=self.size)
        attempts = 0
        for dsh in lens:
            while True:    # Циклом выставляем корабли
                attempts += 1    # Счётчик количество попыток выставить
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), dsh, randint(0, 1))   # Выставляем
                # корабли
                try:
                    board.add_ship(ship)
                    break    # Если удачно выставились корабли прерываем цикл
                except BoardWrongShipException:    # При неправильных точках корабля
                    pass
        board.begin()
        return board

    def loop(self):
        num = 0    # Номер хода
        while True:    # Цикл "кто ходит?"
            print("-" * 27)
            print("Доска игрока:")
            print(self.us.board)
            print("-" * 27)
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:    # Очередность хода
                print("-" * 27)
                print("Ходит игрок!")
                repeat = self.us.move()
            else:
                print("-" * 27)
                print("Ходит компьютер!")

                repeat = self.ai.move()
            if repeat:
                num -= 1    # Дает возможность сделать еще раз ход

            if self.ai.board.count == 7:  # если число подбитых кораблей равно их количеству выиграл ai
                print("-" * 27)
                print("Игрок выиграл!")
                break

            if self.us.board.count == 7:  # если число подбитых кораблей равно их количеству выиграл пользователь
                print("-" * 27)
                print("Компьютер выиграл!")
                break
            num += 1

    # Функция start служит запуску игры
    def start(self):
        self.greet()
        self.loop()
g = Game()
g.start()



