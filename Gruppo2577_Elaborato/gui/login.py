import tkinter as tk
from tkinter import messagebox
from gui.admin import AdminWindow
from gui.user import UserWindow
from db.connection import create_connection

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")

        tk.Label(self, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        tk.Label(self, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack(pady=10)

    def login(self):
        user = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        connection = create_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM users WHERE username='{user}' AND password='{password}' AND email='{email}'")
            record = cursor.fetchone()
            if record:
                if user == 'admin':
                    self.open_admin_window()
                else:
                    self.open_user_window()
            else:
                messagebox.showerror("Errore", "Credenziali non valide")
            cursor.close()
            connection.close()
        else:
            messagebox.showerror("Errore", "Connessione al database fallita")

    def open_admin_window(self):
        self.withdraw()
        admin_window = AdminWindow(self)
        admin_window.mainloop()

    def open_user_window(self):
        self.withdraw()
        user_window = UserWindow(self)
        user_window.mainloop()