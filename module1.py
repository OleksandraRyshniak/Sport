from random import *
sportlased=[]
tulemused=[]
# B-2 Sport

# Напишите функцию sport(), при запуске которой происходит заполнение двух списков: sportlased[], tulemused[].  Список sportlased[] - заполняет пользователь, 
# а список результаты[] – заполняется автоматически: оздаеются случайные 3 числа и наибольшее из них заносится в список.
# После заполнения списков появляется меню с выбором действий:
# • Узнать n лучших результатов;
# • Упорядочить список в порядке возрастания баллов. Отобразить спортсменов их баллы и места;
# • Ввести имя одного или нескольких спортсменов и показать его/их результат;
# • Дисквалифицировать(удалить из списка)  спортсменов, у которых результаты хуже чем придуманный вами критерий;
# • Свой вариант.
# Для описания действий создайте необходимые функции.

def sport(sportlane: str, tulemus)->any:
    """
    """
    sportlased.append(sportlane)
    tulemused.append(tulemus)
    return sportlased, tulemused
        

def tabel(sportlased: list, tulemused:list)->None:
    """
    """
    for n in range(len(sportlased)):
        t=print(f"{sportlased[n]} : {tulemused[n]}")
    return t


def valik1(valik:int)->any:
    """
    """
    i=0
    kogus=int(input("Введи количество лучших результатов: "))
    tulemused.sort(reverse=True)
    print(f"Топ {kogus} лучших результатов")
    for tulemus in tulemused:
        if i>=kogus:
            break
        j=tulemused.index(tulemus)
        nimi=sportlased[j]
        print(f"{nimi} : {tulemus}")
        i+=1

def valik5(valik:int)->any:
    """
    """
    i=0
    kogus=int(input("Введи количество худших результатов: "))
    tulemused.sort()
    print(f"Топ {kogus} худших результатов")
    for tulemus in tulemused:
        if i>=kogus:
            break
        j=tulemused.index(tulemus)
        nimi=sportlased[j]
        print(f"{nimi} : {tulemus}")
        i+=1

