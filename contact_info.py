import tkinter as tk  
from tkinter import messagebox, simpledialog  

class Contact:  
    def __init__(self, name, phone, email, address):  
        self.name = name  
        self.phone = phone  
        self.email = email  
        self.address = address  

class ContactManager:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Contact Management System")  

        self.contacts = []
        
        # Entry fields for contact information name,phone,email,address

        #name
        self.name_label = tk.Label(root, text="Name:",font=("Comic Sans MS",15))  
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)  
        self.name_entry.grid(row=0, column=1)

        #phone
        self.phone_label = tk.Label(root, text="Phone:",font=("Comic Sans MS",15))  
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)  
        self.phone_entry = tk.Entry(root)  
        self.phone_entry.grid(row=1, column=1)
        
        #email
        self.email_label = tk.Label(root, text="Email:",font=("Comic Sans MS",15))  
        self.email_label.grid(row=2, column=0, padx=10, pady=5)  
        self.email_entry = tk.Entry(root)  
        self.email_entry.grid(row=2, column=1)  

        #adreess
        self.address_label = tk.Label(root, text="Address:",font=("Comic Sans MS",15))  
        self.address_label.grid(row=3, column=0, padx=10, pady=5)  
        self.address_entry = tk.Entry(root)  
        self.address_entry.grid(row=3, column=1)
        
        # Add Contact button 
        self.add_button = tk.Button(root, text="Add Contact",font=("Comic Sans MS",15), command=self.add_contact)  
        self.add_button.grid(row=4, column=0, padx=10, pady=5)
        self.add_button.config(bg="yellow",fg="black")
        
        #view contact button
        self.view_button = tk.Button(root, text="View Contacts",font=("Comic Sans MS",15), command=self.view_contacts)  
        self.view_button.grid(row=4, column=1, padx=10, pady=5)
        self.view_button.config(bg="yellow",fg="black")
        
        #Search Contact button  
        self.search_button = tk.Button(root, text="Search Contact",font=("Comic Sans MS",15), command=self.search_contact)  
        self.search_button.grid(row=5, column=0, padx=10, pady=5)
        self.search_button.config(bg="yellow",fg="black")
        
        #Update Contact button  
        self.update_button = tk.Button(root, text="Update Contact",font=("Comic Sans MS",15), command=self.update_contact)  
        self.update_button.grid(row=5, column=1, padx=10, pady=5)
        self.update_button.config(bg="yellow",fg="black")
        
        #Delete Contact button  
        self.delete_button = tk.Button(root, text="Delete Contact",font=("Comic Sans MS",15), command=self.delete_contact)  
        self.delete_button.grid(row=6, column=0, padx=10, pady=5)
        self.delete_button.config(bg="yellow",fg="black")
        
        #Display all contacts on startup 
        self.contact_listbox = tk.Listbox(root, width=50)
        self.contact_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        self.contact_listbox.config(bg="light yellow",fg="black")
        
#Function for add contact
    def add_contact(self):  
        name = self.name_entry.get()  
        phone = self.phone_entry.get()  
        email = self.email_entry.get()  
        address = self.address_entry.get()  

        if not name or not phone:  
            messagebox.showwarning("Warning", "Name and Phone are required.")  
            return  

        contact = Contact(name, phone, email, address)  
        self.contacts.append(contact)  

        messagebox.showinfo("Success", "Contact added successfully.")  
        self.clear_entries()
        
#Function for view contact
    def view_contacts(self):  
        self.contact_listbox.delete(0, tk.END)  
        for contact in self.contacts:  
            self.contact_listbox.insert(tk.END, f" Name:-{contact.name} , Phone:-{contact.phone} , Email:-{contact.email} , Address:-{contact.address}")

#Function for search contact
    def search_contact(self):  
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone:")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone or search_term in contact.email or search_term in contact.address]
        
        self.contact_listbox.delete(0, tk.END)  
        if found_contacts:  
            for contact in found_contacts:  
                self.contact_listbox.insert(tk.END, f"{contact.name},{contact.phone}")  
        else:  
            messagebox.showinfo("Search Result", "No contacts found.")  

#Function for update contact
    def update_contact(self):  
        selected_contact = self.contact_listbox.curselection()  
        if not selected_contact:  
            messagebox.showwarning("Warning", "Please select a contact to update.")  
            return  

        index = selected_contact[0]  
        contact = self.contacts[index]  

        new_name = self.name_entry.get() or contact.name  
        new_phone = self.phone_entry.get() or contact.phone  
        new_email = self.email_entry.get() or contact.email  
        new_address = self.address_entry.get() or contact.address  

        self.contacts[index] = Contact(new_name, new_phone, new_email, new_address)  
        messagebox.showinfo("Success", "Contact updated successfully.")  
        self.clear_entries()  
        self.view_contacts()  

#Function for delete contact
    def delete_contact(self):  
        selected_contact = self.contact_listbox.curselection()  
        if not selected_contact:  
            messagebox.showwarning("Warning", "Please select a contact to delete.")  
            return  

        index = selected_contact[0]  
        self.contacts.pop(index)  
        messagebox.showinfo("Success", "Contact deleted successfully.")  
        self.view_contacts()
        
#Remove the contact once user is ready to update
    def clear_entries(self):  
        self.name_entry.delete(0, tk.END)  
        self.phone_entry.delete(0, tk.END)  
        self.email_entry.delete(0, tk.END)  
        self.address_entry.delete(0, tk.END)  

#Run the applicition/code
if __name__ == "__main__":  
    root = tk.Tk()  
    app = ContactManager(root)  
    root.mainloop()













