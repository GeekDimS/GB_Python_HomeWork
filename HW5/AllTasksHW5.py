# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо.
#  Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её,
# причем чтобы сыграть в нее можно было в одиночку.
# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ,
# в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице,
# а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в
# магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице,
#  иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе,
# ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче.
#  «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму.
#  Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант,
#  что мусорные слова могли быть написаны без использования запятых
# 4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями
#  языков программирования, другой — с числами от 1 до длины первого плюс 1. Вам нужно сделать
#  две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
#  написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом:
#  если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается,
# его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение
#  порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем
# столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью
# reduce сложите получившиеся числа и верните из функции в качестве ответа.

# Экстра-задачи:
# 1. Супер-сложная.
# Совершенным числом называется число, у которого сумма его делителей равна самому числу. Например,
# сумма делителей числа 28 равна 1 + 2 + 4 + 7 + 14 = 28, что означает, что число 28 является
# совершенным числом.
# Число n называется недостаточным, если сумма его делителей меньше n, и называется избыточным,
# если сумма его делителей больше n.
# Так как число 12 является наименьшим избыточным числом (1 + 2 + 3 + 4 + 6 = 16), наименьшее число,
#  которое может быть записано как сумма двух избыточных чисел, равно 24. Используя математический
#  анализ, можно показать, что все целые числа больше 28123 могут быть записаны как сумма двух
# избыточных чисел. Эта граница не может быть уменьшена дальнейшим анализом, даже несмотря на то,
# что наибольшее число, которое не может быть записано как сумма двух избыточных чисел, меньше
#  этой границы.
# Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел.
# 2. Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со знаменателями
# от 2 до 10 даны ниже:
# 1/2=0.5
# 1/3=0.(3)
# 1/4=0.25
# 1/5=0.2
# 1/6=0.1(6)
# 1/7=0.(142857)
# 1/8=0.125
# 1/9=0.(1)
# 1/10=0.1
# Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. Заметим,
#  что 1/7 имеет повторяющуюся последовательность из 6 цифр.
# Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся
# последовательность цифр.
# 3. Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# Можно убедиться, что сумма чисел в диагоналях равна 101. (1+3+5+7+9+13+17+21+25)
# Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?


# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо.
#  Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

from doctest import set_unittest_reportflags
from random import randint
from re import X


input_text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
slice_string = 'абв'

output_text = ''
start = 0
end = input_text.casefold().find('абв')
while end != -1:
    output_text += input_text[start:end]
    start = end + len(slice_string)
    end = input_text.casefold().find('абв', start)
print(output_text)


# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её,
# причем чтобы сыграть в нее можно было в одиночку.

game = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


def print_data(data):
    print(data[0])
    print(data[1])
    print(data[2])


def counting_win(list_lists, lit):
    # if game[0] == ['X', 'X', 'X'] or game[1] == ['X', 'X', 'X'] or game[2] == ['X', 'X', 'X'] or (game[0][0] == 'X' and game[1][0] == 'X' and game[2][0] == 'X') or (game[0][1] == 'X' and game[1][1] == 'X' and game[1][2] == 'X') or (game[0][2] == 'X' and game[1][2] == 'X' and game[2][2] == 'X') or (game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X') or (game[0][2] == 'X' and game[1][1] == 'X' or game[2][0] == 'X'):
    #     return 1    

    for c in range(0, 3):
        win = True
        for r in range(0,3):
            win &= game[c][r] == lit
        if win:
            return True
    for r in range(0, 3):
        win = True
        for c in range(0,3):
            win &= game[c][r] == lit
        if win:
            return True
    win = True
    for rc in range(0, 3):        
        win &= game[rc][rc] == lit            
    if win:
        return True
    win = True
    for rc in range(0, 3):        
        win &= game[rc][2-rc] == lit            
    if win:
        return True
    return False     



print_data(game)
set_game = {'11', '12', '13', '21', '22', '23', '31', '32', '33'}
set_use_cell = set()
set_key = {'1', '2', '3'}
end = True
while end:
    not_ok = True
    while not_ok:
        row = input('Введите номер строки: ')
        if not row in set_key:
            print('Неправильно введён номер строки.')
            break
        column = input('Введите номер столбца: ')
        if not column in set_key:
            print('Неправильно введён номер столбца.')
            break
        use_cell = str(row) + str(column)
        if use_cell in set_use_cell:
            print('Эта клетка уже занята')
            break
        not_ok = False

    set_game.discard(use_cell)
    set_use_cell.add(use_cell)

    if set_game != set():        
        ai = set_game.pop()
        set_use_cell.add(ai)

    game[int(row)-1][int(column)-1] = 'X'
    game[int(ai[0])-1][int(ai[1])-1] = 'O'
    print_data(game)
    if counting_win(game, 'X'):
        print('Поздравляю! Вы победили!')
        end = False
    if counting_win(game, 'O'):
        print('Вы проиграли.')
        end = False
    if set_game == set():
        print('Боевая ничья!')
        end = False
