# Подсчитать сумму цифр в вещественном числе.

sV = str(input('Введите вещественное число:  '))

sV = sV.strip(' -')
sV = sV.replace('.','')
sV = sV.replace(',','')

if sV.isnumeric() == False:
    print("Введено не число")
    exit
res = 0
for i in sV:
    res += int(i)
print(res)