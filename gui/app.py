import tkinter as tk
from gui.screens.intro_screen import IntroScreen
from gui.screens.name_input_screen import NameInputScreen
from gui.screens.character_creation import CharacterSelectScreen
from gui.screens.difficulty_selection import DifficultySelectScreen
from gui.screens.game_mode_screen import GameModeScreen


class DarkWizardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Dark Wizard")
        self.geometry("800x600")
        self.resizable(False, False)
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.selected_class = None
        self.character_name = None
        
        self.party = []
        self.active_index = 0
        self.wizard = None
        
        self.show_intro_screen()
        
    def get_active_player(self):
        if self.party and 0 <= self.active_index < len(self.party):
            return self.party[self.active_index]
        return None
        
    def attack_current(self):
        self.get_active_player().attack(self.wizard)
            
    def heal_current(self):
        self.get_active_player().heal()
            
    def reset_turn_index(self):
        self.active_index = 0
        
    def show_intro_screen(self):
        self._clear_screen()
        IntroScreen(self.container, self).pack(fill="both", expand=True)
        
    def show_name_input_screen(self, selected_class):
        self._clear_screen()
        NameInputScreen(self.container, self, selected_class).pack(fill="both", expand=True)
        
    def show_character_select_screen(self):
        self._clear_screen()
        CharacterSelectScreen(self.container, self).pack(fill="both", expand=True)
        
    def show_difficulty_selection(self, character_name, selected_class):
        self._clear_screen()
        DifficultySelectScreen(self.container, self, character_name, selected_class).pack(fill="both", expand=True)
        
    def show_party_select_screen(self):
        self._clear_screen()
        from gui.screens.party_selection_screen import PartySelectionScreen
        PartySelectionScreen(self.container, self).pack(fill="both", expand=True)
        
    def show_game_mode_screen(self, player_name, selected_class, difficulty):
        self._clear_screen()
        GameModeScreen(self.container, self, player_name, selected_class, difficulty).pack(fill="both", expand=True)
    
    def show_battle_screen(self, player, wizard, attack_callback, special_callback, heal_callback):
        self._clear_screen()
        from gui.screens.battle_screen import BattleScreen
        BattleScreen(self.container, self, player, wizard, attack_callback, special_callback, heal_callback).pack(fill="both", expand=True)
        
    def _clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        
    def start_game(self, mode, player_name, selected_class, difficulty, custom_party=None):
        print(f"Starting game with mode: {mode}, player: {player_name}, class: {selected_class}, difficulty: {difficulty}")
        
        from characters.warrior import Warrior
        from characters.mage import Mage
        from characters.archer import Archer
        from characters.priest import Priest
        from characters.evil_wizard import EvilWizard
        
        class_map = {
            "warrior": Warrior,
            "mage": Mage,
            "archer": Archer,
            "priest": Priest
        }
        
        
        wizard = EvilWizard("The Dark Wizard", **difficulty)
        
        if mode == "solo":
            if not player_name or not selected_class:
                raise ValueError("Solo mode requires player name and class.")
            
            player_class = class_map[selected_class.lower()]
            player = player_class(player_name)
            
            self.show_battle_screen(
                player, 
                wizard,
                attack_callback=lambda: player.attack(wizard),
                special_callback=None,
                heal_callback=player.heal
            )
            
        elif mode == "party":
            if not custom_party:
                print("No custom party provided. Falling back to default.")
            party = custom_party if custom_party else [
                Warrior("Ragnar"),
                Mage("Elira"),
                Archer("Thorne"),
                Priest("Luna")
            ]
            
            self.party = party
            self.wizard = wizard
            self.active_index = 0
            
            self.show_battle_screen(
                party,
                wizard,
                attack_callback=self.attack_current,
                special_callback=None,
                heal_callback=self.heal_current
            )
            
        else:
            print("Unknown game mode.")
            
    def start_party_battle(self, party):
        from characters.evil_wizard import EvilWizard
        wizard = EvilWizard("The Dark Wizard", health=250, attack_power=25)
    
        self.party = party
        self.wizard = wizard
        self.active_index = 0

        self.show_battle_screen(
            party,
            wizard,
            attack_callback=self.attack_current,
            special_callback=None,
            heal_callback=self.heal_current
        )
    
if __name__ == "__main__":
    app = DarkWizardApp()
    app.mainloop()