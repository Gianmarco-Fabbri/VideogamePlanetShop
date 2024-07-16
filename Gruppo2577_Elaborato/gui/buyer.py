import tkinter as tk
from tkinter import messagebox
from db.buyer_queries import get_buyer_purchases

class BuyerWindow(tk.Toplevel):
    def __init__(self, parent, buyer_email):
        super().__init__(parent)
        self.title("Pannello Acquirente")
        self.buyer_email = buyer_email
        
        tk.Label(self, text="Pannello Acquirente", font=("Arial", 14)).pack(pady=10)
        
        query_button = tk.Button(self, text="Visualizza Acquisti", command=self.run_query)
        query_button.pack(pady=5)

    def run_query(self):
        result = get_buyer_purchases(self.buyer_email)
        if isinstance(result, str) and "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            self.show_results(result)

    def show_results(self, results):
        result_window = tk.Toplevel(self)
        result_window.title("Acquisti dell'Acquirente")

        for i, row in enumerate(results):
            tk.Label(result_window, text=str(row)).pack()