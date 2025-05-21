import random

class Character:
    def __init__(self,name,health,attack_power):
        self.name = name 
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        
    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def heal(self):
        heal_amount = random.randint(1, 50)
        if self.health < self.max_health:
            self.health = min(self.health + heal_amount, self.max_health)
            print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}/{self.max_health}")
        else:
            print(f"{self.name} is already at full health!")
            
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        