from .base import Character
import random

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_limit = 4
        self.special_uses = 0
        self.base_attack_power = 35
        
    def use_meteor_strike(self, opponent):
        if self.special_uses >= self.special_limit:
            return f"{self.name} has used all of their special use(s)"
        damage = self.attack_power * 4
        opponent.health -= damage
        self.special_uses += 1
        return f"{self.name} drops a meteor on {opponent.name}'s head and does {int(damage)} damage! ({self.special_limit - self.special_uses} use(s) left)"
    
    def use_ice_storm(self, opponent):
        if self.special_uses >= self.special_limit:
            return f"{self.name} has used all of their special use(s)"
        self.special_uses += 1
        opponent.stunned = True
        return f"{self.name} casts Ice Storm! {opponent.name} is stunned and cannot attack next turn! ({self.special_limit - self.special_uses} use(s) left)"
    
    def attempt_evolution(self, opponent):
        result = ""
        chance = random.randint(1, 100)
        if chance <= 30:
            self.max_health += 60
            self.health = self.max_health
            self.attack_power += 15
            self.base_attack_power = self.attack_power
            self.name += " the Archmage"
            result += f"{self.name} has evolved into a Archmage!\n"
        else:
            result += f"{self.name}'s evolution attempt failed.\n"
        if hasattr(opponent, "evolve") and not opponent.evolved:
            if random.randint(1, 100) <= 20:
                opponent.evolve()
                result += f"{opponent.name} evolves in response to your power!"
            else:
                result += f"{opponent.name} attempted to evolve but failed."
        return result