import sys,time

class Pika():
    def __init__(self):
        self.name="피카츄"
        self.hp=300
        self.type="전기"
        self.acu=50
        self.skill_a_name = "10만볼트"
        self.skill_a_damage = 100
        self.skill_b_name = "몸통박치기"
        self.skill_b_damage = 50
    def skill_a(self,enemy):
        print(self.skill_a_name+"을 시전했다!")
        enemy.hp-=self.skill_a_damage
        enemy.life()
    def skill_b(self,enemy):
        print(self.skill_b_name + "을 시전했다!")
        enemy.hp -= self.skill_b_damage
        enemy.life()
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()

class Ingoking():
    def __init__(self):
        self.name="잉어킹"
        self.hp=10
        self.type="잉여"
        self.acu=50
        self.skill_a_name = "튀어오르기"
    def skill_a(self):
        print(self.skill_a_name+"을 시전했다!")
        print(self.name+"은 튀어올랐다!!엄청 높이 뛰어올랐다!")
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()

class Lichu():
    def __init__(self):
        self.name="라이츄"
        self.hp=200
        self.type="전기"
        self.acu=50
        self.skill_a_name = "100만볼트"
        self.skill_a_damage = 200
        self.skill_b_name = "돌진"
        self.skill_b_damage = 60
    def skill_a(self,enemy):
        print(self.skill_a_name+"을 시전했다!")
        enemy.hp-=self.skill_a_damage
        enemy.life()
    def skill_b(self,enemy):
        print(self.skill_b_name + "을 시전했다!")
        enemy.hp -= self.skill_b_damage
        enemy.life()
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()

class Cobugi():
    def __init__(self):
        self.name="꼬부기"
        self.hp=400
        self.type="물"
        self.acu=50
        self.skill_a_name = "하이드로 펌프"
        self.skill_a_damage = 50
        self.skill_b_name = "비눗방울"
    def skill_a(self,enemy):
        print(self.skill_a_name+"을 시전했다!")
        enemy.hp-=self.skill_a_damage
        enemy.life()
    def skill_b(self,enemy):
        print(self.skill_b_name + "을 시전했다!")
        enemy.acu/=2
        print("명중률이 절반이 되었다!")
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()

class Pairi():
    def __init__(self):
        self.name="파이리"
        self.hp=350
        self.type="불"
        self.acu=50
        self.skill_a_name = "불대문자"
        self.skill_a_damage = 150
        self.skill_b_name = "깨물기"
        self.skill_b_damage = 70
    def skill_a(self,enemy):
        print(self.skill_a_name+"을 시전했다!")
        enemy.hp-=self.skill_a_damage
        enemy.life()
    def skill_b(self,enemy):
        print(self.skill_b_name + "을 시전했다!")
        enemy.hp -= self.skill_b_damage
        enemy.life()
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()

class jamanbo():
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
    def skill_b(self,enemy):
        print(self.skill_b_name + "을 시전했다!")
        enemy.hp -= self.skill_b_damage
        enemy.life()
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()

class gorapaduck():
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
    def skill_b(self,enemy):
        print(self.skill_b_name + "을 시전했다!")
        enemy.hp -= self.skill_b_damage
        enemy.life()
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()

class gilpagi():
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
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()

class tanguri():
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
    def dead(self):
        print(self.name+"은 죽었다")
        time.sleep(3)
        sys.exit()
    def life(self):
        if self.hp<=0:
            self.dead()
















