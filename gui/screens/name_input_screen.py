import tkinter as tk
from PIL import Image, ImageTk

class NameInputScreen(tk.Frame):
    def __init__(self, parent, controller, selected_class):
        super().__init__(parent)
        self.controller = controller
        self.selected_class = selected_class
        
        self.canvas = tk.Canvas(self, width=800, height=600, highlightthickness=0)
        self.canvas.pack()
        
        bg_map = {
            "warrior": "images/warrior_background.png",
            "mage": "images/mage_background.png",
            "archer": "images/archer_background.png",
            "priest": "images/priest_background.png"
        }
        
        image_path = bg_map.get(self.selected_class, "images/default_background.png")
        image = Image.open(image_path).resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        self.canvas.create_text(
            400, 60,
            text="Name Your Hero",
            font=("Georgia", 28, "bold"),
            fill="white",
            tags="name_text"
        )
        
        self.canvas.create_text(
            400, 120,
            text="Type your hero's name below:",
            font=("Georgia", 16),
            fill="white"
        )
        
        entry_frame = tk.Frame(self, bg="white", highlightthickness=2, highlightbackground="blue")
        self.canvas.create_window(400, 150, window=entry_frame)
        
        self.name_entry = tk.Entry(
            entry_frame,
            font=("Georgia", 16, "bold"),
            fg="white",
            bg="#1c1c1c",
            insertbackground="white",
            bd=0,
            highlightthickness=0,
            justify="center"
        )
        self.name_entry.pack(padx=2, pady=2)
        
        self.add_placeholder()

        # Continue Button
        continue_button = tk.Button(
            self, text="Continue",
            font=("Arial", 14), bg="#222", fg="blue",
            command=self.on_submit
        )
        self.canvas.create_window(400, 220, window=continue_button)

        # Back Button
        back_button = tk.Button(
            self, text="Back",
            font=("Arial", 12), bg="#222", fg="blue",
            command=self.go_back
        )
        self.canvas.create_window(60, 550, window=back_button)
        
    def add_placeholder(self):
        self.name_entry.insert(0, "Enter your name...")
        self.name_entry.config(fg="grey")
        
        def on_focus_in(event):
            if self.name_entry.get() == "Enter your name...":
                self.name_entry.delete(0, "end")
                self.name_entry.config(fg="white")
                
        def on_focus_out(event):
            if not self.name_entry.get():
                self.name_entry.insert(0, "Enter your name...")
                self.name_entry.config(fg="grey")
                
        self.name_entry.bind("<FocusIn>", on_focus_in)
        self.name_entry.bind("<FocusOut>", on_focus_out)

    def on_submit(self):
        name = self.name_entry.get().strip()
        if name:
            print(f"Character created: {self.selected_class} named {name}")
            self.controller.show_difficulty_selection(name, self.selected_class)
        else:
            print("Please enter a name before continuing.")


    def go_back(self):
        # Navigate back to character selection or previous screen
        self.controller.show_character_select_screen()

        
        self.name_entry = tk.Entry(self, font=("Arial", 16))
        self.canvas.create_window(400, 150, window=self.name_entry)
        
        submit_button = tk.Button(self, text="Continue", font=("Arial", 14), bg="#444", fg="white", command=self.on_submit)
        self.canvas.create_window(400, 220, window=submit_button)
        