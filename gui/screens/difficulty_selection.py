import tkinter as tk

class DifficultySelectScreen(tk.Frame):
    def __init__(self, parent, controller, player_name, selected_class):
        super().__init__(parent)
        self.controller = controller
        self.player_name = player_name
        self.selected_class = selected_class
        
        self.configure(bg="black")
        
        title = tk.Label(
            self,
            text="Choose Difficulty",
            font=("Georgia", 24, "bold"),
            fg="white",
            bg="black"
        )
        title.pack(pady=40)
        
        difficulties = [
            ("Easy", {"health": 150, "attack_power": 10}),
            ("Normal", {"health": 250, "attack_power": 15}),
            ("Hard", {"health": 400, "attack_power": 25}),
            ("Nightmare", {"health": 1000, "attack_power": 35})
        ]
        
        for label, stats in difficulties:
            button = tk.Button(
                self,
                text=label,
                font=("Arial", 16),
                width=20,
                bg="#222",
                fg="blue",
                command=lambda s=stats: self.select_difficulty(s)
            )
            button.pack(pady=10)

        back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 14),
            bg="#444",
            fg="blue",
            command=lambda: controller.show_name_input_screen(self.selected_class)
        )
        back_button.pack(pady=30)

    def select_difficulty(self, stats):
        print(f"{self.player_name} the {self.selected_class} chose difficulty with stats: {stats}")
        self.controller.start_game(
            mode="solo",
            player_name=self.player_name,
            selected_class=self.selected_class,
            difficulty=stats
        )
