from random import *
sportlased=[]
tulemused=[]
# B-2 Sport

# Напишите функцию sport(), при запуске которой происходит заполнение двух списков: sportlased[], tulemused[].  Список sportlased[] - заполняет пользователь, 
# а список результаты[] – заполняется автоматически: оздаеются случайные 3 числа и наибольшее из них заносится в список.
# После заполнения списков появляется меню с выбором действий:

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
        

def tabel(sportlased: list, tulemused:list)->str:
    """
    """
    for n in range(len(sportlased)):
        t=print(f"{sportlased[n]} : {tulemused[n]}")
    return t

# Узнать n лучших результатов;
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

# Упорядочить список в порядке возрастания баллов. Отобразить спортсменов их баллы и места;
def valik2(valik:int, sportlased:list, tulemused:list)->any:
    """
    """
    sportlased_tulemused=list(zip(sportlased, tulemused))
    for h in range(len(sportlased_tulemused)):
        for i in range(h+1, len(sportlased_tulemused)):
            if sportlased_tulemused[h][1]>sportlased_tulemused[i][1]:
                sportlased_tulemused[h],sportlased_tulemused[i]=sportlased_tulemused[i],sportlased_tulemused[h]
    for i in range(len(sportlased_tulemused)):
        nimi, tulemus=sportlased_tulemused[i]
        print(f"{i+1}.{nimi} : {tulemus}")

# Ввести имя одного или нескольких спортсменов и показать его/их результат;
def valik3(valik:int)->None:
    """
    """
    kogus=int(input("Введи количество спортсменов,результаты которых хочешь посмотреть: "))
    for i in range(kogus):
        while 1:
            nimi=str(input("Siseta nimi: ")).capitalize()
            if nimi in sportlased:
                j=sportlased.index(nimi)
                tulemus=tulemused[j]
                h=print(f"{nimi}:{tulemus}")
                break
            else:
                print("Имени нет в списке, введите другое имя.")
    return h

#Дисквалифицировать(удалить из списка)  
#спортсменов, у которых результаты хуже чем придуманный вами критерий;
def valik4(valik:int, sportlased:list, tulemused:list)->None:
    """
    """
    res=40
    sportlased_tulemused=list(zip(sportlased, tulemused))
    for i in range (len(sportlased_tulemused)):
        nimi, tulemus=sportlased_tulemused[i]
        print(nimi, ":", tulemus)
        if sportlased_tulemused[i][1]<40:
            sportlased_tulemused.remove()
        print(nimi, ":", tulemus)

#Узнать n худших результатов.
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

