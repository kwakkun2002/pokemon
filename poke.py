import sys,time,random

class Setting():

    def __init__(self,name,hp,type,acu,skill_a_name,skill_a_damage,skill_a_type,skill_b_name,skill_b_damage,skill_b_type):
        self.name = name
        self.hp = hp
        self.type = type
        self.acu = acu
        self.skill_a_name = skill_a_name
        self.skill_a_damage = skill_a_damage
        self.skill_a_type=skill_a_type
        self.skill_b_name = skill_b_name
        self.skill_b_damage = skill_b_damage
        self.skill_b_type=skill_b_type

    def acu_choice(self):
        if random.randrange(1,100)<=self.acu:
            return True
        else:
            print("명중하지 못했다!")

    def skill_a(self,enemy):
        if self.acu_choice() is True:
            if self.skill_a_type is "일반":
                print(self.skill_a_name+"을 시전했다!")
                enemy.hp-=self.skill_a_damage
                enemy.life_confirm()

    def skill_b(self,enemy):
        if self.acu_choice() is True:
            if self.skill_b_type is "일반":
                print(self.skill_b_name + "을 시전했다!")
                enemy.hp -= self.skill_b_damage
                enemy.life_confirm()

    def life_confirm(self):
        if self.hp<=0:
            print(self.name + "은 죽었다")
            time.sleep(3)
            sys.exit()








class Pika(Setting):
    def __init__(self):
        super().__init__("피카츄",300,"전기",50,"10만볼트",100,"전기","몸통박치기",50,"일반")

class Ingoking(Setting):
    def __init__(self):
        super().__init__("잉어킹",10,"일반",50,"튀어오르기",0,"특수공격","없음",0,"없음")
    def skill_a(self):
        super().acu_choice() is True:
            print(self.skill_a_name+"을 시전했다!")
            print(self.name+"은 튀어올랐다!!엄청 높이 튀어올랐다!")

class Lichu(Setting):
    def __init__(self):
        super().__init__("라이츄",200,"전기",50,"100만볼트",200,"전기","돌진",60,"일반")

class Cobugi(Setting):
    def __init__(self):
        super().__init__("꼬부기",400,"물",50,"하이드로 펌프",50,"물","비눗방울",0,"특수공격")
    def skill_b(self,enemy):
        super().acu_choice() is True:
            print(self.skill_b_name + "을 시전했다!")
            enemy.acu/=2
            print("명중률이 절반이 되었다!")

class Pairi(Setting):
    def __init__(self):
        self.name="파이리"
        self.hp=350
        self.type="불"
        self.acu=50
        self.skill_a_name = "불대문자"
        self.skill_a_damage = 150
        self.skill_b_name = "깨물기"
        self.skill_b_damage = 70

class Jamanbo(Setting):
    def __init__(self):
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
        enemy.life()
















