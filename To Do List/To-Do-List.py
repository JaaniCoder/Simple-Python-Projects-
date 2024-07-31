import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import PIL

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Add a logo icon
Image_icon = ImageTk.PhotoImage(file="name.jpg")
root.iconphoto(False, Image_icon)

logo = Image.open("dock.jpg")
logo = logo.resize((100, 100), PIL.Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo, bg="white")
logo_label.pack(pady=10)

# Main frame
main_frame = tk.Frame(root, bg="white")
main_frame.pack(pady=10)

# Task entry
task_entry = tk.Entry(main_frame, font=("Helvetica", 14), width=25)
task_entry.grid(row=0, column=0, padx=10)

# Add task button
add_task_button = tk.Button(main_frame, text="Add Task", font=("Helvetica", 14), command=add_task)
add_task_button.grid(row=0, column=1, padx=10)

# Task listbox
task_listbox = tk.Listbox(main_frame, font=("Helvetica", 14), width=35, height=10, bg="lightgrey", bd=0, fg="black", selectbackground="skyblue", selectforeground="black")
task_listbox.grid(row=1, column=0, columnspan=2, pady=20)

# Scrollbar for the listbox
task_scrollbar = tk.Scrollbar(main_frame)
task_scrollbar.grid(row=1, column=2, sticky="ns")

# Configure the scrollbar
task_listbox.config(yscrollcommand=task_scrollbar.set)
task_scrollbar.config(command=task_listbox.yview)

# Button frame
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

# Delete task button
delete_task_button = tk.Button(button_frame, text="Delete Task", font=("Helvetica", 14), command=delete_task)
delete_task_button.grid(row=0, column=0, padx=10)

# Clear all tasks button
clear_tasks_button = tk.Button(button_frame, text="Clear All Tasks", font=("Helvetica", 14), command=clear_tasks)
clear_tasks_button.grid(row=0, column=1, padx=10)

# Main loop
root.mainloop()