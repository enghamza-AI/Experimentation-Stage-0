#character stat system

class Character:

    def __init__(self, health, stamina, strength):
        self.health = health
        self.stamina = stamina
        self.strength = strength

#method to calculate power level

    def power_level(self):
        power = (self.strength * 2) + self.stamina + (self.health * 0.5)
        return power
    
#create characters

player = Character(100, 60, 40)
enemy = Character(80, 50, 30)

#print power levels

print("Player power:", player.power_level())
print("Enemy power:", enemy.power_level())

