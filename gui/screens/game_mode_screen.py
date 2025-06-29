import tkinter as tk

class GameModeScreen(tk.Frame):
    def __init__(self,parent, controller, player_name, selected_class, difficulty):
        """
        Screen where the user selects between solo or party mode
        """
        super().__init__(parent)
        self.controller = controller
        self.player_name = player_name
        self.selected_class = selected_class
        self.difficulty = difficulty
        
        self.configure(bg="black")
        
        tk.Label(
            self, 
            text="Choose Game Mode", 
            font=("Georgia", 24, "bold"), 
            fg="white", 
            bg="black"
        ).pack(pady=40)
        
        tk.Button(
            self, 
            text="Solo Adventure", 
            font=("Arial", 16), 
            width=20, bg="#222", 
            fg="blue",
            command=lambda: self.controller.start_game("solo", self.player_name, self.selected_class, self.difficulty)
        ).pack(pady=10)
        
        tk.Button(
            self, 
            text="Back", 
            font=("Arial", 14), 
            bg="#444", 
            fg="blue", 
            command=lambda: self.controller.show_difficulty_selection(self.player_name, self.selected_class)
        ).pack(pady=30)