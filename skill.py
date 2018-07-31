import sys,time,random
'''"10만볼트",100,"전기","몸통박치기",50,"노말"'''


def acu_choice(self):
    if random.randrange(1, 100) <= self.acu:
        return True
    else:
        print("명중하지 못했다!")
def skill_a(self, enemy):
    if self.acu_choice() is True:
        if self.skill_a_type is "노말":
            print(self.skill_a_name + "을 시전했다!")
            enemy.hp -= self.skill_a_damage
            enemy.life_confirm()

print("this is test")


