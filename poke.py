import sys,time,random
import skill

class Setting():

    def __init__(self,name,hp,type,acu):
        self.name = name
        self.hp = hp
        self.type = type
        self.acu = acu
        self.skill=[]
    def life_confirm(self):
        if self.hp<=0:
            print(self.name + "은 죽었다")
            time.sleep(3)
            sys.exit()


'''"10만볼트",100,"전기","몸통박치기",50,"노말"'''

class Pika(Setting):
    def __init__(self):
        super().__init__("피카츄",300,"전기",50)




'''class Ingoking(Setting):
    def __init__(self):
        super().__init__("잉어킹",10,"노말",50,"튀어오르기",0,"특수공격","없음",0,"없음")
    def skill_a(self):
        if self.acu_choice() is True:
            print(self.skill_a_name+"을 시전했다!")
            print(self.name+"은 튀어올랐다!!엄청 높이 튀어올랐다!")

class Lichu(Setting):
    def __init__(self):
        super().__init__("라이츄",200,"전기",50,"100만볼트",200,"전기","돌진",60,"")

class Cobugi(Setting):
    def __init__(self):
        super().__init__("꼬부기",400,"물",50,"하이드로 펌프",50,"물","비눗방울",0,"특수공격")
    def skill_b(self,enemy):
        if self.acu_choice() is True:
            print(self.skill_b_name + "을 시전했다!")
            enemy.acu/=2
            print("명중률이 절반이 되었다!")

class Pairi(Setting):
    def __init__(self):
        super().__init__("파이리",350,"불",50,"불대문자",150,"불","깨물기",70,"노말")

class Jamanbo(Setting):
    def __init__(self):
        super().__init__("잠만보",1000,"노말",50,"단단해지기",0,"노말","몸통박치기",50,"노말")
        self.name="잠만보"
        self.hp=1000
        self.type="노말"
        self.acu=50
        self.skill_a_name = "단단해지기"
        self.skill_b_name = "몸통박치기"
        self.skill_b_damage = 50
    def skill_a(self,enemy):
        print(self.skill_a_name+"을 시전했다!")
        self.hp+=50
        print("체력이 +50되었다!")

class Gorapaduck(Setting):
    def __init__(self):
        self.name="고라파덕"
        self.hp=200
        self.type="물"
        self.acu=50
        self.skill_a_name = "싫은소리"
        self.skill_b_name = "하이드로펌프"
        self.skill_b_damage = 50
    def skill_a(self,enemy):
        print(self.skill_a_name+"을 시전했다!")
        enemy.acu=0
        print(" 명중률이 0이 되었다!")

class Gilpagi(Setting):
    def __init__(self):
        self.name="질퍼기"
        self.hp=100
        self.type="독"
        self.acu=50
        self.skill_a_name = "트림"
        self.skill_a_damage = 30
        self.skill_b_name = "오물웨이브"
    def skill_a(self,enemy):
        print(self.skill_a_name+"을 시전했다!")
        enemy.hp-=self.skill_a_damage
        self.skill_a_damage+=self.skill_a_damage
        enemy.life()
    def skill_b(self,enemy):
        print(self.skill_b_name + "을 시전했다!")
        enemy.hp -= enemy.hp/2
        enemy.life()

class Tanguri(Setting):
    def __init__(self):
        self.name="탕구리"
        self.hp=350
        self.type="격투"
        self.acu=50
        self.skill_a_name = "지구던지기"
        self.skill_a_damage = 2000
        self.skill_b_name = "기모으기"
        self.skill_b_count=0
    def skill_a(self,enemy):
            if self.skill_b_count != 3:
                print(self.skill_a_name+"을 시전하려고 했으나 기를 3번 모아야한다!")
            else:
                enemy.hp-=self.skill_a_damage
                enemy.life()
    def skill_b(self,enemy):
        print(self.skill_b_name + "을 시전했다!")
        self.skill_b_count+=1
        enemy.life()'''

print("what is going on?")













