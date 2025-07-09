import tkinter as tk
from tkinter import messagebox
from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.priest import Priest

class PartySelectionScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.party_members = []
        self.max_party_size = 4
        
        self.configure(bg="black")
        
        tk.Label(self, text="Build Your Party", font=("Arial", 18), fg="blue", bg="black").pack(pady=10)
        tk.Label(self, text="Choose up to 4 characters:", font=("Arial", 12), fg="lightgray", bg="black").pack(pady=5)
        
        name_frame = tk.Frame(self, bg="black")
        name_frame.pack(pady=5)
        tk.Label(name_frame, text="Name", font=("Arial", 12), fg="blue", bg="black").pack(side="left")
        self.name_entry = tk.Entry(name_frame, font=("Arial", 12))
        self.name_entry.pack(side="left")
        
        class_frame = tk.Frame(self, bg="black")
        class_frame.pack(pady=5)
        tk.Label(class_frame, text="Class:", font=("Arial", 12), fg="blue", bg="black").pack(side="left")
        self.class_var = tk.StringVar(value="Warrior")
        tk.OptionMenu(class_frame, self.class_var, "Warrior", "Mage", "Archer", "Priest").pack(side="left")
        
        tk.Button(self, text="Add Member", font=("Arial", 12), command=self.add_member).pack(pady=10)
        
        self.party_display = tk.Label(self, text="", font=("Arial", 12), fg="lightgreen", bg="black", justify="left")
        self.party_display.pack(pady=10)
        
        tk.Button(self, text="Start Battle", font=("Arial", 14), command=self.start_battle).pack(pady=10)
        
        tk.Button(self, text="Back to Intro", font=("Arial", 12), command=self.controller.show_intro_screen).pack(pady=5)
        
    def add_member(self):
        name = self.name_entry.get().strip()
        char_class = self.class_var.get()
        
        if not name:
            messagebox.showwarning("missing Name", "Please enter a name for your character.")
            return
        
        if char_class.lower() == "warrior":
            character = Warrior(name)
        elif char_class.lower() == "mage":
            character = Mage(name)
        elif char_class.lower() == "archer":
            character = Archer(name)
        elif char_class.lower() == "priest":
            character = Priest(name)
        else:
            messagebox.showerror("Error", "Invalid class selected.")
            return
        
        replaced = False
        for i, member in enumerate(self.party_members):
            if isinstance(member, type(character)):
                self.party_members[i] = character
                replaced = True
                break
        
        if not replaced:
            if len(self.party_members) >= self.max_party_size:
                messagebox.showwarning("Party Full", "You can only have up to 4 members in your party.")
                return
            self.party_members.append(character)
            
        self.update_party_display()
        self.name_entry.delete(0, tk.END)
    
    def update_party_display(self):
        display_text = "\n".join(
            [f"{i+1}. {member.name} ({member.__class__.__name__})" for i, member in enumerate(self.party_members)]
        )
        self.party_display.config(text=display_text)
        
    def start_battle(self):
        if not self.party_members:
            tk.messagebox.showwarning("No Party", "You must add at least one character to start the battle.")
            return
        
        self.controller.show_difficulty_selection(
            character_name=None,
            selected_class=None,
            mode="party"
        )
        self.controller.pending_party = self.party_members