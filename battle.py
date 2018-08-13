import poke as pk
import random
import sys
import time
import os

class player:
    def __init__(self):
        self.pokemon=pk.Pika()
        self.name=''

def clear():
    for i in range(100):
        print("\n")

player=player()
player.name=input("이름이나 입력하셈:")
print("3번 싸워서 이기면 게임끝남ㅅㄱ")
print("너의 포켓몬은 피카츄다")

count=0
round=0
turn=0

continue_skill_list=[]

while count is not 3:
    enemy=pk.Tanguri()
    while True:
        round+=1
        turn='player'
        choice=input("무엇을 하시겠습니까? 1은 "+player.pokemon.skill_list[0]+"2는 "+player.pokemon.skill_list[1])
        if choice is '1':
            player.pokemon.skill_1(enemy)
            if enemy.life_confirm() is True:
                count+=1
                print("상대가 쓰러졌다")
                break
            else:
                print("상대에게 hp "+str(enemy.hp)+"이가 남았다!")
                break
        elif choice is '2':
            player.pokemon.skill_2(enemy)
            if enemy.life_confirm() is True:
                count+=1
                break
            else:
                print("상대에게 hp "+str(enemy.hp)+"이가 남았다!")
                break
        else:
            print("다시 입력해 주세요")
            continue
    while True:
        round+=1
        turn="enemy"
        a=random.choice(range(len(enemy.skill_list)))
        if a is 0:
            enemy.skill_1(player.pokemon)
            if player.pokemon.life_confirm() is True:
                print("그만해 다 끝났어")
                time.sleep(3)
                sys.exit()
            else:
                print("나에게 hp "+str(enemy.hp)+"이가 남았다!")
                break
        elif a is 1:
            enemy.skill_2(player.pokemon)
            if player.pokemon.life_confirm() is True:
                print("그만해 다 끝났어")
                time.sleep(3)
                sys.exit()
            else:
                print("나에게 hp"+str(enemy.hp)+"이가 남았다!")
                break
    time.sleep(3)
    clear()





































