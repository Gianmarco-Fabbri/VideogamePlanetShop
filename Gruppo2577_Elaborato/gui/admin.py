import tkinter as tk
from tkinter import messagebox
from db.admin_queries import *

class AdminWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pannello Amministratore")
        self.geometry("800x500")
        self.create_back_button()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        tk.Label(self, text="Pannello Amministratore", font=("Arial", 14)).pack(pady=10)
        
        self.create_user_form()

        block_user_button = tk.Button(self, text="Blocca Venditore", command=self.block_user)
        block_user_button.pack(pady=5)

        unblock_user_button = tk.Button(self, text="Sblocca Venditore", command=self.unblock_user)
        unblock_user_button.pack(pady=5)

    def on_closing(self):
        self.parent.destroy()
        self.quit()

    def create_back_button(self):
        back_button = tk.Button(self, text="←", command=self.go_back)
        back_button.place(x=10, y=10)

    def go_back(self):
        self.destroy()
        self.master.deiconify()

    def create_user_form(self):
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="Nome").grid(row=0, column=0)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Email").grid(row=1, column=0)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Nome Account").grid(row=2, column=0)
        self.nome_account_entry = tk.Entry(form_frame)
        self.nome_account_entry.grid(row=2, column=1)

        tk.Label(form_frame, text="Password").grid(row=3, column=0)
        self.password_entry = tk.Entry(form_frame, show='*')
        self.password_entry.grid(row=3, column=1)

        tk.Label(form_frame, text="Città").grid(row=4, column=0)
        self.citta_entry = tk.Entry(form_frame)
        self.citta_entry.grid(row=4, column=1)

        tk.Label(form_frame, text="CAP").grid(row=5, column=0)
        self.cap_entry = tk.Entry(form_frame)
        self.cap_entry.grid(row=5, column=1)

        tk.Label(form_frame, text="Via").grid(row=6, column=0)
        self.via_entry = tk.Entry(form_frame)
        self.via_entry.grid(row=6, column=1)

        tk.Label(form_frame, text="Numero").grid(row=7, column=0)
        self.numero_entry = tk.Entry(form_frame)
        self.numero_entry.grid(row=7, column=1)

        tk.Label(form_frame, text="Ruolo (compratore/venditore)").grid(row=8, column=0)
        self.ruolo_entry = tk.Entry(form_frame)
        self.ruolo_entry.grid(row=8, column=1)

        add_user_button = tk.Button(form_frame, text="Aggiungi Utente", command=self.add_user)
        add_user_button.grid(row=9, columnspan=2, pady=10)

    def add_user(self):
        nome = self.name_entry.get()
        email = self.email_entry.get()
        nome_account = self.nome_account_entry.get()
        password = self.password_entry.get()
        città = self.citta_entry.get()
        cap = self.cap_entry.get()
        via = self.via_entry.get()
        numero = self.numero_entry.get()
        ruolo = self.ruolo_entry.get().lower()
        
        if ruolo not in ["compratore", "venditore"]:
            messagebox.showerror("Errore", "Il ruolo deve essere 'compratore' o 'venditore'")
            return

        result = add_user(email, nome, nome_account, password, ruolo, città, cap, via, numero)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

    def block_user(self):
        email = self.email_entry.get()
        
        result = block_user(email)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

    def unblock_user(self):
        email = self.email_entry.get()
        
        result = unblock_user(email)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)