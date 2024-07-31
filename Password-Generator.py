import tkinter as tk
from tkinter import messagebox
import random
import string

def pwd_gen():
    length = int(entry_length.get())
    if length < 1:
        messagebox.showerror("Error", "Length must be greater than 0")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    
def copy_to_cb():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showerror("Error", "No password to copy")

root = tk.Tk()
root.title("Password Generator Interface")
root.geometry("450x250")
root.resizable(False, False)

label_length = tk.Label(root, text="Password Length:", font=("Helvetica", 12))
label_length.pack(pady=5)

entry_length = tk.Entry(root, font=("Helvetica", 12))
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=pwd_gen)
button_generate.pack(pady=10)

entry_password = tk.Entry(root, font=("Hevetica", 12), width=30)
entry_password.pack(pady=5)

button_copy = tk.Button(root, text="Copy to Clipbaord", font=("Helvetica", 12), command=copy_to_cb)
button_copy.pack(pady=10)

root.mainloop()