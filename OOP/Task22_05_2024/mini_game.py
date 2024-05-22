class Weapon:
    def __init__(self, name_pm: str, damage_pm: int):
        self.name = name_pm
        self.damage = damage_pm

class Player:
    def __init__(self, name_pm: str, health_pm: int, arrmor_pm: int, weapon_pm: Weapon):
        self.name = name_pm
        self.health = health_pm
        self.arrmor = arrmor_pm
        self.weapon = weapon_pm

    def attack(self, another_player):
        another_player.take_damage(self.weapon.damage)
        print(f"{self.name} атаковал {another_player.name} и нанёс {self.weapon.damage} урона из {self.weapon.name}")

    def take_damage(self, damage: int):
        if self.arrmor > 0:
            self.arrmor -= damage
        else:
            self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print(f"{self.name} мёртв так как")
        self.health = 0

bow = Weapon(name_pm="лук", damage_pm=5)
awp = Weapon(name_pm="AWP", damage_pm=50)
usp = Weapon(name_pm="USP", damage_pm=21)

player1 = Player(name_pm="Мусорщик", health_pm=15, arrmor_pm=35, weapon_pm=bow)
player2 = Player(name_pm="Адольф", health_pm=45, arrmor_pm=150, weapon_pm=awp)
player3 = Player(name_pm="LuckyWinner", health_pm=30, arrmor_pm=25, weapon_pm=usp)

player1.attack(player2)
player2.attack(player1)

player3.attack(player1)

player3.attack(player2)
player3.attack(player2)
player3.attack(player2)
player3.attack(player2)
player3.attack(player2)
player3.attack(player2)
player3.attack(player2)
player3.attack(player2)
player3.attack(player2)
player3.attack(player2)
