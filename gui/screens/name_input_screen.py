import tkinter as tk

class NameInputScreen(tk.Frame):
    def __init__(self, parent, controller, selected_class):
        super().__init__(parent)
        self.controller = controller
        self.selected_class = selected_class
        
        self.configure(bg="black")
        
        title = tk.Label(self, text="Name Your Hero", font=("Georgia", 24, "bold"), fg="blue", bg="black")
        title.pack(pady=40)
        
        prompt = tk.Label(self, text=f"Enter a name for your {selected_class}:", font=("Arial", 16), fg="white", bg="black")
        prompt.pack(pady=10)
        
        self.name_entry = tk.Entry(self, font=("Arial", 16))
        self.name_entry.pack(pady=20)
        
        submit_button = tk.Button(self, text="Continue", font=("Arial", 14), bg="#444", fg="blue", command=self.submit_name)
        submit_button.pack(pady=20)
        
        back_button = tk.Button(self, text="Back", font=("Arial", 12), bg="#222", fg="blue", command=lambda: controller.show_character_select())
        back_button.pack(pady=10)
    
    def select_character(self, char_type):
        self.controller.show_name_input_screen(char_type.capitalize())
        
    def submit_name(self):
        name = self.name_entry.get().strip()
        if name:
            print(f"Character created: {self.selected_class} name {name}")
            self.controller.show_difficulty_selection(name, self.selected_class)
        else:
            print("Please enter a name before continuing.")
            