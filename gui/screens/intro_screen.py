import tkinter as tk

class IntroScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.configure(bg="black")
        
        title = tk.Label(
            self, 
            text="THE DARK WIZARD", 
            font=("Georgia", 28, "bold"), 
            fg="white", 
            bg="black"
        )
        title.pack(pady=60)
        
        subtitle = tk.Label(
            self, 
            text="A Fantasy Battle RPG", 
            font=("Arial", 18), 
            fg="White", 
            bg="Black"
        )
        subtitle.pack(pady=10)
        
        start_button = tk.Button(
            self, 
            text="Solo Adventure", 
            font=("Arial", 16), 
            bg="#444", 
            fg="blue", 
            command=self.start_game
        )
        start_button.pack(pady=40)
        
        party_mode = tk.Button(
            self,
            text="Build a Party",
            font=("Arial", 16),
            bg="#444",
            fg="blue",
            command=self.controller.show_party_select_screen
        )
        party_mode.pack(pady=10)
        
    def start_game(self):
        
        print("Game Starting...")
        
        self.controller.show_character_select_screen()