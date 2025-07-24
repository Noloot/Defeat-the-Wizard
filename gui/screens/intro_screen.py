import tkinter as tk
import os
from PIL import Image, ImageTk

class IntroScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        img_path = os.path.join("images", "intro_screen_1.png")
        bg_image = Image.open(img_path).resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.configure(bg="black")
        
        title = tk.Label(
            self, 
            text="THE DARK WIZARD", 
            font=("Georgia", 36, "bold"), 
            fg="orange", 
            bg="#000000"
        )
        title.place(relx=0.5, y=60, anchor="center")
        
        subtitle = tk.Label(
            self, 
            text="A Fantasy Battle RPG", 
            font=("Arial", 20), 
            fg="White", 
            bg="#000000"
        )
        subtitle.place(relx=0.5, y=120, anchor="center")
        
        start_button = tk.Button(
            self, 
            text="Solo Adventure", 
            font=("Arial", 16), 
            bg="#222", 
            fg="blue", 
            command=self.start_game
        )
        start_button.place(relx=0.5, y=500, anchor="center")
        
        party_mode = tk.Button(
            self,
            text="Build a Party",
            font=("Arial", 16),
            bg="#222",
            fg="blue",
            command=self.controller.show_party_select_screen
        )
        party_mode.place(relx=0.5, y=550, anchor="center")
        
    def start_game(self):
        
        print("Game Starting...")
        
        self.controller.show_character_select_screen()