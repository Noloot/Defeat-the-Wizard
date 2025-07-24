import tkinter as tk
from PIL import Image, ImageTk
import os

class EndScreen(tk.Frame):
    def __init__(self, parent, controller, message, selected_class=None, party=None):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="black")
        party = party
        
        title = tk.Label(self, text=message, font=("Georgia", 28, "bold"), bg="black")
        title.pack(pady=50)
        
        if "Victory" in message:
            self.animate_victory_text(title, ["purple", "white", "purple"])
            
            if hasattr(controller, "party") and controller.party:
                self.show_party_sprites(controller.party)
            elif selected_class:
                self.show_victory_sprite_jump(selected_class)
        else:
            title.config(fg="red")
        
        tk.Button(self, text="Play Again", font=("Arial", 14), command=controller.show_intro_screen).pack(pady=20)
        
        tk.Button(self, text="Exit", font=("Arial", 14), command=controller.quit).pack(pady=10)
    
    def animate_victory_text(self, label, colors, delay=200, index=0):
            label.config(fg=colors[index % len(colors)])
            self.after(delay, self.animate_victory_text, label, colors, delay, index + 1)
        
    def show_victory_sprite_jump(self, selected_class):
        self.canvas = tk.Canvas(self, width=200, height=200, bg="black", highlightthickness=0)
        self.canvas.pack()
        
        img_path = os.path.join("images", f"{selected_class}.png")
        pil_img = Image.open(img_path).resize((200, 200))
        self.sprite_img = ImageTk.PhotoImage(pil_img)
        
        self.sprite = self.canvas.create_image(90, 100, image=self.sprite_img)
        self.jump_dir = 1
        self.jump_height = 0
        self.max_jump = 20
        
        self.animate_jump()
        
    def show_party_sprites(self, party):
        canvas_width = 700
        sprite_size = 80
        spacing = 20
        total_width = len(party) * sprite_size + (len(party) - 1) * spacing
        start_x = (canvas_width - total_width) // 2
        
        self.canvas = tk.Canvas(self, width=700, height=200, bg="black", highlightthickness=0)
        self.canvas.pack(pady=10)
        
        self.party_sprites = []
        self.sprite_ids = []
        self.jump_dirs = []
        self.jump_heights = []
        self.max_jump = 20
        
        for i, member in enumerate(party):
            char_class = member.__class__.__name__.lower()
            try:
                img_path = os.path.join("images", f"{char_class}.png")
                sprite = Image.open(img_path).resize((sprite_size, sprite_size))
                sprite_img = ImageTk.PhotoImage(sprite)
                
                self.party_sprites.append(sprite_img)
                x = start_x + i * (sprite_size + spacing)
                sprite_id = self.canvas.create_image(x, 100, image=sprite_img)
                self.sprite_ids.append(sprite_id)
                self.jump_dirs.append(1)
                self.jump_heights.append(0)
            except Exception as e:
                print(f"Error loading sprite for {char_class}: {e}")
        
        self.animate_party_jump()
        
    def animate_jump(self):
        dy = -3 * self.jump_dir
        self.jump_height += dy
        
        self.canvas.move(self.sprite, 0, dy)
        
        if abs(self.jump_height) >= self.max_jump:
            self.jump_dir *= -1
            
        self.after(80, self.animate_jump)
    
    def animate_party_jump(self):
        for i, sprite_id in enumerate(self.sprite_ids):
            dy = -3 * self.jump_dirs[i]
            self.jump_heights[i] += dy
            self.canvas.move(sprite_id, 0, dy)
            
            if abs(self.jump_heights[i]) >= self.max_jump:
                self.jump_dirs[i] *= -1
                
        self.after(80, self.animate_party_jump)