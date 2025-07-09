import tkinter as tk
from tkinter import messagebox
import pygame
import math
import numpy
import os

def make_beep_sound(frequency=440, duration_ms=100, volume=0.5):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sample_rate = 44100
    n_samples = int(round(duration_ms * sample_rate/1000))
    waveform = (volume * (2**15 - 1) *
                    numpy.sin(2.0 * math.pi * frequency * numpy.arange(n_samples)/sample_rate)
                ).astype(numpy.int16)
    stereo_waveform = numpy.column_stack((waveform, waveform))
    return pygame.sndarray.make_sound(stereo_waveform)

class BattleScreen(tk.Frame):
    def __init__(self, parent, controller, party, wizard, attack_callback, special_callback, heal_callback):
        super().__init__(parent)
        self.controller = controller
        self.party = party if isinstance(party, list) else [party]
        self.wizard = wizard
        self.active_index = 0
        self.player = self.party[self.active_index]
        self.attack_callback = attack_callback
        self.special_callback = special_callback
        self.heal_callback = heal_callback
        pygame.mixer.init()
        
        self.attack_sounds = {
            "warrior": pygame.mixer.Sound(os.path.join("sounds", "slash1.ogg")),
            "mage": pygame.mixer.Sound(os.path.join("sounds", "mage.wav")),
            "archer": pygame.mixer.Sound(os.path.join("sounds", "arrow.wav")),
            "priest": pygame.mixer.Sound(os.path.join("sounds", "priest.wav"))
        }
        
        self.special_sounds = {
            "deadly_strike": pygame.mixer.Sound(os.path.join("sounds", "Deadly_Strike.wav")),
            "berserk": pygame.mixer.Sound(os.path.join("sounds", "berserk.wav")),
            "evolution": pygame.mixer.Sound(os.path.join("sounds", "evolution_success.wav")),
            "failed_evolution": pygame.mixer.Sound(os.path.join("sounds", "failed_evolution.wav"))
        }
        
        self.configure(bg="black")
        
        self.party_stats_frame = tk.Frame(self, bg="black")
        self.party_stats_frame.pack(pady=5)
        self.player_stats_labels = []
        
        for member in self.party:
            label = tk.Label(self.party_stats_frame, text=self.get_individual_stats(member), font=("Arial", 12), fg="lightgreen", bg="black")
            label.pack()
            self.player_stats_labels.append(label)
        
        self.status = tk.Label(self, text="Battle Begins!", font=("Arial", 16), fg="blue", bg="black")
        self.status.pack(pady=10)
        
        self.turn_label = tk.Label(self, text=f"{self.player.name}'s Turn", font=("Arial", 14), fg="yellow", bg="black")
        self.turn_label.pack(pady=5)
        
        self.wizard_stats = tk.Label(self, text=self.get_wizard_stats(), font=("Arial", 14), fg="lightcoral", bg="black")
        self.wizard_stats.pack(pady=5)
        
        log_label = tk.Label(self, text="Battle Log", font=("Arial", 14, "bold"), fg="blue", bg="black")
        log_label.pack(pady=(20, 5))
        
        log_frame = tk.Frame(self, bg="black")
        log_frame.pack(pady=(0, 20), fill="x")
        
        self.battle_log = tk.Text(log_frame, height=10, width=60, bg="black", fg="lightgrey", font=("Courier", 10), state="disabled", wrap="word")
        self.battle_log.pack(side="left", fill="y", expand=False)
        
        scrollbar = tk.Scrollbar(log_frame, command=self.battle_log.yview)
        scrollbar.pack(side="right", fill="y")
        self.battle_log.configure(yscrollcommand=scrollbar.set)
        
        self.action_btn_frame = tk.Frame(self, bg="black")
        self.action_btn_frame.pack(pady=10)

        self.special_frame = tk.Frame(self, bg="black")
        
        tk.Button(self.action_btn_frame, text="Attack", font=("Arial", 14), width=12, command=self.attack).pack(pady=10)
        tk.Button(self.action_btn_frame, text="Special", font=("Arial", 14), width=12, command=self.special).pack(pady=10)
        tk.Button(self.action_btn_frame, text="Heal", font=("Arial", 14), width=12, command=self.heal).pack(pady=10)
        
    def get_player_stats(self):
        return f"{self.player.name}: {self.player.health}/{self.player.max_health} HP | Power: {self.player.attack_power}"
    
    def get_wizard_stats(self):
        if self.wizard.health <= 0:
            return f"{self.wizard.name}: DEFEATED"
        return f"{self.wizard.name}: {self.wizard.health}/{self.wizard.max_health} HP | Power: {self.wizard.attack_power}"
    
    def update_stats(self):
        for i, member in enumerate(self.party):
            text = self.get_individual_stats(member)
            if i == self.active_index:
                text += " Active"
            self.player_stats_labels[i].config(text=text)
        
        
    def get_individual_stats(self, player):
        return f"{player.name}: {player.health}/{player.max_health} HP | Power: {player.attack_power}"
        
    def log_message(self, message):
        self.battle_log.configure(state="normal")
        self.battle_log.insert("end", message + "\n")
        self.battle_log.see("end")
        self.battle_log.configure(state="disabled")
        
    def update_turn_label(self):
        self.turn_label.config(text=f"{self.player.name}'s Turn")
        
    def attack(self):
        class_name = self.player.__class__.__name__.lower()
        
        if class_name in self.attack_sounds:
            self.attack_sounds[class_name].play()
        else:
            make_beep_sound().play()
            
        self.attack_callback()
        self.wizard_stats.config(text=self.get_wizard_stats())
        self.log_message(f"{self.player.name} attacks {self.wizard.name}!")
        self.status.config(text=f"{self.player.name} attacks!")
        self.check_battle_state()
        
    def special(self):
    # Hide the action buttons
        self.action_btn_frame.pack_forget()

    # Clear and show special options
        for widget in self.special_frame.winfo_children():
            widget.destroy()

        self.special_frame.pack(pady=10)

        class_name = self.player.__class__.__name__.lower()
        if class_name == "warrior":
            self.show_warrior_specials()
        elif class_name == "mage":
            self.show_mage_specials()
        elif class_name == "priest":
            self.show_priest_specials()
        elif class_name == "archer":
            self.show_archer_specials()
            
    # Warrior Powers
    def show_warrior_specials(self):
        # Add Deadly Strike
        tk.Button(
            self.special_frame,
            text="Deadly Strike",
            font=("Arial", 12),
            command=self.use_deadly_strike
        ).pack(pady=5)

    # Add Berserk
        tk.Button(
            self.special_frame,
            text="Berserk",
            font=("Arial", 12),
            command=self.activate_berserk
        ).pack(pady=5)

    # Add Evolution
        tk.Button(
            self.special_frame,
            text="Attempt Evolution",
            font=("Arial", 12),
            command=self.attempt_evolution
        ).pack(pady=5)

    # Add cancel button
        tk.Button(
            self.special_frame,
            text="Cancel",
            font=("Arial", 12),
            command=lambda: [self.special_frame.pack_forget(), self.action_btn_frame.pack(pady=10)]
        ).pack(pady=5)

        self.status.config(text="Choose a special ability")
        
    # Mage Powers
    def show_mage_specials(self):
        tk.Button(
            self.special_frame,
            text="Meteor Strike",
            font=("Arial", 12),
            command=self.use_meteor_strike
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Ice Storm",
            font=("Arial", 12),
            command=self.use_ice_storm
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Attempt Evolution",
            font=("Arial", 12),
            command=self.attempt_evolution
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Cancel",
            font=("Arial", 12),
            command=lambda: [self.special_frame.pack_forget(), self.action_btn_frame.pack(pady=10)]
        ).pack(pady=5)
    
    # Priest Power
    def show_priest_specials(self):
        tk.Button(
            self.special_frame,
            text="Max Health Regen",
            font=("Arial", 12),
            command=self.use_max_health_regen
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Holy Light",
            font=("Arial", 12),
            command=self.use_holy_light
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Attempt Evolution",
            font=("Arial", 12),
            command=self.attempt_evolution
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Cancel",
            font=("Arial", 12),
            command=lambda: [self.special_frame.pack_forget(), self.action_btn_frame.pack(pady=10)]
        ).pack(pady=5)
        
    # Archer Power
    def show_archer_specials(self):
        tk.Button(
            self.special_frame,
            text="Arrow Rain",
            font=("Arial", 12),
            command=self.use_arrow_rain
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Quick Evade",
            font=("Arial", 12),
            command=self.use_quick_evade
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Attempt Evolution",
            font=("Arial", 12),
            command=self.attempt_evolution
        ).pack(pady=5)
        
        tk.Button(
            self.special_frame,
            text="Cancel",
            font=("Arial", 12),
            command=lambda: [self.special_frame.pack_forget(), self.action_btn_frame.pack(pady=10)]
        ).pack(pady=5)      
    
    # Warrior Specials
    
    def use_deadly_strike(self):
        result = self.player.use_deadly_strike(self.wizard)
        self.special_sounds["deadly_strike"].play()
        self.log_message(result)
        self.status.config(text=result)
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.check_battle_state()

    def activate_berserk(self):
        result = self.player.activate_berserk()
        self.special_sounds["berserk"].play()
        self.log_message(result)
        self.status.config(text=result)
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.update_stats()

        
    # Mage Specials
    
    def use_meteor_strike(self):
        result = self.player.use_meteor_strike(self.wizard)
        self.log_message(result)
        self.status.config(text=result)
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.check_battle_state()
        
    def use_ice_storm(self):
        result = self.player.use_ice_storm(self.wizard)
        self.log_message(result)
        self.status.config(text=result)
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.check_battle_state()
    
    # Priest Special
    
    def use_max_health_regen(self):
        result = self.player.use_max_health_regen()
        self.log_message(result)
        self.status.config(text=result)
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.check_battle_state()
        
    def use_holy_light(self):
        result = self.player.use_holy_light(self.wizard)
        self.log_message(result)
        self.status.config(text=result)
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.check_battle_state()
    
    # Archer Special
    
    def use_arrow_rain(self):
        result = self.player.use_arrow_rain(self.wizard)
        self.log_message(result)
        self.status.config(text=result)
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.check_battle_state()
        
    def use_quick_evade(self):
        result = self.player.use_quick_evade(self.wizard)
        self.log_message(result)
        self.status.config(text=result)
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.check_battle_state()

    def attempt_evolution(self):
        result = self.player.attempt_evolution(self.wizard)
        self.log_message(result)
        
        if "success" in result.lower() or "evolved" in result.lower():
            self.special_sounds["evolution"].play()
        else:
            self.special_sounds["failed_evolution"].play()
            
        self.status.config(text="Evolution attempt finished.")
        self.special_frame.pack_forget()
        self.action_btn_frame.pack(pady=10)
        self.update_stats()
        
    # def hide_special_options(self):
    #     self.special_frame.pack_forget()
        
    def heal(self):
        self.heal_callback()
        self.log_message(f"{self.player.name} heals.")
        self.status.config(text=f"{self.player.name} heals.")
        self.update_stats()
        
    def check_battle_state(self):
        self.update_stats()
        self.log_message("-" * 50)
        
        if self.wizard.health <= 0:
            messagebox.showinfo("Victory", f"{self.player.name} has defeated the Dark Wizard!")
            self.controller.show_intro_screen()
            return
            
        if all(p.health <= 0 for p in self.party):
            messagebox.showerror("Defeat", "The entire party has fallen")
            self.controller.show_intro_screen()
            return
        
        self.wizard_turn()
        
        while True:
            self.active_index = (self.active_index + 1) % len(self.party)
            self.player = self.party[self.active_index]
            if self.player.health > 0:
                break                 
        self.status.config(text=f"{self.player.name}'s turn!")
        self.update_turn_label()

    def wizard_turn(self):
        if getattr(self.player, "evade_next", False):
            self.log_message(f"{self.player.name} evades the attack!")
            self.status.config(text=f"{self.player.name} evades the Dark Wizard's strike!")
            self.player.evade_next = False
            return
        
        self.wizard.attack(self.player)
        self.log_message(f"{self.wizard.name} attacks {self.player.name}")
        self.status.config(text=f"{self.wizard.name} attacks {self.player.name}!")
        self.update_stats()
        
        if self.player.health <= 0:
            self.log_message(f"{self.player.name} has fallen in battle!")