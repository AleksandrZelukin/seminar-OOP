import time
class Fighter():
    def __init__(self,life,defense,damage):
        self.life = life
        self.defense = defense
        self.damage = damage
    def attack(self,fighter):
        fighter.life -= self.damage - fighter.defense
fighter_1 = Fighter(100,20,25)
fighter_2 = Fighter(100,20,30)  

while True:
    print("Uzbrūk pirmais cinitajs")
    fighter_1.attack(fighter_2)
    print(f"Dzīvība otrajam cīkstonim:  {fighter_2.life}")
    time.sleep(2)
    if fighter_2.life <=0:
        print("F2 zaudēja")
        break
    print("Uzbrūk otrais cinitajs")
    fighter_2.attack(fighter_1)
    print(f"Dzīvība pirmajam cīkstonim:  {fighter_1.life}")
    time.sleep(2)
    if fighter_1.life <=0:
        print("F1 zaudēja")
        break