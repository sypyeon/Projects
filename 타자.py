twoletterwords = ['책상','바지','머리','게임','연필','볼펜','지폐','동상','물병','잠옷','상의','기차','수리','정비','직업','과자','맥주','음료','알약','식당','침대','이불']
#this will be gamemode no.1

threeletterwords = ['자동차','비행기','컴퓨터','게임기','지우개','짜장면','마우스','키보드','피규어','화장품','가로등','갈매기','나무꾼','닌텐도','라디오','마스크','코로나','아저씨','쓰레기','자전거','알감자','고구마']
#this will be gamemode no.2


import random

def gamemode1():
    score = 0
    while score != 10:
        randomword = random.randint(0,len(twoletterwords)-1)
        print(twoletterwords[randomword])
        answer = input()
        if answer == (twoletterwords[randomword]):
            score += 1
            print('score = ', score)
        elif answer != (twoletterwords[randomword]):
            score -= 0
            print('score = ', score)
    if score == 10:
        print('good job!')

def gamemode2():
    score = 0
    while score != 10:
        randomword = random.randint(0,len(threeletterwords)-1)
        print(threeletterwords[randomword])
        answer = input()
        if answer == (threeletterwords[randomword]):
            score += 1
            print('score = ', score)
        elif answer != (threeletterwords[randomword]):
            score -= 0
            print('score = ', score)
    if score == 10:
        print('good job!')
    

gamemode = input('press enter to start')
while gamemode != 2 or 3:
    gamemode = int(input('input number 2 or 3'))

    if gamemode == 2:
        gamemode1()

    elif gamemode == 3:
        gamemode2()

