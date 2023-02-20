from typing import Annotated
from playsound import playsound
import winsound
from graphics import*
from random import randint
import time

#create a window
win = GraphWin("OverMatch",1200,1000)

#my variables
player_maxhp = 4
playing=1
LifeSteal=0
Attack=0

#my images
mainscreen = Image(Point(600,524),"mainscreen.gif")
button = Image(Point(600,624),"button.gif")
tutorial = Image(Point(600,500),"tutorial.gif")
background1=Image(Point(600,500),"battle1.gif")
background2=Image(Point(600,500),"battle2.gif")
background3=Image(Point(600,500),"battle3.gif")
GameOver=Image(Point(600,500),"game over.gif")
win_game=Image(Point(600,500),"win.gif")
reward1=Image(Point(600,500),"Reward1.gif")
reward2=Image(Point(600,500),"Reward2.gif")
info=Image(Point(600,500),"info.gif")
back1 = Image(Point(600,900),"cardback.gif")
back2 = Image(Point(600,100),"cardbacko.gif")
cardA = Image(Point(600,700),"0.gif")
cardB=Image(Point(600,700),"1000.gif")
cardC=Image(Point(600,700),"1500.gif")
cardD=Image(Point(600,700),"2000.gif")
cardE=Image(Point(600,700),"2500.gif")
cardF=Image(Point(600,700),"3000.gif")
cardS1=Image(Point(600,700),"GF.gif")
cardS2=Image(Point(600,700),"ikaros.gif")
cardS3=Image(Point(600,700),"Paarthurnax.gif")
boss_cardA=Image(Point(600,300),"0r.gif")
boss_cardB=Image(Point(600,300),"1000r.gif")
boss_cardC=Image(Point(600,300),"1500r.gif")
boss_cardD=Image(Point(600,300),"2000r.gif")
boss_cardE=Image(Point(600,300),"2500r.gif")
boss_cardF=Image(Point(600,300),"BEyes.gif")
boss_cardGs=Image(Point(600,300),"Theworld.gif")
boss_cardHs=Image(Point(600,300),"BiteTheDust.gif")

#decks
player_deck = [cardA,cardB,cardC,cardD,cardE,cardF]
dio_deck = [boss_cardA,boss_cardB,boss_cardC,boss_cardD,boss_cardE,boss_cardF,boss_cardGs]
kili_deck = [boss_cardB,boss_cardC,boss_cardD,boss_cardE,boss_cardF,boss_cardHs]
pucci_deck = [boss_cardC,boss_cardD,boss_cardE,boss_cardF,boss_cardGs,boss_cardHs]

#functions that I made
def Start_Screen():
    winsound.PlaySound("Music.wav",winsound.SND_ASYNC|winsound.SND_LOOP)
    mainscreen.draw(win)
    button.draw(win)
    
def Continue():
    while True:
        mouseclick = win.getMouse()
        if mouseclick.getX()>450 and mouseclick.getX()<750 and mouseclick.getY()>484 and mouseclick.getY()<600:
            mainscreen.undraw()
            button.undraw()
            winsound.PlaySound(None,winsound.SND_PURGE)
            play=1
            return play
        elif mouseclick.getX()>450 and mouseclick.getX()<750 and mouseclick.getY()>645 and mouseclick.getY()<765:
            play=0
            return play
        elif mouseclick.getX()>887 and mouseclick.getX()<1167 and mouseclick.getY()>28 and mouseclick.getY()<111:
            info.draw(win)
            win.getMouse()
            info.undraw()


def Tutorial():
    tutorial.draw(win)
    while True:
        mouseclick=win.getMouse()
        if mouseclick.getX()>297 and mouseclick.getX()<650 and mouseclick.getY()>780 and mouseclick.getY()<905:
            tutorial.undraw()
            break

def Boss_Fight_1():
    winsound.PlaySound("duel.wav",winsound.SND_ASYNC|winsound.SND_LOOP)
    background1.draw(win)

def Boss_Fight_2():
    winsound.PlaySound("duel.wav",winsound.SND_ASYNC|winsound.SND_LOOP)
    background2.draw(win)

def Battle1():
    dio_hp=3
    dio_ability=1
    player_hp=player_maxhp
    while dio_hp>0 and player_hp>0:
        player_health = Text(Point(320.5,928),str(player_hp)+"hp")
        Boss_health = Text(Point(887.5,56),str(dio_hp)+"hp")
        back1.draw(win)
        back2.draw(win)
        Boss_health.draw(win)
        player_health.draw(win)
        while back1.anchor.getY()!=700 and back2.anchor.getY()!=300:
            time.sleep(0.05)
            back1.move(0,-10)
            back2.move(0,10)
        win.getMouse()
        back1.undraw()
        back2.undraw()
        p_card=randint(0,5)
        b_card=randint(0,5)
        if dio_hp<2 and dio_ability==1:
            time.sleep(0.05)
            dio_deck[6].draw(win)
            player_deck[p_card].draw(win)
            dio_hp=dio_hp+1
            player_hp=player_hp-1
            dio_ability=0
            time.sleep(2)
            dio_deck[6].undraw()
            player_deck[p_card].undraw()
            Boss_health.undraw()
            player_health.undraw()
        else:
            time.sleep(0.05)
            dio_deck[b_card].draw(win)
            player_deck[p_card].draw(win)
            if b_card>p_card:
                player_hp=player_hp-1
                time.sleep(2)
                dio_deck[b_card].undraw()
                player_deck[p_card].undraw()
                Boss_health.undraw()
                player_health.undraw()
            elif b_card<p_card:
                dio_hp=dio_hp-1
                time.sleep(2)
                dio_deck[b_card].undraw()
                player_deck[p_card].undraw()
                Boss_health.undraw()
                player_health.undraw()
            else:
                time.sleep(2)
                dio_deck[b_card].undraw()
                player_deck[p_card].undraw()
                Boss_health.undraw()
                player_health.undraw()
        if dio_hp<1:
            result=1
            background1.undraw()
            return result
        elif player_hp<1:
            result=0
            background1.undraw()
            return result

def Battle2():
    back1 = Image(Point(600,900),"cardback.gif")
    back2 = Image(Point(600,100),"cardbacko.gif")
    kili_hp=4
    kili_ability=1
    player_hp=player_maxhp
    player_ability=1
    wincon=0
    while kili_hp>0 and player_hp>0:
        player_health = Text(Point(361,929),str(player_hp)+"hp")
        Boss_health = Text(Point(835,69),str(kili_hp)+"hp")
        back1.draw(win)
        back2.draw(win)
        Boss_health.draw(win)
        player_health.draw(win)
        while back1.anchor.getY()!=700 and back2.anchor.getY()!=300:
            time.sleep(0.05)
            back1.move(0,-10)
            back2.move(0,10)
        win.getMouse()
        back1.undraw()
        back2.undraw()
        p_card=randint(0,5)
        b_card=randint(0,4)
        if player_hp<2 and player_ability==1:
            if Effect==1:
                time.sleep(0.1)
                kili_deck[b_card].draw(win)
                cardS1.draw(win)
                kili_hp=kili_hp-2
                player_ability=0
                time.sleep(2)
                kili_deck[b_card].undraw()
                cardS1.undraw()
                Boss_health.undraw()
                player_health.undraw()
            elif Effect==2 and wincon==3:
                time.sleep(0.1)
                kili_deck[b_card].draw(win)
                cardS2.draw(win)
                kili_hp=0
                time.sleep(2)
                kili_deck[b_card].undraw()
                cardS2.undraw()
                Boss_health.undraw()
                player_health.undraw()
            else:
                time.sleep(0.1)
                kili_deck[b_card].draw(win)
                cardS3.draw(win)
                player_hp=player_hp+2
                player_ability=0
                time.sleep(2)
                kili_deck[b_card].undraw()
                cardS3.undraw()
                Boss_health.undraw()
                player_health.undraw()
        elif kili_hp<2 and kili_ability==1:
            time.sleep(0.1)
            kili_deck[5].draw(win)
            player_deck[p_card].draw(win)
            kili_hp=4
            player_hp=player_maxhp
            kili_ability=0
            time.sleep(2)
            kili_deck[5].undraw()
            player_deck[p_card].undraw()
            Boss_health.undraw()
            player_health.undraw()
        else:
            time.sleep(0.1)
            kili_deck[b_card].draw(win)
            player_deck[p_card].draw(win)
            if b_card+1>p_card:
                player_hp=player_hp-1
                time.sleep(2)
                kili_deck[b_card].undraw()
                player_deck[p_card].undraw()
                Boss_health.undraw()
                player_health.undraw()
                wincon=wincon+1
            elif b_card+1<p_card:
                kili_hp=kili_hp-1
                wincon=0
                time.sleep(2)
                kili_deck[b_card].undraw()
                player_deck[p_card].undraw()
                Boss_health.undraw()
                player_health.undraw()
            else:
                time.sleep(2)
                kili_deck[b_card].undraw()
                player_deck[p_card].undraw()
                Boss_health.undraw()
                player_health.undraw()
        if kili_hp<1:
            result=1
            background2.undraw()
            return result
        elif player_hp<1:
            result=0
            background2.undraw()
            return result

def Reward_Screen_1():
    reward1.draw(win)
    while True:
        mouseclick=win.getMouse()
        if mouseclick.getX()>63 and mouseclick.getX()<316 and mouseclick.getY()>310 and mouseclick.getY()<687:
            reward1.undraw()
            Effect_card=1
            return Effect_card
        elif mouseclick.getX()>489 and mouseclick.getX()<741 and mouseclick.getY()>225 and mouseclick.getY()<597:
            reward1.undraw()
            Effect_card=2
            return Effect_card
        elif mouseclick.getX()>875 and mouseclick.getX()<1131 and mouseclick.getY()>310 and mouseclick.getY()<687:
            reward1.undraw()
            Effect_card=3
            return Effect_card

def Reward_Screen_2():
    reward2.draw(win)
    while True:
        mouseclick=win.getMouse()
        if mouseclick.getX()>79 and mouseclick.getX()<298 and mouseclick.getY()>461 and mouseclick.getY()<747:
            reward2.undraw()
            Effect=1
            return Effect
        elif mouseclick.getX()>496 and mouseclick.getX()<687 and mouseclick.getY()>325 and mouseclick.getY()<663:
            reward2.undraw()
            Effect=2
            return Effect
        elif mouseclick.getX()>891 and mouseclick.getX()<1112 and mouseclick.getY()>410 and mouseclick.getY()<762:
            reward2.undraw()
            Effect=3
            return Effect

def Again():
    winsound.PlaySound(None,winsound.SND_PURGE)
    GameOver.draw(win)
    while True:
        mouseclick=win.getMouse()
        if mouseclick.getX()>259 and mouseclick.getX()<403 and mouseclick.getY()>840 and mouseclick.getY()<906:
            play=1
            GameOver.undraw()
            return play
        elif mouseclick.getX()>793 and mouseclick.getX()<908 and mouseclick.getY()>840 and mouseclick.getY()<906:
            play=0
            GameOver.undraw()
            return play

def Next_Stage():
    winsound.PlaySound(None,winsound.SND_PURGE)
    win_game.draw(win)
    while True:
        mouseclick=win.getMouse()
        if mouseclick.getX()>465 and mouseclick.getX()<716 and mouseclick.getY()>562 and mouseclick.getY()<655:
            win_game.undraw()
            break

#The real game
while playing==1:
    while True:
        Start_Screen()
        play=Continue()
        if play==0:
            playing=0
            break
        Tutorial()
        Boss_Fight_1()
        result=Battle1()
        if result==0:
            playing=Again()
            break
        Next_Stage()
        Effect=Reward_Screen_1()
        Boss_Fight_2()
        result=Battle2()
        if result==0:
            playing=Again()
            break
        Next_Stage()
        Effect2=Reward_Screen_2()
        if Effect2==1:
            LifeSteal=1
        elif Effect2==2:
            player_maxhp=player_maxhp+2
        else:
            Attack=1
        Boss_Fight_3()
        result=Battle3