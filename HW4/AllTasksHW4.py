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

# 2. Создать функцию, которая из списка чисел возвращает число, являющее суммой двух или 
# нескольких других элементов, либо возвращающее None, если такого числа нет.
# 3. Вот вам задача: https://cloud.mail.ru/public/7X6f/PXza5yoTP
#Найдите первые десять цифр суммы следующих ста 50-значных чисел.
# 37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690

# Вам помогут знания со второй лекции. Решение в лоб (скопировать число, вставить в переменную, 
# сделать из нее список с числами) – слабо подойдет. Подумайте, как то, что было в лекции, 
# вяжется с этой задачей.


# -----------------------------------------------------------------------------------------
# 1. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую
# последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя

from cmath import sqrt
from itertools import combinations
from random import randint
from unittest import result

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


# path = '1Kints.txt'

# with open(path, 'r') as fr:
#     inp_list = fr.readlines()
#     inp_list.pop()
#     list_val = list(map(int, inp_list))
# count = 0
# for vali in list_val:
#     for valj in list_val:
#         for valk in list_val:
#             if(vali + valj + valk == 0):
#                 print(f'{vali} + {valj} + {valk} = 0')
#                 count += 1
# print(f'Количество триплетов равно {count}') # Количество триплетов равно 420


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

# refbonus = 1500
# costbeer = 2


# def beeramid(refbonus, costbeer):
#     maxbeer = refbonus // costbeer
#     step = 0
#     while(maxbeer >= 0):
#         step += 1
#         maxbeer -= step**2
#     return step - 1


# print(beeramid(refbonus, costbeer))


# 2. Создать функцию, которая из списка чисел возвращает число, являющее суммой двух или 
# нескольких других элементов, либо возвращающее None, если такого числа нет.

# inp_list = []
# max_val = 10
# quantity = 6
# for i in range(quantity):
#     inp_list.append(randint(-max_val, max_val))

# #inp_list = [-9, 6, -6, -9, -7]

# def seek_summ(inp_list ,quantity):
#     inp_dict = {}
#     for index, item in enumerate(inp_list):
#         inp_dict[index] = inp_list[index]
#     print(inp_dict)

#     list_keys = list(inp_dict.keys())
#     set_use_keys = set()
#     set_unused_keys = set()
#     result = []

#     for cycle in range(2, quantity):
#         for item in combinations(list_keys, cycle): # Сочетания ключей
#             sum = 0
#             set_use_keys.clear()
#             set_unused_keys.clear()
#             str_result = ''
#             for j in item:                  # Для каждого ключа в выбранной комбинации
#                 sum += inp_dict[j]          # находим сумму значений
#                 set_use_keys.add(j)         # и записываем каждый ключ во множество использованных ключей
#             set_unused_keys = set(list_keys) - set_use_keys     # Находим неиспользованные в текущем сочетании ключи
#             for k in set_unused_keys:       # и ищем по значениям этих ключей равенство суммы сочетания со значением входного списка
#                 if(inp_dict[k]) == sum:
#                     for l in set_use_keys:
#                         str_result += str(inp_dict[l]) + ' '
#                     result.append(str(f'Числа {str_result} дают в сумме число {sum}'))    # Добавляем найденное в результат
#                     str_result = ''
#     return result
        
# print(seek_summ(inp_list ,quantity))



# 3. Найдите первые десять цифр суммы следующих ста 50-значных чисел.
# 37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690

# Вам помогут знания со второй лекции. Решение в лоб (скопировать число, вставить в переменную, 
# сделать из нее список с числами) – слабо подойдет. Подумайте, как то, что было в лекции, 
# вяжется с этой задачей.

# path = 'file_dat.txt'

# str_in = """37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690"""

# with open(path, 'w') as data:
#     data.write(str_in)

# sum = 0
# with open(path, 'r') as data:
#     numb = data.readline()
#     while numb:
#         sum += int(numb)
#         numb = data.readline()

# print(sum)
# print(f'Первые десять цифр результата: {str(sum)[0:10:]}')      



# 1*. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую
# последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя. Найти самую длиную последовательность.

list_in = [1, 5, 2, 3, 4, 6, 1, 7]
list_out = []
val_max = 0

def sequence_ok(list_seq):   # Функция проверки возрастающей последовательности
    val_max = 0
    for val in list_seq:
        if(val > val_max):
            val_max = val
        else:
            return False
    return True

for part in range(len(list_in)-1, 2, -1):   # Перебор возможных перестановок с уменьшением "окна"
    for item in combinations(list_in, part):
        if sequence_ok(item):
            print(item)
            exit()

# Решение от Прудникова# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

# dynamic programming with memoization: runtime O(n^2), memory using: O(n)
def dyn_prog(elements: list) -> list:
    dp = [0] * (len(elements) + 1)  # memoization
    best_indexes = [0] * (len(elements) + 1)  # best indexes list

    def rec_seeker(index: int) -> int:
        # border case:
        if index == -1:
            return 0

        #recurrent relation
        if index == len(elements) or dp[index] == 0:
            max_length = 0
            best_ind = -1
            for inner_index in range(index):
                if index == len(elements) or elements[inner_index] < elements[index]:
                    rec_sec_val = rec_seeker(inner_index) + 1
                    if max_length < rec_sec_val:
                        max_length = rec_sec_val
                        best_ind = inner_index

            # here we save the new calculated values of dp and best index
            dp[index] = max_length
            best_indexes[index] = best_ind

        return dp[index]

    rec_seeker(len(elements))

    # back motion to capture the right numbers
    result = []  # resulting LIS
    ind = len(elements)
    while True:
        ind = best_indexes[ind]  # the best way's steps -> here we get the longest increasing subsequence char by char
        if ind != -1:
            result.insert(0, str(elements[ind]))
        else:
            break

    return result


print(dyn_prog([1, 5, 2, 3, 4, 6, 1, 7]))
print(dyn_prog([5, 2, 3, 4, 6, 1, 7]))
print(dyn_prog([1, 1, 1, 1, 1, 5, 2, 1, 3, 4, 6, 1, 2, 2, 7]))


# СВЕРХ БЫСТРОЕ решение для нахождения ДЛИННЫ LIS, НЕ ГАРАНТИРУЕТ верную последовательность, НО ВЗАМЕН ГАРАНТИРУЕТ верную длину, скорость: O(N*log(N))
def get_longest_increasing_subsequence(elements: list) -> list:  # Runtime O(n*log(n)), where n = len(elements)
    result = []
    print('Building of the longest increasing subsequence (LIS):')
    for i in range(len(elements)):
        expected_index = bin_search(0, len(result) - 1, elements[i], result)  # expected place of element in the resulting set
        if expected_index == len(result):  # if the elements lies outside of current set
            result.append(elements[i])
        else:  # inside case -> we change the greater element by the less one at th position found with the binary search above
            result[expected_index] = elements[i]
        print(f'index = {i}, el[i] = {elements[i]}, expected index = {expected_index}, res: {result}')
    print(f'The quick length of LIS = {len(result)}')
    print('outcome pseudo-LIS: ', end='')
    return result


# Binary search of position the current element to be located at
def bin_search(left_border: int, right_border: int, target: int, elems: list) -> int:
    if right_border == -1:  # border case -> when there is no elements in elems list
        return 0

    if left_border == right_border:  # ending case -> the searching is finished
        return left_border + (1 if target > elems[left_border] else 0)  # the element is not found, and consequently it can be located inside the set or outside
    pivot_index = (left_border + right_border) // 2  # median index
    if elems[pivot_index] < target:  # here we decide in which part of current interval the target should be distributed
        return bin_search(pivot_index + 1, right_border, target, elems)
    elif elems[pivot_index] > target:
        return bin_search(left_border, pivot_index, target, elems)
    else:
        return pivot_index  # the case of finding the target amongst the elements given


print(get_longest_increasing_subsequence([1, 5, 2, 3, 4, 6, 1, 7]))
print(get_longest_increasing_subsequence([5, 2, 3, 4, 6, 1, 7]))
