import time
import random
class Fighter:
    def __init__(self,life,defense,damage):
        self.life=life
        self.defense =defense
        self.damage =damage
    def attack(self,fighter):
        fighter.life -= self.damage -fighter.defense

class Creature(Fighter):
    def __init__(self, life, defense, damage):
        self.nagi =random.randint(0,5)
        super().__init__(life, defense, damage)
    def attack(self, fighter):
        fighter.life -= self.damage+ self.nagi -fighter.defense

class Hero(Fighter):
    def __init__(self, life, defense, damage):
        self.exp =0
        self.level=1
        self.critical=10

        super().__init__(life, defense, damage)
    def attack(self, fighter):
        if random.randint(1,100)<=self.critical:
            fighter.life -= (self.damage- fighter.defense)*2   
        else:
            fighter.life -= self.damage- fighter.defense        

class Monster(Fighter):
    def __init__(self):
        self.life=0
        self.defense=0
        self.damage=0
        self.boss_level=1
        self.penetration =5
    def attack(self, fighter):
        fighter.life -= self.damage -fighter.defense


creature=Creature(40,20,30)
hero=Hero(200,20,30)   

def increase_level():
    hero.level +=1
    print("""
    1 Dzīvību
    2 Aizsardzību
    3 Uzbrukumu
    4 Veiksmi    
    """)
    options =int(input("Ko palielināt?"))
    if options ==1:
        hero.life+=10
        print(f"Dziviba: {hero.life}")
    elif options ==2:
        hero.defense+=2
        print(f"Aizsardziba: {hero.defense}")
    elif options ==3:
        hero.damage+=2
        print(f"Uzbrukums: {hero.damage}")
    elif options ==4:
        hero.critical+=2
        print(f"Veiksme: {hero.critical}")
    else:
        pass

def attack_creature():
    creature_no = int(input("Cik daudz radījumu?"))
    no_exp=creature_no
    hero_life=hero.life
    while True:
        hero.attack(creature)
        if creature.life <=0 and creature_no==1:
            print("Radijumi ir beigti!")
            hero.exp += no_exp*50
            hero.life=hero_life
            if hero.exp>=hero.level*100:
                increase_level()
                hero.exp=0
            break
        elif creature.life <=0 and creature_no>1:
            creature_no -=1
            print(f"palikušie radijumi{creature_no}")
            creature.life=40
        
        for i in range(creature_no):
            creature.attack(hero)
        
        if hero.life <=0:
            print("Varonis nomira!")
            break
        print(f"Varoņa dzīvība:{hero.life}")
        time.sleep(2)


def attack_monster():
    pass
def main():
    while True:
        print("""
        1 Uzbrukt radījumam
        2 Uzbrukt briesmonim
        3 Beigt spēli
        """)
        choice = int(input("Ko vēlies darīt?"))
        if choice ==1:
            attack_creature()
        elif choice ==2:
            attack_monster()
        elif choice ==3:
            break
main()