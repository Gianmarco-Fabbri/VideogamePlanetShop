import tkinter as tk
from tkinter import messagebox
from sqlalchemy.orm import sessionmaker
from db.database import setup_database
from db.models import User, Role, UserType
import hashlib

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestione Database")
        self.geometry("400x300")
        self.engine, self.Session = setup_database()
        self.session = self.Session()
        self.show_registration_panel()
    
    def show_registration_panel(self):
        self.clear_frame()

        self.label_name = tk.Label(self, text="Nome:")
        self.label_name.pack()
        self.entry_name = tk.Entry(self)
        self.entry_name.pack()
        
        self.label_email = tk.Label(self, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self)
        self.entry_email.pack()
        
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()
        
        self.label_role = tk.Label(self, text="Ruolo:")
        self.label_role.pack()
        
        self.role_var = tk.StringVar(value=Role.USER.value)
        self.radio_user = tk.Radiobutton(self, text="Utente", variable=self.role_var, value=Role.USER.value)
        self.radio_user.pack()
        self.radio_admin = tk.Radiobutton(self, text="Amministratore", variable=self.role_var, value=Role.ADMIN.value)
        self.radio_admin.pack()
        
        self.button_register = tk.Button(self, text="Registrati", command=self.register_user)
        self.button_register.pack()

        self.button_login_panel = tk.Button(self, text="Hai già un account? Accedi", command=self.show_login_panel)
        self.button_login_panel.pack()
    
    def show_login_panel(self):
        self.clear_frame()

        self.label_email = tk.Label(self, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self)
        self.entry_email.pack()
        
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()
        
        self.button_login = tk.Button(self, text="Accedi", command=self.login_user)
        self.button_login.pack()

    def show_user_type_selection(self, user):
        self.clear_frame()
        
        self.label_welcome = tk.Label(self, text=f"Benvenuto, {user.name}")
        self.label_welcome.pack()
        
        self.label_user_type = tk.Label(self, text="Scegli il tuo ruolo:")
        self.label_user_type.pack()

        self.user_type_var = tk.StringVar(value=UserType.BUYER.value)
        self.radio_buyer = tk.Radiobutton(self, text="Acquirente", variable=self.user_type_var, value=UserType.BUYER.value)
        self.radio_buyer.pack()
        self.radio_seller = tk.Radiobutton(self, text="Venditore", variable=self.user_type_var, value=UserType.SELLER.value)
        self.radio_seller.pack()

        self.button_select = tk.Button(self, text="Seleziona", command=lambda: self.set_user_type(user))
        self.button_select.pack()
    
    def set_user_type(self, user):
        user_type = self.user_type_var.get()
        user.user_type = user_type
        self.session.commit()
        messagebox.showinfo("Successo", f"Ruolo impostato su {user_type}.")
    
    def register_user(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        role = self.role_var.get()
        
        if not name or not email or not password:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori.")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        new_user = User(name=name, email=email, password=hashed_password, role=role)
        self.session.add(new_user)
        try:
            self.session.commit()
            messagebox.showinfo("Successo", "Registrazione completata con successo.")
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Errore", f"Errore durante la registrazione: {e}")
    
    def login_user(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if not email or not password:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori.")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = self.session.query(User).filter_by(email=email, password=hashed_password).first()
        
        if user:
            self.show_user_type_selection(user)
        else:
            messagebox.showerror("Errore", "Email o password non validi.")
    
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()