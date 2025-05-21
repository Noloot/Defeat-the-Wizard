from .base import Character
import random

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
        self.base_attack_power = 20
        self.special_limit = 8
        self.special_uses = 0
        self.evade_next = False
    
    def use_arrow_rain(self, opponent):
        if self.special_uses >= self.special_limit:
            return f"{self.name} has used all of their Arrow Rains"
        damage = self.attack_power * 2
        opponent.health -= damage
        self.special_uses += 1
        return f"{self.name} rains arrows down from the heavens and surrounds {opponent.name} with no escape and deals {damage} damage!"
    
    def use_quick_evade(self, opponent):
        self.evade_next = True
        self.special_uses += 1
        return f"{self.name} evaded the {opponent.name}'s next attack!"
    
    def attempt_evolution(self, opponent):
        result = ""
        chance = random.randint(1, 100)
        if chance <= 30:
            self.max_health += 30
            self.health = self.max_health
            self.attack_power += 15
            self.base_attack_power = self.attack_power
            self.name += " the Ranger"
            result += f"{self.name} has evolved into a Ranger!\n"
        else:
            result += f"{self.name}'s evolution attempt failed.\n"
        if hasattr(opponent, "evolve") and not opponent.evolved:
            if random.randint(1, 100) <= 20:
                opponent.evolve()
                result += f"{opponent.name} evolves in response to your power!"
            else:
                result += f"{opponent.name} attempted to evolve but failed."
        return result