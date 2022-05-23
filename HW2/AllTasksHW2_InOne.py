# 1.	Найти сумму чисел списка стоящих на нечетной позиции

from audioop import reverse


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