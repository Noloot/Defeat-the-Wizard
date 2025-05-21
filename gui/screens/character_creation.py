import tkinter as tk
from functools import partial

class CharacterSelectScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="black")
        
        title = tk.Label(self, text="Choose Your Character", font=("Georgia", 24, "bold"), fg="white", bg="black")
        title.pack(pady=40)
        
        characters = [
            ("Warrior", "warrior"),
            ("Mage", "mage"),
            ("Archer", "archer"),
            ("Priest", "priest")
        ]
        
        for name, char_type in characters:
            button = tk.Button(
                self,
                text=name,
                font=("Arial", 16),
                width=20,
                bg="#222",
                fg="blue",
                command=partial(self.select_character, char_type)
            )
            button.pack(pady=10)
            
        self.back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 14),
            bg="#444",
            fg="blue",
            command=self.controller.show_intro_screen
        )
        self.back_button.pack(pady=30)
        
    def select_character(self, char_type):
        print(f"Character selected: {char_type.capitalize()}")
        self.controller.show_name_input_screen(char_type)