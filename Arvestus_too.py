# B-2 Sport
from module1 import *
from random import *
# Напишите функцию sport(), при запуске которой происходит заполнение двух списков: sportlased[], tulemused[].  Список sportlased[] - заполняет пользователь,
#  а список результаты[] – заполняется автоматически: оздаеются случайные 3 числа и наибольшее из них заносится в список.
# После заполнения списков появляется меню с выбором действий:
# • Узнать n лучших результатов;
# • Упорядочить список в порядке возрастания баллов. Отобразить спортсменов их баллы и места;
# • Ввести имя одного или нескольких спортсменов и показать его/их результат;
# • Дисквалифицировать(удалить из списка)  спортсменов, у которых результаты хуже чем придуманный вами критерий;
# • Свой вариант.
# Для описания действий создайте необходимые функции.
print("Соревнования!!!")
i=randint(5,10)

for j in range (1, i+1):
    while 1:
        sportlane=str(input("Sisesta nimi sportlane: ")).capitalize()
        if sportlane.isalpha():break
        else:
            print("Ответ должен состоять из букв!")
    while 1:
        arv1=randint(1,100)
        arv2=randint(1,100)
        arv3=randint(1,100)
        if arv1>arv2 and arv1>arv3:
            tulemus=arv1
            break
        elif arv2>arv1 and arv2>arv3:
            tulemus=arv2
            break
        elif arv3>arv1 and arv3>arv2:
            tulemus=arv3
            break
        else:
            ("Числа не должны совподать!")
    sport(sportlane, tulemus)

print("MENU\n",
             "1. Узнать n лучших результатов;\n", 
             "2. Упорядочить список в порядке возрастания баллов. Отобразить спортсменов их баллы и места;\n",
             "3. Ввести имя одного или нескольких спортсменов и показать его/их результат;\n",
             "4. Дисквалифицировать спортсмен, которые набрали меньше 40 баллов;\n",
             "5. Узнать n худших результатов.")
try:
    while 1:
        valik=int(input("Введите свой выбор: "))
        if valik==1:
            valik1(valik)
            break
        elif valik==2:
            valik2(valik,sportlased, tulemused)
            break
        elif valik==3:
            valik3(valik)
            break
        elif valik==4:
            valik4(valik, sportlased, tulemused)
        elif valik==5:
            valik5(valik)
            break
        else:
            print()

except:
    print("Ответ должен быть числовым!")