from .base import Character
import random

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.base_attack_power = 25
        self.special_limit = 4
        self.special_uses = 0
        self.berserk_active = False 
    
    def use_deadly_strike(self, opponent):
        if self.special_uses >= self.special_limit:
            return f"{self.name} has used all of their Deadly Strikes."
        damage = self.attack_power * 2.5
        opponent.health -= damage
        self.special_uses += 1
        return f"{self.name} strikes {opponent.name} and does {int(damage)} damage!"

    def activate_berserk(self):
        if self.special_uses >= self.special_limit:
            return f"{self.name} has used all of their special abilities."
        self.berserk_active = True
        self.attack_power = self.base_attack_power * 4
        self.special_uses += 1
        return f"{self.name} enters Berserk mode! Attack power is now {self.attack_power}!"

    def attempt_evolution(self, opponent):
        result = ""
        chance = random.randint(1, 100)
        if chance <= 30:
            self.max_health += 60
            self.health = self.max_health
            self.attack_power += 15
            self.base_attack_power = self.attack_power
            self.name += " the Hero"
            result += f"{self.name} has evolved into a HERO!\n"
        else:
            result += f"{self.name}'s evolution attempt failed.\n"
        if hasattr(opponent, "evolve") and not opponent.evolved:
            if random.randint(1, 100) <= 20:
                opponent.evolve()
                result += f"{opponent.name} evolves in response to your power!"
            else:
                result += f"{opponent.name} attempted to evolve but failed."
        return result
