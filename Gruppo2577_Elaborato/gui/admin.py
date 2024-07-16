import tkinter as tk
from tkinter import messagebox
from db.admin_queries import execute_admin_query, get_all_products

class AdminWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pannello Amministratore")
        
        tk.Label(self, text="Pannello Amministratore", font=("Arial", 14)).pack(pady=10)
        
        query1_button = tk.Button(self, text="Esegui Query 1", command=lambda: self.run_query("SELECT * FROM tabella1"))
        query1_button.pack(pady=5)
        
        query2_button = tk.Button(self, text="Esegui Query 2", command=lambda: self.run_query("UPDATE tabella2 SET campo='valore' WHERE condizione"))
        query2_button.pack(pady=5)
        
        query3_button = tk.Button(self, text="Esegui Query 3", command=lambda: self.run_query("DELETE FROM tabella3 WHERE condizione"))
        query3_button.pack(pady=5)
        
        query4_button = tk.Button(self, text='Visualizza prodotti neri', command=self.run_get_all_products)
        query4_button.pack(pady=5)

    def run_query(self, query):
        result = execute_admin_query(query)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

    def run_get_all_products(self):
        result = get_all_products()
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)