# Fantasy Battle Game

A terminal-based turn-based combat game where you choose a character class to battle an evil Dark Wizard. Each character has unique abilities, health, and attack powers. The game includes random damage, healing, special abilities, and even evolution mechanics.

---

## 🛡️ Character Classes

### Warrior
- High health and strong attack.
- **Special Abilities:**
  - **Deadly Strike:** Deals 2.5x attack power.
  - **Berserk Mode:** Temporarily boosts attack power 4x but drains 5 health each turn.
  - **Evolution:** Chance to evolve into "Hero" with boosted stats.

### Mage
- Glass cannon with powerful spells.
- **Special Abilities:**
  - **Meteor Strike:** Massive 4x damage.
  - **Ice Storm:** Stuns the opponent.
  - **Evolution:** Chance to evolve into "Archmage".

### Archer
- Balanced damage and utility.
- **Special Abilities:**
  - **Arrow Rain:** Double damage.
  - **Quick Evade:** Dodges the next enemy attack.
  - **Evolution:** Chance to evolve into "Ranger".

### Priest
- Support role with healing and light damage.
- **Special Abilities:**
  - **Max Health Regen:** Fully heals.
  - **Holy Light:** 10x attack power.
  - **Evolution:** Chance to evolve into "Saint".

---

## 🧙‍♂️ Enemy: The Dark Wizard
- Regenerates 5 HP per turn.
- Can be **stunned** (by Mage).
- Can have attacks **evaded** (by Archer).
- Has a chance to **evolve** after player's evolution attempt.
  - If it fails, a message indicates a failed evolution attempt.

---

## 🔁 Game Mechanics

- **Random Attack Damage**: Normal attacks deal random damage from 1 to `attack_power`.
- **Healing**: Restore 1–50 HP, up to your `max_health`.
- **Special Limits**: Each class can only use special abilities a limited number of times.
- **Evolution System**: Characters may evolve mid-battle, gaining a new title and improved stats. Dark Wizard may attempt to evolve too.

---

## ▶️ How to Play
1. Run the script with `python filename.py`.
2. Choose a class and enter your name.
3. Take turns to **attack**, **heal**, use a **special ability**, or **view stats**.
4. Try to defeat the Dark Wizard before he defeats you.

---

## 📦 Requirements
- Python 3.10+
- No external dependencies

---

## 🎮 Future Enhancements
- More enemies and stages
- Saving/loading characters
- Multiplayer
- XP and leveling

---

Enjoy your battle adventure!

