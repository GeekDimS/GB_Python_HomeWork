# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def CountSubstring(s, sub):
    i = 0
    count = 0
    i = s.find(sub, i)
    while i != -1:
        i = s.find(sub, i+1)
        count += 1
    else:
        return count

s1 = input('Введите первую строку:  ')
s2 = input('Введите вторую строку:  ')
if(len(s1) >= len(s2)):
    print(CountSubstring(s1, s2))
    # print(s1.count(s2))                # Вариант замены верхней строки без написания функции
else:
    print(CountSubstring(s2, s1))
    # print(s2.count(s1))                # Вариант замены верхней строки без написания функции