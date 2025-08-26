import tkinter as tk
import random
from utils.difficulty_flavor import pick_lines

class DifficultySelectScreen(tk.Frame):
    def __init__(self, parent, controller, player_name, selected_class, mode):
        super().__init__(parent)
        self.controller = controller
        self.player_name = player_name
        self.selected_class = selected_class
        self.mode = mode
        
        self.hero_class = (selected_class or "").strip().title()
        
        self.bg_default = "#000000"
        self.bg_map = {
            "Easy": "#203224",
            "Normal": "#222533",
            "Hard": "#332225",
            "Nightmare": "#15151e"
        }
        
        self.configure(bg=self.bg_default)
        
        self.title_label = tk.Label(
            self,
            text="Choose Difficulty",
            font=("Georgia", 28, "bold"),
            fg="#f2f2f2",
            bg=self["bg"],
        )
        self.title_label.pack(pady=(32, 8))
        
        self.flavor_wrap = tk.Frame(self, bg=self["bg"], height=50, width=760)
        self.flavor_wrap.pack(pady=(0, 20), padx=20, fill="x")
        self.flavor_wrap.pack_propagate(False)
        
        self.flavor = tk.Label(
            self,
            text="Hover a difficulty to preview flavor & rules.",
            justify="left",
            font=("Georgia", 13),
            fg="#f0e6d2",
            bg=self["bg"],
            wraplength=720,
            anchor="nw"
        )
        self.flavor.pack(fill="both", expand=True)
        
        self.btn_wrap = tk.Frame(self, bg=self["bg"])
        self.btn_wrap.pack()
        
        self.difficulties = [
            ("Easy", {"health": 150, "attack_power": 10}),
            ("Normal", {"health": 250, "attack_power": 15}),
            ("Hard", {"health": 400, "attack_power": 25}),
            ("Nightmare", {"health": 1000, "attack_power": 35})
        ]
        
        self.buttons = {}
        for label, stats in self.difficulties:
            btn = tk.Button(
                self.btn_wrap,
                text=label,
                font=("Arial", 18, "bold"),
                width=20,
                padx=16,
                pady=10,
                bg="#222222",
                fg="#c8d6ff",
                activebackground="#2d2d2d",
                activeforeground="#ffffff",
                bd=2,
                relief="ridge",
                cursor="hand2"
            )
            btn.pack(pady=8)
            btn.bind("<Enter>", lambda e, n=label: self.on_hover(n))
            btn.bind("<Leave>", lambda e, n=label: self.on_leave(n))
            btn.bind("<Button-1>", lambda e, n=label, s=stats: self.on_select(n, s))
            self.buttons[label] = btn

        back_button = tk.Button(
            self,
            text="Back",
            font=("Arial", 14),
            bg="#444444",
            fg="#c8d6ff",
            activebackground="#555555",
            activeforeground="#ffffff",
            command=lambda: controller.show_name_input_screen(self.selected_class),
        )
        back_button.pack(pady=24)
        
        self._type_job = None
        self.after(200, lambda: self.typewrite("Hover an option to feel the journey..."))
        
    def _set_bg(self, color: str):
        self.configure(bg=color)
        self.title_label.config(bg=color)
        self.flavor.config(bg=color)
        self.flavor_wrap.config(bg=color)
        self.btn_wrap.config(bg=color)
        
    def typewrite(self, text, i=0):
        if i == 0 and self._type_job:
            self.after_cancel(self._type_job)
            self._type_job = None
        
        if i <= len(text):
            self.flavor.config(text=text[:i])
            self._type_job = self.after(12, self.typewrite, text, i + 1)
            
    def compose_flavor(self, difficulty: str) -> str:
        lines = pick_lines(difficulty, self.hero_class)
        return (
            f"{difficulty} — {lines['tagline']}\n"
            f"• {lines['warning']}\n"
            f"• {lines['lore']}\n"
            f"{self.hero_class}: “{lines['voice']}”"
        )
        
    
    def on_hover(self, difficulty: str):
        btn = self.buttons.get(difficulty)
        if btn:
            btn.config(bg="#2d2d2d")
            
        self._set_bg(self.bg_map.get(difficulty, self.bg_default))
        self.typewrite(self.compose_flavor(difficulty))
        
    def _over_any_button(self) -> bool:
        x, y = self.winfo_pointerx(), self.winfo_pointery()
        w = self.winfo_containing(x, y)
        return any(w is b for b in self.buttons.values())
        
    def on_leave(self, difficulty: str):
        btn = self.buttons.get(difficulty)
        if btn:
            btn.config(bg="#222222")
            
        if not self._over_any_button():
            self._set_bg(self.bg_default)
        
    def on_select(self, difficulty_label: str, stats: dict):
        if self._type_job:
            self.after_cancel(self._type_job)
            self._type_job = None
        confirm_line = random.choice([
            f"{difficulty_label} selected. May your steps be steady.",
            f"{difficulty_label} chosen - the path is set.",
            f"{difficulty_label}. Let the tale begin."
        ])
        self.flavor.config(text=confirm_line)
        
        print(f"{self.player_name} the {self.selected_class} chose {difficulty_label} with stats: {stats}")
        self.controller.start_game(
            mode=self.mode,
            player_name=self.player_name,
            selected_class=self.selected_class,
            difficulty=stats
        )

