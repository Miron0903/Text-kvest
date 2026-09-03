from random import *
from time import *
import winsound
from pictures import *
def predhistory():
    b = 0
    c = -1
    d = 3
    e = ['вы видете беззаботно выпригивающих дельфинов', 'вам открываются прекасные виды, море постирается до самого горизонта', 'вы видите огромный риф, с которого стекает огромный водопад']
    print("Вы плывёте по морю на красивом корабле...")
    sleep(3)
    print("Вы прогуливаетесь по палубе и вдруг замечаете что у штурвала никого нет")
    sleep(2)
    a = input('Вы никогда не пробовали управлять кораблём, хотите попробовать?\n')
    if (a == 'нет'):
        sleep(2)
        winsound.PlaySound("grom.wav", winsound.SND_ASYNC)
        print('вдруг небо темнеет, начинается шторм, вы молниеносно хватаетесь за штурвал, ')
        groza()
    while True:
        b = randint(1, 10)
        a = ''
        c = -1
        while (a != 'направо' and a != 'налево'):
            c += 1
            if (c > 0):
                print('не понял ваш ответ, повторите пожалуйста')
                sleep(1)
            a = input('куда повернём?\n')
            sleep(2)
        if (a == 'направо'):
            d += 1
            if (d != 5):
                print('вы повернули направо,', e[d - 2])
            else:
                break
        else:
            d -= 1
            if (d != 1):
                print('вы повернули налево,', e[d - 2])
            else:
                break
    winsound.PlaySound("predhist.wav", winsound.SND_ASYNC)
    print('Вы налетели на скалы и от удара потеряли сознание. Вы очутились на острове.')
    island()
    sleep(3)
    bereg()
def bereg():
    ret = 0
    while (ret == 0):
        print('слева вы видите пляж, а справа - вход в пещеру')
        a = input('Куда пойдём (1 - пляж, 2 - пещера)\n')
        if (a == '1'):
            plash()
        elif (a == '2'):
            cave()
        else:
            print('Вы легли на землю и отдыхаете')
            sleep(3)
            print('отдохнув, вы поднялись')
            sleep(2)
def plash():
    ret = 0
    beach()
    while (ret == 0):
        print('вы на пляже')
        a = input('1 - порыбачить, \n2 - порыться в песке, \n3 - заглянуть в кусты, \n4 - вернуться к месту крушения, \n5 - полежать на песке\n')
        if (a == '1'):
            if (inventory['yd'] == 0):
                print('у вас нет удочки')
            else:
                print('вы забросили крючок в море')
                sleep(randint(3, 6))
                if (randint(1, 4) == 1) and (inventory['key'] == 0):
                    inventory['key'] = 1
                    print('Ура! вы вытощили ключ!')
                    sleep(1)
                elif (randint(1, 3) == 1) and (inventory['key'] == 1):
                    print('вы поймали рыбу и съели её')
                    sleep(2)
                else:
                    print('вы ничего не поймали')
                    sleep(2)
        elif (a == '2'):
            print('вы роетесь в песке')
            sleep(randint(3, 6))
            if (randint(1, 4) == 1) and (inventory['TNT'] == 0):
                inventory['TNT'] = 1
                print('Ух-ты! вы выкопали динамит!')
                sleep(1)
            elif (randint(1, 3) == 1):
                print('вы выкопали птичью какашку')
                sleep(2)
                print('вы испачкали руки, и бросились мыть их в море')
                sleep(2)
            else:
                print('вы ничего не выкопали и очень устали')
                sleep(2)
        elif (a == '3'):
            print('вы заглянули в кусты')
            sleep(randint(3, 6))
            if (randint(1, 3) == 1) and (inventory['yd'] == 0):
                inventory['yd'] = 1
                print('Здорово! вы нашли удочку!')
                sleep(1)
            elif (randint(1, 3) == 1):
                print('вы нашли чей-то скелет')
                sleep(2)
                print('вы очень испугались, и бросились обратно на пляж')
                sleep(2)
            else:
                print('в кустах ничего нету')
                sleep(2)
        elif (a == '4'):
            ret = 1
        else:
            winsound.PlaySound("sea.wav", winsound.SND_ASYNC)
            print('вы улеглись на песок')
            sleep(randint(3, 6))
            if (randint(1, 2) == 1):
                print('Ой! меня кто-то укусил за попу... это краб!')
                sleep(3)
            elif (randint(1, 2) == 1):
                print('Ай! что-это выполо из птички на меня')
                sleep(2)
                print('скорее мыться')
                sleep(2)
            else:
                print('отдохнув вы встали')
                sleep(2)
def cave():
    ret = 0
    while (ret == 0):
        print('вы в пещере, но впереди чудовище, боюсь пройти дальше')
        a = input('1 - убить монстра, \n2 - прокрасться мимо монстра, \n3 - спеть песню, \n4 - вернуться к месту крушения, \n5 - постоять подумать\n')
        if (a == '1'):
            if (inventory['TNT'] == 0):
                print('это рисованно, у вас нет оружия, вы передумали')
            else:
                print('вы бросили в монстра динамит')
                inventory['TNT'] = 0
                sleep(randint(3, 4))
                if (randint(1, 4) == 1):
                    print('Ой! вы забыли поджечь фитиль')
                    sleep(1)
                elif (randint(1, 2) == 1):
                    winsound.PlaySound("obval.wav", winsound.SND_ASYNC)
                    print('вы попали монстра и он оглушен, вы прошли мимо него')
                    sleep(2)
                    cave_2()
                else:
                    winsound.PlaySound("obval.wav", winsound.SND_ASYNC)
                    print('вы промахнулись и с потолка посыпались камни, придётся искать динамит снова')
                    sleep(2)
        elif (a == '2'):
            print('вы тихонечко крадётесь мимо монстра')
            winsound.PlaySound("step.wav", winsound.SND_ASYNC)
            sleep(randint(3, 6))
            if (randint(1, 2) == 1):
                print('монстр спал и не заметил вас')
                sleep(1)
                cave_2()
            else:
                inventory['z'] -= 1
                winsound.PlaySound("babax.wav", winsound.SND_ASYNC)
                print('монстр заметил вас и нанёс удар, жизней стало', inventory['z'])
                sleep(2)
                if (inventory['z'] == 0):
                    bad_end()
        elif (a == '3'):
            print('вы поёте песню')
            sleep(randint(3, 6))
            if (randint(1, 3) == 1):
                print('Монстр заснул и вы прошли мимо него')
                sleep(2)
                cave_2()
            elif (randint(1, 3) == 1):
                inventory['z'] -= 1
                winsound.PlaySound("babax.wav", winsound.SND_ASYNC)
                print('монстру непонравилась ваша песня и он нанёс удар, жизней стало', inventory['z'])
                sleep(2)
                if (inventory['z'] == 0):
                    bad_end()
            else:
                print('вы допели песню и очень довольны собой')
                winsound.PlaySound("song.wav", winsound.SND_ASYNC)
                sleep(2)
        elif (a == '4'):
            ret = 1
        else:
            print('вы стоите и думаете')
            sleep(randint(3, 6))
            if (randint(1, 2) == 1):
                print('Ой! меня кто-то укусил за ухо... это летучая мышь!')
                sleep(3)
            elif (randint(1, 2) == 1):
                print('Фу! что-за запах')
                sleep(2)
                print('может выйти из пещеры?')
                sleep(2)
            else:
                print('хорошенько подумав, вы...')
                sleep(2)
def cave_2():
    ret = 0
    while (ret == 0):
        print('вы в глубине пещеры, виден сундук и ход дальше')
        a = input('1 - открыть сундук, \n2 - идти дальше, \n3 - заглянуть под камень, \n4 - вернуться назад, \n5 - посидеть на камне\n')
        if (a == '1'):
            print('вы пытаетесь открыть сундук')
            sleep(2)
            if (inventory['key'] == 0):
                print('у вас нет ключа, может поискать его на пляже...')
            else:
                print('Ура! сундук открылся')
                sleep(2)
                if (inventory['map'] == 1):
                    print('но он пуст, карта уже у вас')
                    sleep(2)
                else:
                    inventory['map'] = 1
                    sleep(randint(3, 6))
                    print('в нём карта пещеры, можно попытаться идти дальше')
                    sleep(2)
        elif (a == '2'):
            if (inventory['map'] == 0):
                print('у вас нет карты, вы поплутали и вернулись обратно')
                sleep(randint(3, 6))
            else:
                winsound.PlaySound("cave.wav", winsound.SND_ASYNC)
                print('вы бредёте по коридорам поглядывая карту...')
                sleep(5)
                print('Чувствуется приток свежего воздуха...')
                sleep(2)
                print('вы выходите из пещеры в потайную бухту')
                sleep(2)
                byxta()
        elif (a == '3'):
            print('там пусто')
            sleep(2)
        elif (a == '4'):
            ret = 1
        else:
            print('вы сели на камень')
            sleep(randint(3, 6))
            if (randint(1, 2) == 1):
                print('Ой! меня кто-то укусил за пятку... это пещерная мышь!')
                sleep(3)
            elif (randint(1, 2) == 1):
                print('Ай! что-это капнуло с потолка на меня')
                sleep(2)
                print('фух, водичка... попью...')
                sleep(2)
            else:
                print('отдохнув вы встали')
                sleep(2)
def byxta():
    ret = 0
    byx()
    while (ret == 0):
        print('вы в бухте на берегу моря, на волнах качается катер, рядом на песке: сокровища, топливо и еда')
        a = input('1 - взять сокровища, \n2 - взять топливо, \n3 - взять еду, \n4 - вернуться в пещеру, \n5 - залезть на катер\n')
        if (a == '1'):
            inventory['tres'] = 1
            print('вы подняли сокровища')
            sleep(2)
        elif (a == '2'):
            inventory['benz'] = 1
            print('вы подняли топливо')
            sleep(2)
        elif (a == '3'):
            inventory['eat'] = 1
            print('вы подняли еду')
            sleep(2)
        elif (a == '4'):
            print('вход в пещеру завален, туда невернуться')
        else:
            print('вы лезите на катер')
            sleep(2)
            if (inventory['tres'] + inventory['benz'] + inventory['eat'] == 3):
                print('вы взяли сокровища, топливо и еду, слишком тяжело, катер сидит на мели')
                sleep(2)
                print('вы расстроились и выбросили всё обратно')
                sleep(2)
            elif (inventory['tres'] + inventory['benz'] + inventory['eat'] == 2):
                if (inventory['eat'] == 0):
                    print('у вас нет еды, вероятность выжить 20%')
                    sleep(2)
                    print('1 - попытаться уплыть, \n2 - выбросить всё на берег')
                    a = input()
                    if (a == '1'):
                        if (randint(1, 5) == 1):
                            win()
                        else:
                            bad_end()
                    else:
                        print('вы расстроились и выбросили всё обратно')
                        sleep(2)
                elif (inventory['benz'] == 0):
                    print('у вас нет топлива, вы неможете плыть')
                    sleep(2)
                    print('вы расстроились и выбросили всё обратно')
                    sleep(2)
                else:
                    win()
            else:
                if (inventory['eat'] == 1):
                    print('у вас нет топлива, вы неможете плыть')
                    sleep(2)
                    print('вы расстроились и выбросили всё обратно')
                    sleep(2)
                if (inventory['benz'] == 1):
                    print('у вас нет еды, вероятность выжить 20%')
                    sleep(2)
                    print('1 - попытаться уплыть, \n2 - выбросить всё на берег')
                    a = input()
                    if (a == '1'):
                        if (randint(1, 5) == 1):
                            win()
                        else:
                            bad_end()
                    else:
                        print('вы расстроились и выбросили всё обратно')
                        sleep(2)
def bad_end():
    winsound.PlaySound("proig.wav", winsound.SND_ASYNC)
    print('вы умерли')
    sleep(10)
    exit()
def win():
    winsound.PlaySound("win.wav", winsound.SND_ASYNC)
    print('Ура! победа, вы вернулись домой')
    sleep(3)
    if (inventory['tres'] == 1):
        print('да ещё и с сокровищами! вы богаты!')
    sleep(10)
    exit()
global inventory
inventory = {'z' : 3, 'key' : 0, 'map' : 0, 'TNT' : 0, 'yd' : 0, 'benz' : 0, 'eat' : 0, 'tres' : 0}
sleep(1)
predhistory()
