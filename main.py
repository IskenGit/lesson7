from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
class Sword(Weapon):
    def attack(self):
        print("наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("делает выстрел из лука.")
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            print(f"{self.name} ", end="")
            self.weapon.attack()
        else:
            print("У бойца нет оружия.")
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"Монстр {self.name} побежден!")

def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()

# Демонстрация работы
fighter = Fighter("Рыцарь")
monster = Monster("Гоблин")

# Боец выбирает меч
fighter.changeWeapon(Sword())
print(f"{fighter.name} выбирает меч.")
battle(fighter, monster)

# Боец выбирает лук
fighter.changeWeapon(Bow())
print(f"\n{fighter.name} выбирает лук.")
battle(fighter, monster)
