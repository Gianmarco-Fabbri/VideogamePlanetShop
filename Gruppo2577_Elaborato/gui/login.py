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
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        #per premere invio e fare login
        self.bind('<Return>', self.login_key_return)

        frame = tk.Frame(self)
        frame.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        tk.Label(frame, text="Email").grid(row=0, column=0, pady=5, padx=5)
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(frame, text="Password").grid(row=1, column=0, pady=5, padx=5)
        self.password_entry = tk.Entry(frame, show='*')
        self.password_entry.grid(row=1, column=1, pady=5, padx=5)

        login_button = tk.Button(frame, text="Login", command=self.login)
        login_button.grid(row=2, columnspan=2, pady=10)
        
    def login_key_return(self, event):
        self.login()
    
    def on_closing(self):
        self.destroy()

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