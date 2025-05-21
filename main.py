# from characters.warrior import Warrior
# from characters.mage import Mage
# from characters.archer import Archer
# from characters.priest import Priest
# from characters.evil_wizard import EvilWizard
# from game.mode import choose_game_mode
# from game.battle import battle_party, color_text
# from utils.intro import show_intro
from gui.app import DarkWizardApp
print("Launching game...")
# def create_character():
#     print("Choose your character class: ")
#     print("1. Warrior")
#     print("2. Mage")
#     print("3. Archer")
#     print("4. Priest")
    
#     class_choice = input("Enter the number of your class choice:")
#     name = input("Enter your character's name: ")
    
#     if class_choice == '1':
#         return Warrior(name)
#     elif class_choice == '2':
#         return Mage(name)
#     elif class_choice == '3':
#         return Archer(name)
#     elif class_choice == '4':
#         return Priest(name)
#     else:
#         print("Invalid choice. Defaulting to Warrior. ")
#         return Warrior(name)

# def choose_difficulty():
#     print("\nSelect Difficulty:")
#     print("1. Easy")
#     print("2. Normal")
#     print("3. Hard")
#     print("4. Nightmare")
#     choice = input("Enter difficulty (1-4): ")
    
#     if choice == '1':
#         return {"health": 150, "attack_power": 10}
#     elif choice == '2':
#         return {"health": 250, "attack_power": 15}
#     elif choice == '3':
#         return {"health": 400, "attack_power": 25}
#     elif choice == '4':
#         return {"health": 1000, "attack_power": 35}
#     else:
#         print("Invalide choice. Defaulting to Normal.")
#         return {"health": 250, "attack_power": 15}

# def battle(player, wizard):
#     turn_count = 0
    
#     while wizard.health > 0 and player.health > 0:
#         turn_count += 1
#         print(color_text(f"\n---Turn {turn_count}---", "1;97"))
#         print(color_text(f"{wizard.name}'s Stats - Health: {wizard.health}/{wizard.max_health}, Attack Power: {wizard.attack_power}", "95"))
#         print(color_text(f"\n --- {player.name}'s Turn ---", "96"))
#         print("1. Attack")
#         print("2. Use Special Ability")
#         print("3. Heal")
#         print("4. View Stats")
        
#         while True:
#             choice = input("Choose an action: ").strip()
#             print()
        
#             if choice == '1':
#                 player.attack(wizard)
#                 break
#             elif choice == '2':
#                 player.special_ability(wizard)
#                 break
#             elif choice == '3':
#                 player.heal()
#                 break
#             elif choice == '4':
#                 player.display_stats()
#             else:
#                 print("Invalid choice. Try again.")
            
#         if isinstance(player, Warrior) and player.berserk_active:
#             player.health -= 5
#             print(color_text(f"{player.name} loses 5 health due to Berserk.", "91"))
            
#             if player.special_uses >= player.special_limit:
#                 player.attack_power = player.base_attack_power
#                 player.berserk_active = False
#                 print(f"{player.name}'s Berserk mode has ended.")
            
#         print(color_text("\n" + "=" * 50, "94"))
#         print(color_text(" " * 15 + "End of Turn", "1;94"))
#         print(color_text("=" * 50 + "\n", "94"))
                
#         if wizard.health <= 0:
#             if turn_count <= 15 and not wizard.revived:
#                 print(color_text(f"\n The Dark Wizard rises again, Reborn from the depths of Shadows", "93"))
#                 wizard.health = 700
#                 wizard.max_health = 700
#                 wizard.attack_power += 75
#                 wizard.name += " (Reborn)"
#                 wizard.revived = True
#                 continue
#             else:
#                 if wizard.revived:
#                     print(color_text(f"\n {player.name} has triumphed over the Reborn Dark Wizard! Light returns to the realm, and your name is etched into Legend.", "92"))
#                 else:
#                     print(color_text(f"The wizard {wizard.name} has been defeated by {player.name}!", "92"))
#                 break
#         wizard.regenerate()
#         if wizard.stunned:
#             print(color_text(f"{wizard.name} is stunned and skips this turn!", "93"))
#             wizard.stunned = False
#         elif isinstance(player,Archer) and player.evade_next:
#             print(color_text(f"{player.name} evades the attack with Quick Evade!", "96"))
#             player.evade_next = False
#         else:
#             wizard.attack(player)
            
#         if player.health <= 0:
#             print(color_text(f"{player.name} has been defeated!", "91"))
#             break
            
# def main():
#     while True:
#         show_intro()
#         mode, party_size = choose_game_mode()
#         characters = []
        
#         for i in range(party_size):
#             print(f"\n--- Create Character {i+1} ---")
#             characters.append(create_character())
            
#         difficulty = choose_difficulty()
#         wizard = EvilWizard("The Dark Wizard", **difficulty)
        
#         if mode == "solo":
#             battle(characters[0], wizard)
#         else:
#             battle_party(characters, wizard)
    
        
#         play_again = input("\nWould you like to play again? (y/n): ").lower()
#         if play_again != 'y':
#             print("\nThanks for playing THE DARK WIZARD! Farewell, hero.\n")
#             print("Game created by Marcquez Tookes")
#             break
    
if __name__ == "__main__":
    try:
        app = DarkWizardApp()
        app.mainloop()
    except Exception as e:
        print("An error occured:", e)