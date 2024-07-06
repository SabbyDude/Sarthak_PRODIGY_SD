import tkinter as tk
from tkinter import messagebox
import json

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = self.load_contacts()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)
        tk.Label(self.root, text="Phone:").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1)
        tk.Label(self.root, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=3, column=0)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=3, column=1)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            self.contacts[name] = {"phone": phone, "email": email}
            self.save_contacts()
            messagebox.showinfo("Success", "Contact added successfully!")
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields are required!")

    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Contacts")
        row = 0
        for name, info in self.contacts.items():
            tk.Label(view_window, text=name).grid(row=row, column=0)
            tk.Label(view_window, text=info["phone"]).grid(row=row, column=1)
            tk.Label(view_window, text=info["email"]).grid(row=row, column=2)
            tk.Button(view_window, text="Edit", command=lambda n=name: self.edit_contact(n)).grid(row=row, column=3)
            tk.Button(view_window, text="Delete", command=lambda n=name: self.delete_contact(n)).grid(row=row, column=4)
            row += 1

    def edit_contact(self, name):
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit Contact - {name}")
        tk.Label(edit_window, text="Name:").grid(row=0, column=0)
        name_entry = tk.Entry(edit_window)
        name_entry.grid(row=0, column=1)
        name_entry.insert(0, name)
        tk.Label(edit_window, text="Phone:").grid(row=1, column=0)
        phone_entry = tk.Entry(edit_window)
        phone_entry.grid(row=1, column=1)
        phone_entry.insert(0, self.contacts[name]["phone"])
        tk.Label(edit_window, text="Email:").grid(row=2, column=0)
        email_entry = tk.Entry(edit_window)
        email_entry.grid(row=2, column=1)
        email_entry.insert(0, self.contacts[name]["email"])
        save_button = tk.Button(edit_window,
                                text="Save Changes",
                                command=lambda: self.save_edited_contact(name,
                                                                         name_entry.get(),
                                                                         phone_entry.get(),
                                                                         email_entry.get(),
                                                                         edit_window))
        
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def save_edited_contact(self, old_name, new_name, new_phone, new_email, edit_window):
        if old_name in self.contacts:
            del self.contacts[old_name]  
            self.contacts[new_name] = {"phone": new_phone, "email": new_email}  
            self.save_contacts()
            messagebox.showinfo("Success", "Contact updated successfully!")
            edit_window.destroy()
        else:
            messagebox.showerror("Error", "Contact not found!")

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=4)

root = tk.Tk()
app = ContactApp(root)
root.mainloop()