import tkinter as tk
from PIL import Image, ImageTk
import os

class EndScreen(tk.Frame):
    def __init__(self, parent, controller, message, selected_class=None):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="black")
        
        title = tk.Label(self, text=message, font=("Georgia", 28, "bold"), bg="black")
        title.pack(pady=50)
        
        if "Victory" in message and selected_class:
            try:
                img_path = os.path.join("images", f"{selected_class}.png")
                sprite = Image.open(img_path)
                sprite = sprite.resize((50, 50))
                self.sprite_img = ImageTk.PhotoImage(sprite)
                img_label = tk.Label(self, image=self.sprite_img, bg="black")
                img_label.pack(pady=10)
            except Exception as e:
                print(f"Could not load image for {selected_class}: {e}")
        
        if "Victory" in message:
            self.animate_victory_text(title, ["purple", "white", "purple"])
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
        
    def animate_jump(self):
        dy = -3 * self.jump_dir
        self.jump_height += dy
        
        self.canvas.move(self.sprite, 0, dy)
        
        if abs(self.jump_height) >= self.max_jump:
            self.jump_dir *= -1
            
        self.after(80, self.animate_jump)