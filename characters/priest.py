from .base import Character
import random

class Priest(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=10)
        self.base_attack_power = 10
        self.special_limit = 3
        self.special_uses = 0
        
    def use_max_health_regen(self, party):
        if self.special_uses >= 2:
            return f"{self.name} has no uses of Max Health Regen left!"
        
        healed_names = []
        
        for member in party:
            member.health = member.max_health
            healed_names.append(member.name)
        
        if self not in party:
            self.health = self.max_health
            healed_names.append(self.name)
            
        self.special_uses += 1
        return f"{self.name} used Max Health Regen! Healed: {', '.join(healed_names)}. ({2 - self.special_uses} use(s) left)"
    
    def use_holy_light(self, opponent):
        damage = self.attack_power * 10
        opponent.health -= damage
        self.special_uses += 1
        return f"{self.name} uses Holy Light on {opponent.name} and deals {damage} critical damage! ({self.special_limit - self.special_uses} use(s) left)"
        
    def attempt_evolution(self, opponent):
        result = ""
        chance = random.randint(1, 100)
        if chance <= 30:
            self.max_health += 100
            self.health = self.max_health
            self.attack_power += 25
            self.base_attack_power = self.attack_power
            self.name += " the Saint"
            result += f"{self.name} has evolved into a Saint!\n"
        else:
            result += f"{self.name}'s evolution attempt failed.\n"
        if hasattr(opponent, "evolve") and not opponent.evolved:
            if random.randint(1, 100) <= 20:
                opponent.evolve()
                result += f"{opponent.name} evolves in response to your power!"
            else:
                result += f"{opponent.name} attempted to evolve but failed."
        return result