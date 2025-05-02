# 🧙‍♂️ Fantasy Battle Game

This is a terminal-based Python game where the player battles against an Evil Wizard using a character class of their choice. Each class comes with its own stats and unique abilities.

---

## 🚀 Features
- **Character Classes:** Warrior, Mage, Archer, and Priest
- **Randomized Attack Damage** for dynamic gameplay
- **Healing System** using random health regeneration (1-50 HP)
- **Special Abilities** for each class with usage limits
- **Enemy AI:** Evil Wizard that regenerates and attacks
- **Status Effects:**
  - * Stun* (Mage's Ice Storm)
  - * Evade* (Archer's Quick Evade)
  - * Berserk* (Warrior's Berserk mode with high risk/reward)

---

## 📦 Requirements
- Python 3.7+

---

## ▶️ How to Play
1. Run the script in a terminal:
   ```bash
   python battle_game.py
   ```
2. Choose your character class
3. During each turn, select one of the following options:
   - Attack the wizard
   - Use a special ability (limited uses)
   - Heal yourself (random 1-50 HP)
   - View your current stats

---

## 🧝‍♂️ Character Classes & Abilities

### Warrior
- **Health:** 140
- **Attack Power:** 25
- **Abilities:**
  - *Deadly Strike* (2.5x damage)
  - *Berserk* (temporarily x4 attack power, loses 5 HP per turn)

### Mage
- **Health:** 100
- **Attack Power:** 35
- **Abilities:**
  - *Meteor Strike* (4x damage)
  - *Ice Storm* (stuns wizard for one turn)

### Archer
- **Health:** 120
- **Attack Power:** 20
- **Abilities:**
  - *Arrow Rain* (2x damage)
  - *Quick Evade* (avoids next wizard attack)

### Priest
- **Health:** 80
- **Attack Power:** 10
- **Abilities:**
  - *Max Health Regen* (fully restores health)
  - *Holy Light* (10x damage)

---

## ⚔️ Enemy: Evil Wizard
- **Health:** 250
- **Attack Power:** 15
- **Special Trait:** Regenerates 5 HP per turn

---

## 💡 Tips
- Use healing when your health is low
- Save your special abilities for crucial moments
- Watch the wizard's health and plan your next move strategically

---

## 📝 Future Enhancements
- Add inventory and potions
- Multiple enemy types
- Leveling system
- Save/load game

---

## 📂 File Structure
```
battle_game.py        # Main game logic
shows_list.txt        # Example list used for TV show extension (optional)
```

---

## 🔒 License
This project is open source and free to use for learning or personal modification.

