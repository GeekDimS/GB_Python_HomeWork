# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются
# операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;
# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные
# данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике —
# сжатая версия этого текста).
# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв
#  после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. Также
# создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.

# Экстра-задачи:
# 1.Рассмотрим все целочисленные комбинации ab для 2 ≤ a ≤ 5 и 2 ≤ b ≤ 5:
# 22=4, 23=8, 24=16, 25=32
# 32=9, 33=27, 34=81, 35=243
# 42=16, 43=64, 44=256, 45=1024
# 52=25, 53=125, 54=625, 55=3125
# Если их расположить в порядке возрастания, исключив повторения, мы получим следующую последовательность
#  из 15 различных членов:
# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
# Сколько различных членов имеет последовательность ab для 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100?
# 2. Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало
# являются простыми числами: 197, 719 и 971.
# Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
# Сколько существует круговых простых чисел меньше миллиона?
# 3. Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. Однако, их разность, 70 − 22 = 48, не является
#  пятиугольным числом.
# Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность являются пятиугольными числами
#  и значение D = |Pk − Pj| минимально, и дайте значение D в качестве ответа.


# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются
# операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


# example = '1-2*3'
# example2 = '(1+2)*3'
# example3 = '(5*2)+(3*4/3)+(4-3*3)'

# data_str = example[:]

# def calculate_open_braces(inp_str):
#     s_inp = inp_str[:]
#     s_inp = s_inp.replace(' ', '') # убираем пробелы из строки
#     start, end = None, None   #
#     str_left, str_right = '',''
#     count = s_inp.count('(')
#     while True:
#         if count == 0:
#             return calculate_arithm(s_inp)
#         for index in range(0, len(s_inp)):  # Перебираем символы в строке по порядку. Ищем скобки
#             if s_inp[index] == '(':
#                 start = index
#             if s_inp[index] == ')':
#                 end = index
#                 break
#         if start > 0:
#             if s_inp[start-1] == ')' or s_inp[start-1].isdigit():
#                 str_left = '*'
#         if end + 1 <= len(s_inp)-1:
#             if s_inp[end+1] == '(' or s_inp[end+1].isdigit():
#                 str_right = '*'
#         s_inp = s_inp[:start] + str_left + calculate_arithm(s_inp[start+1:end]) + str_right + s_inp[end + 1:]

#         count -= 1


# def calculate_arithm(inp_str):
#     s_inp = inp_str[:]
#     s_inp = s_inp.replace(' ', '')  # убираем пробелы из строки
#     res_str = ''
#     start, end = None, None
#     precision = 0
#     for oper in ['*', '/', '+', '-']:   # Цикл для всех арифметических операций в порядке приоритета
#         count = s_inp.count(oper)       # Количество текущих операций
#         if count != 0:
#             for i in range(0, count):   # Обход всех текущх операций в строке и выполнение их поочереди
#                 target = s_inp.find(oper)
#                 step = 1
#                 dot = False
#                 while (target - step >= 0) and (s_inp[target - step].isdigit() or s_inp[target - step] == '.'): # Ищем число слева от знака операции
#                     if s_inp[target - step] == '.':
#                         dot = True
#                         if precision < step:
#                             precision = step
#                     step += 1
#                 step -= 1
#                 start = target - step
#                 if dot:
#                     if s_inp[start:target] == '':
#                         a = 0
#                     else:
#                         a = float(s_inp[start:target])
#                 else:
#                     if s_inp[start:target] == '':
#                         a = 0
#                     else:
#                         a = int(s_inp[start:target])
#                 step = 1
#                 dot = False
#                 pred_prec = 0
#                 while (target + step < len(s_inp)) and (s_inp[target + step].isdigit() or s_inp[target + step] == '.' or s_inp[target + 1] == '-'):
#                     if s_inp[target + step] == '.':
#                         dot = True
#                         pred_prec = step
#                     step += 1
#                 step -= 1
#                 end = target + step
#                 if precision < (end - pred_prec):
#                     precision = end - pred_prec
#                 if dot:
#                     b = float(s_inp[target+1:end + 1])
#                 else:
#                     b = int(s_inp[target+1:end + 1])
#                 if oper == '*':
#                     res = str(a*b)
#                 if oper == '/':
#                     res = str(a/b)
#                 if oper == '+':
#                     res = str(a+b)
#                 if oper == '-':
#                     res = str(a-b)
#                 s_inp = s_inp[0:start] + res + s_inp[end+1:]
#     return s_inp


# print(data_str)
# print(calculate_open_braces(data_str))


# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные
# данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике —
# сжатая версия этого текста).


text = """A2AAAAAAggggggggggggk 9999999999999999999 8kk lll dddddddddrrrrrrrppp
tttttttttuiinnnnnnnnn kkkkk"""
text2 = """Сказка «Репка»
Русская народная сказка
Русская народная сказка «Репка»
Посадил дед репку. Выросла репка большая-пребольшая. Пошёл дед репку рвать: тянет-потянет, вытянуть не может!

Позвал дед бабку: бабка за дедку, дедка за репку — тянут-потянут, вытянуть не могут!

Позвала бабка внучку: внучка за бабку, бабка за дедку, дедка за репку — тянут-потянут, вытянуть не могут!

Позвала внучка Жучку: Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку — тянут-потянут, вытянуть не могут!

Позвала Жучка кошку: кошка за Жучку, Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку — тянут- потянут, вытянуть не могут!

Позвала кошка мышку: мышка за кошку, кошка за Жучку, Жучка за внучку, внучка за бабку, бабка за дедку, дедка за репку — тянут-потянут, — вытянули репку!"""

# path1 = 'text_for_encode.txt'
# path2 = 'text_for_decode.txt'
# with open(path1, 'w') as data:
#     data.write(text)
    
# def encode_text(name_file_in, name_file_out):
#     res = ''
#     old_char = ''
#     count = 1
#     with open(name_file_in, 'r') as data:
#         for lines in data.readlines() :
#             for char in lines:
#                 if char != old_char or count == 9:
#                     if old_char:
#                         res += str(count) + old_char
#                     old_char = char
#                     count = 1
#                 else:
#                     count += 1
#         else:
#             res += str(count) + old_char
#             with open(name_file_out, 'w') as data:
#                 data.write(res)


# def decode_text(name_file):
#     step = 0
#     count = 0
#     res = ''
#     with open(name_file,'r') as data:
#         for lines in data.readlines() :
#             for char in lines:
#                 if step == 0:
#                     count = int(char)
#                 else:
#                     res += count * char
#                 step = (step + 1) % 2
#         return res


# encode_text(path1, path2)
# print(decode_text(path2))



# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв
#  после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. Также
# создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.


# path1 = 'text_for_encode_ROT13.txt'
# path2 = 'text_for_decode_ROT13.txt'
# with open(path1, 'w') as data:
#     data.write(text)

# def encode_ROT13(line):
#     res = ''
#     enc_alpha = 'abcdefghijklmnopqrstuvwxyz'
#     for symb in line:
#         dig = enc_alpha.find(symb.lower())
#         if dig != -1:
#             char = enc_alpha[(dig + 13)%26]
#         else:
#             char = symb
#         res += char
#     return res


# print(encode_ROT13(text))                   # Закодированная строка
# print(encode_ROT13(encode_ROT13(text)))     # Декодированная обратно строка


# 1.2 (2 вариант решения 1 задачи)
#  Написать программу вычисления арифметического выражения заданного строкой. Используются
# операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

example3 = '(5*22)+(3*4/3)+(4-3*3)'# '5*6+(2-9)'#

# def calculate_arithm_2(inp_str):
#     s_inp = inp_str[:]
#     s_inp = s_inp.replace(' ', '')  # убираем пробелы из строки
#     res_str = ''
#     start, end = None, None

def infix_to_postfix(line):
    inline = line[:]
    inline = inline.replace(' ', '')
    stack = []
    res = []
    prev_is_number = 0
    for symb in inline:
        if symb.isdigit():            
            prev_is_number = prev_is_number*10 + int(symb)
            # res[-1] = res[-1]*10**prev_is_number + symb
            # prev_is_number += 1
        elif prev_is_number != 0:
            res.append(int(prev_is_number))
            prev_is_number = 0
        if symb == '(':
            stack.append(symb)
        if symb == ')':
            if len(stack) > 0:
                while len(stack)>0 and (temp := stack.pop()) != '(':
                    res.append(temp)
        if symb in ('+','-','*','/'):
            if len(stack) == 0 or stack[-1] == '(' or (symb in ('*','/') and stack[-1] in ('+','-')):
                stack.append(symb)
            else:
                if symb in ('*','/'):# and stack[-1] in ('+','-'):
                    while len(stack)>0 and (temp := stack.pop()) in ('*','/'):
                        #if temp != ')':
                        res.append(temp)
                if symb in ('+','-'):
                    while len(stack)>0 and (temp := stack.pop()) in ('*','/','+','-'):
                        res.append(temp)
                stack.append(symb)
    while len(stack)>0:
        res.append(stack.pop())
    return res

def calculate_postfix(inlist):
    stck = []
    a, b = 0, 0
    for elem in inlist:
        if type(elem) == int:          
            stck.append(elem)
        if elem in ('+','-','*','/'):
            if elem == '+':
                a = stck.pop()
                b = stck.pop()
                stck.append(a + b)
            if elem == '-':
                a = stck.pop()
                b = stck.pop()
                stck.append(a - b)
            if elem == '*':
                a = stck.pop()
                b = stck.pop()
                stck.append(a * b)
            if elem == '/':
                a = stck.pop()
                b = stck.pop()
                stck.append(a / b)
    return stck[0]


print(infix_to_postfix(example3))
print(calculate_postfix(infix_to_postfix(example3)))