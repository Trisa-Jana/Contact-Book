import tkinter as tk
from tkinter import messagebox, simpledialog


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # GUI Setup
        self.setup_gui()

    def setup_gui(self):
        # Add Contact Button
        add_btn = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        add_btn.pack(pady=5)

        # View Contacts Button
        view_btn = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        view_btn.pack(pady=5)

        # Search Contact Button
        search_btn = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        search_btn.pack(pady=5)

        # Update Contact Button
        update_btn = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        update_btn.pack(pady=5)

        # Delete Contact Button
        delete_btn = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        delete_btn.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter Name:")
        if not name:
            messagebox.showwarning("Warning", "Name cannot be empty!")
            return
        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists!")
            return

        phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
        if not phone:
            messagebox.showwarning("Warning", "Phone number cannot be empty!")
            return

        email = simpledialog.askstring("Add Contact", "Enter Email Address:")
        address = simpledialog.askstring("Add Contact", "Enter Address:")

        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contact List", "No contacts available.")
            return

        # Display only the name and phone number of each contact
        contact_list = "\n".join([f"Name: {name}, Phone: {info['phone']}" for name, info in self.contacts.items()])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
        if not search_term:
            messagebox.showwarning("Warning", "Search term cannot be empty!")
            return

        found_contacts = {name: info for name, info in self.contacts.items() if search_term.lower() in name.lower() or search_term in info['phone']}

        if not found_contacts:
            messagebox.showinfo("Search Results", "No contacts found.")
            return

        contact_list = ""
        for name, info in found_contacts.items():
            contact_list += f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n\n"

        messagebox.showinfo("Search Results", contact_list)

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter Name of the Contact to Update:")
        if not name:
            messagebox.showwarning("Warning", "Name cannot be empty!")
            return
        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return

        new_phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:")
        new_email = simpledialog.askstring("Update Contact", "Enter New Email Address:")
        new_address = simpledialog.askstring("Update Contact", "Enter New Address:")

        self.contacts[name] = {'phone': new_phone, 'email': new_email, 'address': new_address}
        messagebox.showinfo("Success", f"Contact '{name}' updated.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter Name of the Contact to Delete:")
        if not name:
            messagebox.showwarning("Warning", "Name cannot be empty!")
            return
        if name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return

        del self.contacts[name]
        messagebox.showinfo("Success", f"Contact '{name}' deleted.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
