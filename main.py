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
            print(f"{self.name} iis already at full health!")
            
    def display_stats(self):
        print(f"{self.name}'s Ststs - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.base_attack_power = 25
        self.special_limit = 4
        self.special_uses = 0
        self.berserk_active = False 
    
    def special_ability(self, opponent):
        print("\nSpecial Ability")
        if self.special_uses >= self.special_limit:
            print(f"{self.name} you have used all of your Deadly Strikes")
            return
        print("1. Deadly Strike")
        print("2. Breserk")
        action = input("\nWhich ability would you like to use? ")
        
        if action == '1':
            damage = self.attack_power * 2.5
            opponent.health -= damage
            self.special_uses += 1
            print(f"{self.name} strikes {opponent.name} and does {damage} damage!")
        elif action == '2':
            self.berserk_active = True
            self.attack_power = self.base_attack_power * 4
            self.special_uses += 1
            print(f"{self.name} enters Berserk mode! Attack power is now {self.attack_power}!")
            
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_limit = 4
        self.special_uses = 0
    
    def special_ability(self, opponent):
        print("\nSpecial Abilities")
        if self.special_uses >= self.special_limit:
            print(f"{self.name} Can no longer use Meteor Strike")
            return
        print("1. Meteor Strike")
        print("2. Ice Storm")
        action = input("\nWhich ability do you want to use? ")
        
        if action == '1':
            damage = self.attack_power * 4
            opponent.health -= damage
            self.special_uses += 1
            print(f"{self.name} drops a meteor on {opponent.name}'s head and does {damage} damage!")
        elif action == '2':
            opponent.stunned = True
            print(f"{self.name} casts Ice Storm! {opponent.name} is stunned and cannot attack next turn!")
        else:
            print("Invalid input.")
            
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
        self.special_limit = 8
        self.special_uses = 0
        self.evade_next = False
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        if self.special_uses >= self.special_limit:
            print(f"{self.name} has run out of special ability uses!")
            return
        print("1. Arrow Rain")
        print("2. Quick Evade")
        action = input("\nWhich ability do you want to use? ")
        
        if action == '1':
            damage = self.attack_power * 2
            opponent.health -= damage
            self.special_uses += 1
            print(f"{self.name} rains arrows down from the heavens and surrounds {opponent.name} with no escape and deals {damage} damage!")
        elif action == '2':
            self.evade_next = True
            self.special_uses += 1
            print(f"{self.name} evaded the {opponent.name}'s next attack!")
        else:
            print("Invalid input.")
            
class Priest(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=10)
        self.special_limit = 3
        self.special_uses = 0
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Max Health Regen")
        print("2. Holy Light")
        action = input("\nWhich ability do you want to use? ")
        
        if action == '1':
            self.health = self.max_health
            self.special_uses += 1
            print(f"{self.name} has been fully healed to {self.health} health!")
        elif action == '2':
            damage = self.attack_power * 10
            opponent.health -= damage
            self.special_uses =+ 1
            print(f"{self.name} uses Holy Light on {opponent.name} and deals {damage} critical damage!")
        else:
            print("Invalid input.")
            
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=15)
        self.stunned = False
        
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
def create_character():
    print("Choose your character class: ")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Priest")
    
    class_choice = input("Enter the number of your class choice:")
    name = input("Enter your character's name: ")
    
    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Priest(name)
    else:
        print("Invalid choice. Defaulting to Warrior. ")
        return Warrior(name)
    
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n --- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")
        
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")
            
        if isinstance(player, Warrior) and player.berserk_active:
            if player.special_uses >= player.special_limit:
                player.attack_power = player.base_attack_power
                player.berserk_active = False
                print(f"{player.name}'s Berserk mode has ended. Attack power retored to {player.attack_power}.")
            
            print(f"{player.name} loses 5 health due to Berserk and gains *4 attack power! Health: {player.health}, Attack Power: {player.attack_power}")
            
            if player.special_uses >= player.special_limit:
                player.berserk_active = False
                print(f"{player.name}'s Berserk mode has ended.")
            
        if wizard.health > 0:
            wizard.regenerate()
            if hasattr(wizard, 'stunned') and wizard.stunned:
                print(f"{wizard.name} is stunned and skips this turn!")
                wizard.stunned = False
            elif isinstance(player, Archer) and getattr(player, 'evade_next', False):
                print(f"{player.name} evades the attack with Quick Evade!")
                player.evade_next = False
            else:
                wizard.attack(player)
            
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break
        
        if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")
            
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)
    
if __name__ == "__main__":
    main()