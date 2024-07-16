import tkinter as tk
from tkinter import messagebox
from db.seller_queries import get_seller_products

class SellerWindow(tk.Toplevel):
    def __init__(self, parent, seller_email):
        super().__init__(parent)
        self.title("Pannello Venditore")
        self.seller_email = seller_email
        
        tk.Label(self, text="Pannello Venditore", font=("Arial", 14)).pack(pady=10)
        
        query_button = tk.Button(self, text="Visualizza Prodotti", command=self.run_query)
        query_button.pack(pady=5)

    def run_query(self):
        result = get_seller_products(self.seller_email)
        if isinstance(result, str) and "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            self.show_results(result)

    def show_results(self, results):
        result_window = tk.Toplevel(self)
        result_window.title("Prodotti del Venditore")

        for i, row in enumerate(results):
            tk.Label(result_window, text=str(row)).pack()