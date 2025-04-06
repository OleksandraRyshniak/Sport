# B-2 Sport
# Напишите функцию sport(), при запуске которой происходит заполнение двух списков: sportlased[], tulemused[].  Список sportlased[] - заполняет пользователь,
#  а список результаты[] – заполняется автоматически: оздаеются случайные 3 числа и наибольшее из них заносится в список.
# После заполнения списков появляется меню с выбором действий:
# • Узнать n лучших результатов;
# • Упорядочить список в порядке возрастания баллов. Отобразить спортсменов их баллы и места;
# • Ввести имя одного или нескольких спортсменов и показать его/их результат;
# • Дисквалифицировать(удалить из списка)  спортсменов, у которых результаты хуже чем придуманный вами критерий;
# • Свой вариант.
# Для описания действий создайте необходимые функции.
from random import *
from module1 import *
print("Võistlus!!!")
i=randint(5,10)

for j in range (1, i+1):
    while 1:
        sportlane=str(input("Sisesta nimi sportlane: ")).capitalize()
        if sportlane.isalpha():break
        else:
            print("Vastus peab koosnema tähtedest!")
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
            ("Numbrid ei pea kokku langema!")
    sport(sportlane, tulemus)

print("MENU\n",
             "1. Tunnistage n parimat tulemust;\n", 
             "2. Korraldage nimekiri punktide kasvavas järjekorras. Kuvage sportlaste tulemused ja kohad;\n",
             "3. Sisestage ühe või mitme sportlase nimi ja näidake tema(te) tulemust(ed);\n",
             "4. Diskvalifitseerida sportlane, kes on saanud vähem kui 40 punkti;\n",
             "5. Tunnistage n halvimat tulemust;\n",
             "6. Väljumine.")
while 1:
    try:
        valik=int(input("Sisesta oma valik: "))
        if valik==1:
            valik1(valik)
            break
        elif valik==2:
            valik2(valik,sportlased, tulemused)
            break
        elif valik==3:
            valik3(valik, sportlased, tulemused)
            break
        elif valik==4:
            valik4(valik, sportlased, tulemused)
            break
        elif valik==5:
            valik5(valik, sportlased, tulemused)
            break
        elif valik==6:
            break
        else:
            print("Sisestage number vahemikus 1 kuni 6!")
    except:
        print("Vastus peab olema numbriline!")