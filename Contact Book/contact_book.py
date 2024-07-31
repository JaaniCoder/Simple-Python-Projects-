import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db():
    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL,
                   email TEXT NOT NULL
        )
    ''')
    con.commit()
    con.close()

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if not name or not phone or not email:
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    
    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()
    cursor.execute('''
            INSERT INTO contacts (name, phone, email)
                   VALUES (?, ?, ?)
                   ''', (name, phone, email))
    con.commit()
    con.close()

    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    messagebox.showinfo("Success", "Contact added successfully!")
    view_contacts()

def view_contacts():
    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()
    con.close()

    listbox_contacts.delete(0, tk.END)
    for row in rows:
        listbox_contacts.insert(tk.END, f"{row[1]} - {row[2]} - {row[3]}")

def delete_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showwarning("Selection Error", "No contact selected.")
        return
    
    contact_details = selected_contact.split(" - ")
    name = contact_details[0]

    con = sqlite3.connect('contacts.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM contacts WHERE name = ?', (name,))
    con.commit()
    con.close()

    messagebox.showinfo("Success", "Contact deleted successfully!")
    view_contacts()

root = tk.Tk()
root.title("Contact Book Interface")
root.geometry("450x450")
root.resizable(False, False)
root.config(bg="#f0f0f0")

label_title = tk.Label(root, text="Contact Book", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

frame_form = tk.Frame(root, bg="#f0f0f0")
frame_form.pack(pady=10)

label_name = tk.Label(frame_form, text="Name:", bg="#f0f0f0")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_form)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_phone = tk.Label(frame_form, text="Phone:", bg="#f0f0f0")
label_phone.grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_form)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

label_email = tk.Label(frame_form, text="Email:", bg="#f0f0f0")
label_email.grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_form)
entry_email.grid(row=2, column=1, padx=5, pady=5)

button_add = tk.Button(root, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white")
button_add.pack(pady=10)

label_contacts = tk.Label(root, text="Contacts:", bg="#f0f0f0")
label_contacts.pack(pady=5)

listbox_contacts = tk.Listbox(root, width=50)
listbox_contacts.pack(pady=5)

button_delete = tk.Button(root, text="Delete Contact", command=delete_contact, bg="#f44336", fg="white")
button_delete.pack(pady=10)

init_db()
view_contacts()

root.mainloop()