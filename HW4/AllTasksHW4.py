# 1.	Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую
# последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя

# 2.	Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого
# файла по возрастанию.
# 3.	Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа,
# которые в сумме дают 0. (решение будет долгим, ибо является демонстрационным при теме
# многопоточного программирования).

# Экстра-задачи:
# 1.	Давайте представим, что ваша компания только что наняла вашего друга из колледжа и заплатила
#  вам реферальный бонус. Потрясающе! Чтобы отпраздновать, вы берете свою команду в очень странный бар
#  по соседству и используете реферальный бонус, чтобы купить и построить самую большую трехмерную
#  пирамиду из пивных банок, которую вы можете.
# Пирамида пивных банок будет квадратировать количество банок на каждом уровне - 1 банка на верхнем
#  уровне, 4 на втором, 9 на следующем, 16, 25...
# Определите функцию beeramid, чтобы вернуть количество полных уровней пирамиды пивных банок,
# которую вы можете сделать, учитывая параметры: реферальный бонус и цена пивной банки.
# Например:
# beeramid(1500, 2)# 12
# beeramid(5000, 3)# 16

# 2.	Создать функцию, которая из списка чисел возвращает число, являющее суммой двух или нескольких других элементов, либо возвращающее None, если такого числа нет.
# 3.	Вот вам задача: https://cloud.mail.ru/public/7X6f/PXza5yoTP
# Вам помогут знания со второй лекции. Решение в лоб (скопировать число, вставить в переменную, сделать из нее список с числами) – слабо подойдет. Подумайте, как то, что было в лекции, вяжется с этой задачей.


# -----------------------------------------------------------------------------------------
# 1. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую
# последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя

# from random import randint


# list_in = [1, 5, 2, 3, 4, 6, 1, 7]
# list_out = []
# val_max = 0

# for val in list_in:
#     if(val > val_max):
#         val_max = val
#         list_out.append(val)
# print(list_out)


# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого
# файла по возрастанию.

# path = 'file4_2.txt'

# max_val = 100
# quantity = 10
# data = open(path, 'w')
# for i in range(quantity):
#     data.write(f'{str(randint(0, max_val))},')
# data.close()

# with open(path, 'r') as fr:
#     list_int = fr.readline().split(',')
#     list_int.pop()
#     list_int.sort(key=(int))
# print(list_int)


# 3. Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа,
# которые в сумме дают 0. (решение будет долгим, ибо является демонстрационным при теме
# многопоточного программирования).

path = '1Kints.txt'

with open(path, 'r') as fr:
    inp_list = fr.readlines()
    inp_list.pop()
    list_val = list(map(int, inp_list))
count = 0
for vali in list_val:
    for valj in list_val:
        for valk in list_val:
            if(vali + valj + valk == 0):
                print(f'{vali} + {valj} + {valk} = 0')
                count += 1
print(f'Количество триплетов равно {count}') # Количество триплетов равно 420
# print(list_val)