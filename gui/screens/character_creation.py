import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import os

class CharacterSelectScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="gray20")
        
        self.char_order = ["warrior", "mage", "archer", "priest"]
        self.selected = None
        self.silhouettes = {}
        self.image_labels = []
        self.tk_images = {}
        
        self.index = 0
        
        self.canvas = tk.Canvas(self, width=800, height=600, bg="gray20", highlightthickness=0)
        self.canvas.pack(pady=40)
        
        self.images = []
        self.image_ids = []
        self.load_images()
        
        nav_left = tk.Button(self.canvas, text="<<", font=("Arial", 14), bg="#333", fg="white", command=self.show_next)
        nav_right = tk.Button(self.canvas, text=">>", font=("Arial", 14), bg="#333", fg="white", command=self.show_previous)
        
        select_button = tk.Button(self.canvas, text="Select", font=("Arial", 16,), bg="#222", fg="blue", command=self.select_character)
        back_button = tk.Button(self.canvas, text="Back", font=("Arial", 14), bg="#444", fg="blue", command=self.controller.show_intro_screen)
        
        self.canvas.create_window(250, 480, window=nav_left)
        self.canvas.create_window(550, 480, window=nav_right)
        self.canvas.create_window(450, 480, window=select_button)
        self.canvas.create_window(350, 480, window=back_button)
        
        self.draw_characters()
        
    def load_images(self):
        self.detailed_images = []
        self.silhouette_images = []
        self.background_images = []
        
        for char in self.char_order:
            sil_path = os.path.join("images", f"{char}_silhouette.png")
            det_path = os.path.join("images", f"{char}_detailed.png")
            bg_path = os.path.join("images", f"{char}_background.png")
            
            silhouette = Image.open(sil_path).convert("RGBA")
            detailed = Image.open(det_path).convert("RGBA")
            background = Image.open(bg_path).convert("RGBA")
            
            self.silhouette_images.append(silhouette)
            self.detailed_images.append(detailed)
            self.background_images.append(background)

    def draw_characters(self):
        self.tk_images.clear()
        for img_id, _ in getattr(self, "image_ids", []):
            self.canvas.delete(img_id)
        self.image_ids = []
        
        bg_img = self.background_images[self.index].resize((800, 600), Image.LANCZOS)
        bg_tk = ImageTk.PhotoImage(bg_img)
        self.canvas.create_image(0, 0, image=bg_tk, anchor="nw")
        self.canvas.bg_tk = bg_tk
        
        positions = [200, 400, 600]
        for i, offset in enumerate([-1, 0, 1]):
            char_index = (self.index + offset) % len(self.char_order)
            x_pos = positions[offset + 1]
            
            
            if offset == 0:
                img = self.detailed_images[char_index].resize((220, 220), Image.LANCZOS)
                img_bright = ImageEnhance.Brightness(img).enhance(1.0)
                tk_img = ImageTk.PhotoImage(img_bright)
                img_id = self.canvas.create_image(x_pos, 200, image=tk_img, anchor="center")
                self.tk_images[img_id] = tk_img
                self.image_ids.append((img_id, tk_img))
                coords = self.canvas.coords(img_id)
                
                def on_enter(event, idx=char_index, item_id=img_id, pos=coords):
                    enlarged = self.detailed_images[idx].resize((250, 250), Image.LANCZOS)
                    glow = ImageEnhance.Brightness(enlarged).enhance(2.0)
                    glow_img = ImageTk.PhotoImage(glow)
                    self.canvas.itemconfig(item_id, image=glow_img)
                    self.canvas.coords(item_id, *pos)
                    self.tk_images[item_id] = glow_img
                
                def on_leave(event, idx=char_index, item_id=img_id, pos=coords):
                    normal = self.detailed_images[idx].resize((220, 220), Image.LANCZOS)
                    normal_img = ImageTk.PhotoImage(normal)
                    self.canvas.itemconfig(img_id, image=normal_img)
                    self.canvas.coords(item_id, *pos)
                    self.tk_images[item_id] = normal_img
                    
                def on_click(event, idx=char_index):
                    self.select_character()
                    
                self.canvas.tag_bind(img_id, "<Enter>", on_enter)
                self.canvas.tag_bind(img_id, "<Leave>", on_leave)
                self.canvas.tag_bind(img_id, "<Button-1>", on_click)
            elif offset != 0:
                img = self.silhouette_images[char_index].resize((150, 150), Image.LANCZOS)
                alpha = img.split()[-1].point(lambda p: p * 0.3)
                img.putalpha(alpha)
                img = ImageEnhance.Brightness(img).enhance(0.5)
                tk_img = ImageTk.PhotoImage(img)
                img_id = self.canvas.create_image(x_pos, 200, image=tk_img, anchor="center")
                self.tk_images[img_id] = tk_img
                self.image_ids.append((img_id, tk_img))
        
    def show_previous(self):
        self.index = (self.index + 1) % len(self.char_order)
        self.animate_slide(-1)
        
    def show_next(self):
        self.index = (self.index - 1) % len(self.char_order)
        self.animate_slide(1)
        
    def animate_slide(self, direction, step=0):
        dx = 10 * direction
        if step < 20:
            for img_id, _ in self.image_ids:
                self.canvas.move(img_id, dx, 0)
            self.after(15, lambda: self.animate_slide(direction, step + 1))
        else:
            self.draw_characters()
        
    def select_character(self):
        selected = self.char_order[self.index]
        print(f"Character selected: {selected}")
        self.controller.show_name_input_screen(selected)