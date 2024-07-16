import tkinter as tk
from tkinter import messagebox
from gui.admin import AdminWindow
from gui.seller import SellerWindow
from gui.buyer import BuyerWindow
from db.user_queries import get_user_type

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500") 
        self.title("Login")

        tk.Label(self, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack(pady=10)
        

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        user_type = get_user_type(email, password)

        if user_type == "admin":
            self.open_admin_window(email)
        elif user_type == "seller":
            self.open_seller_window(email)
        elif user_type == "buyer":
            self.open_buyer_window(email)
        else:
            messagebox.showerror("Errore", "Credenziali non valide o utente non trovato")

    def open_admin_window(self, email):
        self.withdraw()
        admin_window = AdminWindow(self)
        admin_window.mainloop()

    def open_seller_window(self, email):
        self.withdraw()
        seller_window = SellerWindow(self, email)
        seller_window.mainloop()

    def open_buyer_window(self, email):
        self.withdraw()
        buyer_window = BuyerWindow(self, email)
        buyer_window.mainloop()