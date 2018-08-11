import poke as pk

class player:
    def __init__(self):
        self.pokemon=pk.Pika()
        self.name=''



player=player()
player.name=input("이름이나 입력하셈:")
print("3번 싸워서 이기면 게임끝남ㅅㄱ")

count=0
while count is not 3:
    enemy=pk.Jamanbo()
    # print(enemy.name+"이 나타났다!")
    choice=input("무엇을 하시겠습니까? 1은 "+player.pokemon.skill_list[0]+"2는 "+player.pokemon.skill_list[1])
    if choice is '1':
        player.pokemon.skill_1(enemy)
    elif choice is '2':
        player.pokemon.skill_2(enemy)
    else:


































