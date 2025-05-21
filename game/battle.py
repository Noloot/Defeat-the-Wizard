from characters.warrior import Warrior
import random

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def battle_party(party, wizard):
    turn_count = 0
    
    while wizard.health > 0 and any(p.health > 0 for p in party):
        turn_count += 1
        print(color_text(f"\n--- Turn {turn_count} ---", "1;97"))
        print(color_text(f"{wizard.name}'s Stats - Health: {wizard.health}/{wizard.max_health}, Attack Power: {wizard.attack_power}", "95"))
        
        for player in party:
            if player.health <= 0:
                print(color_text(f"{player.name} is down and cannot act.", "90"))
                continue
            
            print(color_text(f"\n--- {player.name}'s Turn ---", "96"))
            print("1. Attack")
            print("2. Special Ability")
            print("3. Heal")
            print("4. View Stats")
            print("5. Skip Turn")
            
            while True:
                choice = input("Choose an action: ").strip()
                print()
            
                if choice == '1':
                    player.attack(wizard)
                    if wizard.health <= 0:
                        print(color_text(f"\nThe party has defeated {wizard.name}! Light returns to the land.", "92"))
                        return
                    break
                elif choice == '2':
                    player.special_ability(wizard)
                    if wizard.health <= 0:
                        print(color_text(f"\nThe party has defeated {wizard.name}! Light returns to the land.", "92"))
                        return
                    break
                elif choice == '3':
                    player.heal()
                    break
                elif choice == '4':
                    player.display_stats()
                    continue
                elif choice == '5':
                    print(color_text(f"{player.name} skips their turn.", "93"))
                    break
                else:
                    print(color_text("Invalid choice. Try again.", "91"))
                
            if isinstance(player, Warrior) and player.berserk_active:
                player.health -= 5
                print(color_text(f"{player.name} loses 5 health due to Berserk.", "91"))
                
                if player.special_uses >= player.special_limit:
                    player.attack_power = player.base_attack_power
                    player.berserk_active = False
                    print(color_text(f"{player.name}'s Berserk mode has ended.", "90"))
                    
        print(color_text("\n" + "=" * 50, "94"))
        print(color_text(" " * 15 + "End of Party Turn", "1;94"))
        print(color_text("=" * 50 + "\n", "94"))
                
        if wizard.health <= 0:
            print(color_text(f"\nThe party has defeated {wizard.name}! Light returns to the land.", "92"))
            break

        wizard.regenerate()
        print(color_text(f"{wizard.name}'s Stats - Health: {wizard.health}/{wizard.max_health}, Attack Power: {wizard.attack_power}", "95"))

        if wizard.stunned:
            print(color_text(f"{wizard.name} is stunned and skips this turn!", "93"))
            wizard.stunned = False
            continue
        
        alive_players = [p for p in party if p.health > 0]
        target = random.choice(alive_players)
        wizard.attack(target)
        print(color_text(f"{wizard.name} targets {target.name}!", "91"))

        if all(p.health <= 0 for p in party):
            print(color_text("The entire party has fallen... Darkness prevails.", "91"))
            break
        
def battle(player, wizard):
    return battle_party([player], wizard)