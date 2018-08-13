import sys,random

class Skill():
    def __init__(self,skill_name,skill_damage,skill_type):
        self.skill_name=skill_name
        self.skill_damage=skill_damage
        self.skill_type=skill_type
        self.skill_ability="일반"
    def acu_choice(self):
        if random.randrange(1, 101) <= self.acu:
            return True
    def skill(self,enemy):
        if self.acu_choice() is True:
            print(self.skill_name+"을 시전했다!")
            enemy.hp-=self.skill_damage
            enemy.life_confirm()
        else:
            print(self.skill_name+"는 실패했다!")

class SpecialSkill(Skill):
    def __init__(self,skill_name,skill_damage,skill_type,skill_ability,sentence):
        self.skill_name=skill_name
        self.skill_type=skill_type
        self.skill_damage=skill_damage
        self.skill_ability="특수:"+skill_ability
        self.sentence=sentence
    def skill(self,enemy):
        if self.acu_choice() is True:
            print(self.skill_name+"을 시전했다!")
            print(self.sentence)
            enemy.life_confirm()
        else:
            print(self.skill_name + "는 실패했다!")
            return 0

class Setting():
    def __init__(self,name,hp,type,acu,*skill_list):
        self.name = name
        self.hp = hp
        self.type = type
        self.acu = acu
        self.skill_list=skill_list
    def life_confirm(self):
        if self.hp<=0:
            return True

class Pika(Setting,Skill):
    def __init__(self):
        Setting.__init__(self,"피카츄",300,"전기",50,"십만볼트","몸통박치기")
    def skill_1(self,enemy):
        Skill.__init__(self,"십만볼트",100,"전기")
        Skill.skill(self,enemy)
    def skill_2(self,enemy):
        Skill.__init__(self,"몸통박치기",50,"노말")
        Skill.skill(self,enemy)

class Ingoking(Setting,Skill):
    def __init__(self):
        Setting.__init__(self,"잉어킹", 10, "노말", 50,"튀어오르기","몸통박치기")
    def skill_1(self):
        SpecialSkill.__init__(self,"튀어오르기",0,"노말","높이 뛰어오른다","엄청 높이 뛰어올랐다!@")
        SpecialSkill.skill(self)
    def skill_2(self,enemy):
        Skill.__init__(self,"몸통박치기",50,"노말")
        Skill.skill(self,enemy)

class Lichu(Setting,Skill):
    def __init__(self):
        Setting.__init__(self,"라이츄",200,"전기",50,"100만볼트","돌진")
    def skill_1(self,enemy):
        Skill.__init__(self,"100만볼트",200,"전기")
        Skill.skill(self,enemy)
    def skill_2(self,enemy):
        Skill.__init__(self,"돌진",60,"노말")
        Skill.skill(self,enemy)

class Cobugi(Setting,Skill):
    def __init__(self):
        Setting.__init__(self,"꼬부기",400,"물",50,"하이드로펌프","비눗방울")
    def skill_1(self,enemy):
        Skill.__init__(self,"하이드로 펌프", 50, "물")
        Skill.skill(self, enemy)
    def skill_2(self,enemy):
        SpecialSkill.__init__(self,"비눗방울",0,"물","상대의 명중률 절반","상대의 명중률이 절반 떨어졌다!")
        SpecialSkill.skill(self,enemy)
        enemy.acu/=2

class Pairi(Setting,Skill):
    def __init__(self):
        Setting.__init__(self,"파이리",350,"불",50,"불대문자","깨물기")
    def skill_1(self,enemy):
        Skill.__init__(self,"불대문자", 150, "불")
        Skill.skill(self, enemy)
    def skill_2(self,enemy):
        Skill.__init__(self,"깨물기",70,"노말")
        Skill.skill(self,enemy)

class Jamanbo(Setting,Skill):
    def __init__(self):
        Setting.__init__(self,"잠만보",1000,"노말",50,"단단해지기","몸통박치기")
    def skill_1(self,enemy):
        SpecialSkill.__init__(self,"단단해지기",0,"노말","체력을 50회복","체력이 +50 되었다!")
        SpecialSkill.skill(self, enemy)
        self.hp+=50
    def skill_2(self,enemy):
        Skill.__init__(self,"몸통박치기",50,"노말")
        Skill.skill(self,enemy)

class Gorapaduck(Setting,Skill):
    def __init__(self):
        Setting.__init__(self,"고라파덕",400,"물",50,"하이드로 펌프","싫은소리")
    def skill_1(self,enemy):
        Skill.__init__(self,"하이드로 펌프", 50, "물")
        Skill.skill(self, enemy)
    def skill_2(self,enemy):
        SpecialSkill.__init__(self,"싫은소리",0,"노말","상대의 명중률을 다음턴에 0으로 만듭니다.","상대의 명중률이 0이 되었다!")
        SpecialSkill.skill(self,enemy)
        enemy.acu=0
        pass

class Gilpagi(Setting,Skill):
    skill_used=0
    def __init__(self):
        Setting.__init__(self,"질뻐기",100,"독",50,"트림","오물웨이브")
    def skill_1(self,enemy):
        SpecialSkill.__init__(self,"트림", 30, "독")
        SpecialSkill.skill(self, enemy)
        enemy.hp-=self.skill_damage
    def skill_2(self,enemy):
        SpecialSkill.__init__(self,"오물웨이브",0,"독","상대의 체력을 절반","상대의 체력이 절반으로 떨어졌다!")
        SpecialSkill.skill(self,enemy)
        enemy.hp/=2

class Tanguri(Setting,Skill):
    def __init__(self):
        Setting.__init__(self,"탕구리",350,"격투",50,"지구던지기","기모으기")
        self.skill_used=0
    def skill_1(self,enemy):
        SpecialSkill.__init__(self,"지구던지기", 2000, "격투",'','')
        if self.skill_used is 3:
            Skill.skill(self, enemy)
        else:
            print("할수없습니다")
    def skill_2(self,enemy):
        SpecialSkill.__init__(self,"기모으기",0,"격투","지구던지기를 쓸수있게됩니다",str(self.skill_used)+"번모음")
        if self.skill_used is not 3:
            self.skill_used += 1
        else:

        SpecialSkill.skill(self,enemy)







