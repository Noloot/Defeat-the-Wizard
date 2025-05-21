import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("400x300")

label = tk.Label(root, text="If you see this, Tkinter works!", font=("Arial", 16))
label.pack(pady=100)

root.mainloop()
