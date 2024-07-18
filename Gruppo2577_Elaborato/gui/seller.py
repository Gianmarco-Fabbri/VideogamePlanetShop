import tkinter as tk
from tkinter import messagebox
from db.seller_queries import *

class SellerWindow(tk.Toplevel):
    def __init__(self, parent, email):
        super().__init__(parent)
        self.title("Pannello Venditore")
        self.email = email
        
        self.create_layout()

    def create_layout(self):
        left_frame = tk.Frame(self)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        right_frame = tk.Frame(self)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_annuncio_form(left_frame)
        self.create_delete_annuncio_form(left_frame)
        self.create_discount_form(left_frame)
        self.create_add_specifica_form(right_frame)
        self.create_my_annunci_button(right_frame)

    def create_annuncio_form(self, parent):
        form_frame = tk.LabelFrame(parent, text="Crea Annuncio")
        form_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        tk.Label(form_frame, text="Titolo").grid(row=0, column=0, pady=5, padx=5)
        self.titolo_entry = tk.Entry(form_frame)
        self.titolo_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Descrizione").grid(row=1, column=0, pady=5, padx=5)
        self.descrizione_entry = tk.Entry(form_frame)
        self.descrizione_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Prezzo").grid(row=2, column=0, pady=5, padx=5)
        self.prezzo_entry = tk.Entry(form_frame)
        self.prezzo_entry.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Codice").grid(row=3, column=0, pady=5, padx=5)
        self.codice_entry = tk.Entry(form_frame)
        self.codice_entry.grid(row=3, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Numero di Serie").grid(row=4, column=0, pady=5, padx=5)
        self.numero_serie_entry = tk.Entry(form_frame)
        self.numero_serie_entry.grid(row=4, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Descrizione Prodotto").grid(row=5, column=0, pady=5, padx=5)
        self.desc_prodotto_entry = tk.Entry(form_frame)
        self.desc_prodotto_entry.grid(row=5, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Colore").grid(row=6, column=0, pady=5, padx=5)
        self.colore_entry = tk.Entry(form_frame)
        self.colore_entry.grid(row=6, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Usato (0 o 1)").grid(row=7, column=0, pady=5, padx=5)
        self.is_usato_entry = tk.Entry(form_frame)
        self.is_usato_entry.grid(row=7, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Condizioni").grid(row=8, column=0, pady=5, padx=5)
        self.condizioni_entry = tk.Entry(form_frame)
        self.condizioni_entry.grid(row=8, column=1, pady=5, padx=5)

        create_button = tk.Button(form_frame, text="Crea Annuncio", command=self.create_annuncio)
        create_button.grid(row=9, columnspan=2, pady=10)

    def create_annuncio(self):
        titolo = self.titolo_entry.get()
        descrizione = self.descrizione_entry.get()
        prezzo = self.prezzo_entry.get()
        codice = self.codice_entry.get()
        numero_serie = self.numero_serie_entry.get()
        desc_prodotto = self.desc_prodotto_entry.get()
        colore = self.colore_entry.get()
        is_usato = self.is_usato_entry.get()
        condizioni = self.condizioni_entry.get()
        
        result = create_annuncio(self.email, titolo, descrizione, prezzo, codice, numero_serie, desc_prodotto, colore, is_usato, condizioni)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", "Annuncio creato con successo")

    def create_delete_annuncio_form(self, parent):
        form_frame = tk.LabelFrame(parent, text="Elimina Annuncio")
        form_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        tk.Label(form_frame, text="ID Annuncio").grid(row=0, column=0, pady=5, padx=5)
        self.id_annuncio_entry = tk.Entry(form_frame)
        self.id_annuncio_entry.grid(row=0, column=1, pady=5, padx=5)

        delete_button = tk.Button(form_frame, text="Elimina Annuncio", command=self.delete_annuncio)
        delete_button.grid(row=1, columnspan=2, pady=10)

    def delete_annuncio(self):
        id_annuncio = self.id_annuncio_entry.get()
        
        result = delete_annuncio(self.email, id_annuncio)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", "Annuncio eliminato con successo")

    def create_discount_form(self, parent):
        form_frame = tk.LabelFrame(parent, text="Applica Sconto")
        form_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        tk.Label(form_frame, text="ID Annuncio").grid(row=0, column=0, pady=5, padx=5)
        self.id_annuncio_sconto_entry = tk.Entry(form_frame)
        self.id_annuncio_sconto_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Sconto (%)").grid(row=1, column=0, pady=5, padx=5)
        self.sconto_entry = tk.Entry(form_frame)
        self.sconto_entry.grid(row=1, column=1, pady=5, padx=5)

        discount_button = tk.Button(form_frame, text="Applica Sconto", command=self.apply_discount)
        discount_button.grid(row=2, columnspan=2, pady=10)

    def apply_discount(self):
        id_annuncio = self.id_annuncio_sconto_entry.get()
        sconto = self.sconto_entry.get()
        
        result = apply_discount(self.email, id_annuncio, sconto)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", "Sconto applicato con successo")

    def create_add_specifica_form(self, parent):
        form_frame = tk.LabelFrame(parent, text="Aggiungi Specifica Prodotto")
        form_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        tk.Label(form_frame, text="ID Annuncio").grid(row=0, column=0, pady=5, padx=5)
        self.id_annuncio_specifica_entry = tk.Entry(form_frame)
        self.id_annuncio_specifica_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Codice").grid(row=1, column=0, pady=5, padx=5)
        self.codice_specifica_entry = tk.Entry(form_frame)
        self.codice_specifica_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Numero di Serie").grid(row=2, column=0, pady=5, padx=5)
        self.numero_serie_specifica_entry = tk.Entry(form_frame)
        self.numero_serie_specifica_entry.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Descrizione Prodotto").grid(row=3, column=0, pady=5, padx=5)
        self.desc_prodotto_specifica_entry = tk.Entry(form_frame)
        self.desc_prodotto_specifica_entry.grid(row=3, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Colore").grid(row=4, column=0, pady=5, padx=5)
        self.colore_specifica_entry = tk.Entry(form_frame)
        self.colore_specifica_entry.grid(row=4, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Usato (0 o 1)").grid(row=5, column=0, pady=5, padx=5)
        self.is_usato_specifica_entry = tk.Entry(form_frame)
        self.is_usato_specifica_entry.grid(row=5, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Condizioni").grid(row=6, column=0, pady=5, padx=5)
        self.condizioni_specifica_entry = tk.Entry(form_frame)
        self.condizioni_specifica_entry.grid(row=6, column=1, pady=5, padx=5)

        add_specifica_button = tk.Button(form_frame, text="Aggiungi Specifica", command=self.add_specifica)
        add_specifica_button.grid(row=7, columnspan=2, pady=10)

    def add_specifica(self):
        id_annuncio = self.id_annuncio_specifica_entry.get()
        codice = self.codice_specifica_entry.get()
        numero_serie = self.numero_serie_specifica_entry.get()
        descrizione_prodotto = self.desc_prodotto_specifica_entry.get()
        colore = self.colore_specifica_entry.get()
        is_usato = self.is_usato_specifica_entry.get()
        condizioni = self.condizioni_specifica_entry.get()
        
        result = modify_annuncio(id_annuncio, self.email, codice, numero_serie, descrizione_prodotto, colore, is_usato, condizioni)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", "Specifica aggiunta con successo")

    def create_my_annunci_button(self, parent):
        my_annunci_button = tk.Button(parent, text="Visualizza i miei Annunci", command=self.show_my_annunci)
        my_annunci_button.pack(pady=10)

    def show_my_annunci(self):
        result = my_annunci(self.email)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            self.display_my_annunci(result)

    def display_my_annunci(self, annunci):
        window = tk.Toplevel(self)
        window.title("I miei Annunci")
        window.geometry("500x400")  # Dimensione maggiore

        container = tk.Frame(window)
        container.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        tk.Label(scrollable_frame, text="I miei Annunci", font=("Arial", 14)).pack(pady=10)

        for annuncio in annunci:
            text = f"ID: {annuncio['id_annuncio']}, Titolo: {annuncio['titolo']}, Prezzo: {annuncio['prezzo']}, Descrizione: {annuncio['descrizione']}"
            tk.Label(scrollable_frame, text=text).pack(pady=5, padx=10)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        close_button = tk.Button(window, text="Chiudi", command=window.destroy)
        close_button.pack(pady=10)