import tkinter as tk
import db.seller_queries as dbsq
from tkinter import messagebox
from db.seller_queries import my_annunci, create_annuncio, delete_annuncio, apply_discount, product_best_seller

class SellerWindow(tk.Toplevel):
    def __init__(self, parent, email):
        super().__init__(parent)
        self.title("Pannello Venditore")
        self.email = email
        
        tk.Label(self, text="Pannello Venditore", font=("Arial", 14)).pack(pady=10)

        self.create_announcement_form()
        self.create_buttons()

    def create_announcement_form(self):
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Titolo").grid(row=0, column=0, pady=5, padx=5)
        self.titolo_entry = tk.Entry(form_frame)
        self.titolo_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Descrizione").grid(row=1, column=0, pady=5, padx=5)
        self.descrizione_entry = tk.Entry(form_frame)
        self.descrizione_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Prezzo").grid(row=2, column=0, pady=5, padx=5)
        self.data_entry = tk.Entry(form_frame)
        self.data_entry.grid(row=2, column=1, pady=5, padx=5)

        create_button = tk.Button(form_frame, text="Crea Annuncio", command=self.create_announcement)
        create_button.grid(row=4, columnspan=2, pady=10)

    def create_buttons(self):
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Label(button_frame, text="ID Annuncio").grid(row=0, column=0, pady=5, padx=5)
        self.id_annuncio_entry = tk.Entry(button_frame)
        self.id_annuncio_entry.grid(row=0, column=1, pady=5, padx=5)

        delete_button = tk.Button(button_frame, text="Elimina Annuncio", command=self.delete_announcement)
        delete_button.grid(row=1, columnspan=2, pady=5)

        tk.Label(button_frame, text="Sconto").grid(row=2, column=0, pady=5, padx=5)
        self.sconto_entry = tk.Entry(button_frame)
        self.sconto_entry.grid(row=2, column=1, pady=5, padx=5)

        discount_button = tk.Button(button_frame, text="Applica Sconto", command=self.discount_announcement)
        discount_button.grid(row=3, columnspan=2, pady=5)

        my_annunci_button = tk.Button(button_frame, text="Visualizza i miei annunci", command=self.show_my_annunci)
        my_annunci_button.grid(row=4, columnspan=2, pady=5)

        best_selling_button = tk.Button(button_frame, text="Visualizza Prodotto Più Venduto", command=self.show_best_selling_product)
        best_selling_button.grid(row=4, columnspan=2, pady=5)

    def create_announcement(self):
        titolo = self.titolo_entry.get()
        descrizione = self.descrizione_entry.get()
        prezzo = self.punti_entry.get()
        
        result = create_annuncio(self.email, titolo, descrizione, prezzo)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

    def delete_announcement(self):
        id_annuncio = self.id_annuncio_entry.get()
        
        result = delete_annuncio(self.email, id_annuncio)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

    def discount_announcement(self):
        id_annuncio = self.id_annuncio_entry.get()
        sconto = self.sconto_entry.get()
        
        result = apply_discount(self.email, id_annuncio, sconto)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

    def show_my_annunci(self):
        result = my_annunci(self.email)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Prodotto Più Venduto", result)

    def show_best_selling_product(self):
        result = product_best_seller()
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Prodotto Più Venduto", result)