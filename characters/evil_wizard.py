from .base import Character
import random

class EvilWizard(Character):
    def __init__(self, name, health=250, attack_power=15):
        super().__init__(name, health, attack_power)
        self.stunned = False
        self.evolved = False
        self.revived = False
        
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
    def evolve(self):
        if not self.evolved:
            print(f"{self.name} begins to channel dark energy...")
            self.health += 100
            self.max_health += 100
            self.attack_power += 5
            self.name += " Ascended"
            self.evolved = True
            print(f"{self.name} has evolved into a DARK ARCHMAGE! Health and attack increased")
        