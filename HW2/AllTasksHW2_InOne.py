# 1.	Найти сумму чисел списка стоящих на нечетной позиции

from audioop import reverse
from random import randint


inpList = [2, 4, 5, 7, 3, 8, 3, 1, 5, 5, 3]
res = 0
for item in range(1, len(inpList), 2):
    res += inpList[item]
print(res)


# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

inpList2 = [2, 3, 4, 5, 6, 9]
resList = []

# 0.1 добавлена, чтобы round(x.5) округляла "правильно" всегда в большую сторону
for i in range(0, round((len(inpList2)+0.1)/2)):
    resList.append(inpList2[i]*inpList2[-1*i-1])
print(resList)


# 3. В заданном списке вещественных чисел найдите разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

inpList3 = [1.1, 1.2, 3.1, 5, 10.01]
divList = []
for i in range(len(inpList3)):
    divList.append(inpList3[i] - inpList3[i]//1)
maxVal = max(divList)
minVal = min(divList)
res = maxVal-minVal
print(f'{res:.2f}')


# 4. Написать программу преобразования десятичного числа в двоичное

inpNumb = input('Введите целое положительное число:  ')
inpNumb = inpNumb.strip(' ')
if (inpNumb.isnumeric() == False) or (inpNumb == None):
    print("Введено не целое положительное число")
    exit()
numb = int(inpNumb)

s = ''
while numb != 0:
    div = numb % 2
    s = s + str(div)
    numb = numb // 2
print(s[::-1])


# Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.

inpBinary = str(input('Введите двоичное число:  '))
inpBinary = inpBinary[::-1]
res = 0
for i, val in enumerate(inpBinary):
    if val == '1':
        res += 2**i
print(res)


# 2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:
# Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число.
# За каждую цифру, которую пользователь правильно угадал в нужном месте, у них есть “корова”.
# За каждую цифру, которую пользователь угадал правильно, в неправильном месте стоит “бык”.
# Каждый раз, когда пользователь делает предположение, скажите им, сколько у них “коров” и “быков”.
# Как только пользователь угадает правильное число, игра окончена.
# Следите за количеством догадок, которые пользователь делает на протяжении всей игры,
# и сообщите пользователю в конце.

randomNumberStr = str(randint(1000, 9999))
print('Игра "Коровы(A) и быки(V)" начинается!!!')
inpNumb2 = input('Введите 4-хзначное число:  ')
res = inpNumb2
outStr = ''
count = 0
while res != randomNumberStr:
    for i in range(4):
        if randomNumberStr[i] == res[i]:
            outStr += 'A'
        elif res[i] in randomNumberStr:
            outStr += 'V'
        else:
            outStr += '*'
    count += 1
    print(outStr)
    outStr = ''
    res = input('Угадывайте дальше. Снова введите 4-хзначное число:  ')
print(f'Ура! Вы угадали задуманное число {res} с {count} шагов!')


# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

# Упомяну, что обычно первыми членами считаются 1, 1, 2, 3, 5, 8...

membSequenceAct = 2
membSequenceOld = 1
membSequenceNew = 3
summOdd = 2
count = 2
while membSequenceNew <= 4000000:
    membSequenceNew = membSequenceOld + membSequenceAct
    membSequenceOld = membSequenceAct
    membSequenceAct = membSequenceNew
    count += 1
    if count % 2 == 0:
        summOdd += membSequenceAct
print(
    f'Номер последнего члена последовательности Фибоначчи {count-1} . Число {membSequenceOld} . Сумма чётных членов до этой границы равна  {summOdd}')


# 4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

listPrimeNumber = [2]
listTargetPrimeNumber = []
number = 600851475143 #13195
optNumber = int(number // 2)
for i in range(3, optNumber, 2):
    primeNumber = 1
    for j in listPrimeNumber:
        if i % j == 0:
            primeNumber = 0
            break
    if primeNumber:
        listPrimeNumber.append(i)
        print(f'Простое число {i}')
for i in listPrimeNumber:
    if number % i == 0:
        listTargetPrimeNumber.append(i)
        print(f'Делитель {i}')
print(listTargetPrimeNumber)
