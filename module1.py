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

def sport(sportlane: str, tulemus)->str:
    """Nimede lisamine nimekirjadesse ja nende tulemused
    :param str sportlane: Sisend kasutajalt 
    :param str tulemus: Sisend kasutajalt 
    :rtype: str tagastab vastuse stringina
    """
    sportlased.append(sportlane)
    tulemused.append(tulemus)
    return sportlased, tulemused
        

# Узнать n лучших результатов;
def valik1(valik: int )->None:
    """Tunnista n parimat tulemust
    Kasutaja sisestab tipptulemuste arvu, mida ta soovib näha.
    :param int valik: funktsiooni valiku number
    :rtype: None
    """
    i=0
    kogus=int(input("Sisestage tipptulemuste arv: "))
    tulemused.sort(reverse=True)
    print(f"Top {kogus} parimad tulemused")
    for tulemus in tulemused:
        if i>=kogus:
            break
        j=tulemused.index(tulemus)
        nimi=sportlased[j]
        print(f"{nimi} : {tulemus}")
        i+=1

# Упорядочить список в порядке возрастания баллов. Отобразить спортсменов их баллы и места;
def valik2(valik: int, sportlased:list, tulemused:list)->None:
    """Sportlaste, tulemuste ja nende kohtade kuvamine punktide järjekorras.
    Funktsioon sorteerib sportlased tulemuste järgi kasvavas järjekorras
    :param int valik: funktsiooni valiku number
    :param list sportlased: Sportlaste nimede loend
    :param list tulemused: Sportlaste tulemuste loend
    :return: None 
    """
    sportlased_tulemused=list(zip(sportlased, tulemused))
    for h in range(len(sportlased_tulemused)):
        for i in range(h+1, len(sportlased_tulemused)):
            if sportlased_tulemused[h][1]>sportlased_tulemused[i][1]:
                sportlased_tulemused[h],sportlased_tulemused[i]=sportlased_tulemused[i],sportlased_tulemused[h]
    for i in range(len(sportlased_tulemused)):
        nimi, tulemus=sportlased_tulemused[i]
        print(f"{len(sportlased_tulemused)-i}.{nimi} : {tulemus}")

# Ввести имя одного или нескольких спортсменов и показать его/их результат;
def valik3(valik: int, sportlased: list, tulemused: list)->str:
    """Funktsioon võimaldab sisestada ühe või mitme sportlase nime ja kuvab nende tulemused.
    Kasutaja sisestab kõigepealt soovitud sportlaste arvu ja seejärel sportlaste nimed.
    :param int valik: funktsiooni valiku number
    :param list sportlased: Sportlaste nimede loend
    :param list tulemused: Sportlaste tulemuste loend
    :return: str
    """
    kogus=int(input("Sisestage nende sportlaste arv, kelle tulemusi soovite näha: "))
    for i in range(kogus):
        while 1:
            nimi=str(input("Siseta nimi: ")).capitalize()
            if nimi in sportlased:
                j=sportlased.index(nimi)
                tulemus=tulemused[j]
                h=print(f"{nimi}:{tulemus}")
                break
            else:
                print("Nimi ei ole nimekirjas, sisestage teine nimi.")
    return h

#Дисквалифицировать(удалить из списка)  
def valik4(valik: int, sportlased: list, tulemused: list) -> None:
    """Funktsioon kuvab kõik sportlased ja nende tulemused ning seejärel filtreerib ja kuvab
    ainult need sportlased, kelle tulemus on võrdne või suurem kui etteantud piir.
    :param int valik: funktsiooni valiku number
    :param list sportlased: Sportlaste nimede loend
    :param list tulemused: Sportlaste tulemuste loend
    :return: None
    """
    res = 60
    sportlased_tulemused = list(zip(sportlased, tulemused))
    for i in range(len(sportlased_tulemused)):
        nimi, tulemus = sportlased_tulemused[i]
        print(nimi, ":", tulemus)
    print("------------------------")
    uus_list = []
    for nimi, tulemus in sportlased_tulemused:  
        if tulemus >= res:
            uus_list.append((nimi, tulemus))
    for nimi, tulemus in uus_list:  
        print(nimi, ":", tulemus)


#Узнать n худших результатов.
def valik5(valik: int, sportlased: list, tulemused: list)->any:
    """Funktsioon tunnistab n halvemat tulemust ja väljastab need koos sportlaste nimedega.
    Kasutaja sisestab soovitud halvimate tulemuste arvu ning funktsioon sorteerib tulemused
    :param int valik: funktsiooni valiku number
    :param list sportlased: Sportlaste nimede loend
    :param list tulemused: Sportlaste tulemuste loend
    :return: None
    """
    i=0
    kogus=int(input("Sisestage halvimate tulemuste arv: "))
    tulemused.sort()
    print(f"Top {kogus} halvimad tulemused")
    for tulemus in tulemused:
        if i>=kogus:
            break
        j=tulemused.index(tulemus)
        nimi=sportlased[j]
        print(f"{nimi} : {tulemus}")
        i+=1

