import tkinter as tk
from tkinter import messagebox
from db.queries import execute_query

class UserWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pannello Utente")
        
        tk.Label(self, text="Pannello Utente", font=("Arial", 14)).pack(pady=10)
        
        query1_button = tk.Button(self, text="Esegui Query 1", command=lambda: self.run_query("SELECT * FROM tabella1"))
        query1_button.pack(pady=5)
        
        query2_button = tk.Button(self, text="Esegui Query 2", command=lambda: self.run_query("INSERT INTO tabella4 (campo1, campo2) VALUES ('valore1', 'valore2')"))
        query2_button.pack(pady=5)

    def run_query(self, query):
        result = execute_query(query)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)