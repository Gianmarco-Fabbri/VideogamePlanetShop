import tkinter as tk
from tkinter import messagebox
from db.buyer_queries import *

class BuyerWindow(tk.Toplevel):
    def __init__(self, parent, email):
        super().__init__(parent)
        self.title("Pannello Acquirente")
        self.email = email
        
        tk.Label(self, text="Pannello Acquirente", font=("Arial", 14)).pack(pady=10)

        self.create_payment_method_form()
        self.create_order_form()
        self.create_subscription_form()
        self.create_review_form()
        self.create_order_history_button()
        self.create_rating_buttons()

    def create_payment_method_form(self):
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Metodo di Pagamento").grid(row=0, column=0, pady=5, padx=5)
        self.metodo_pagamento_entry = tk.Entry(form_frame)
        self.metodo_pagamento_entry.grid(row=0, column=1, pady=5, padx=5)

        payment_button = tk.Button(form_frame, text="Aggiungi Metodo di Pagamento", command=self.add_payment_method)
        payment_button.grid(row=1, columnspan=2, pady=10)

    def create_order_form(self):
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="ID Annunci (separati da virgola)").grid(row=0, column=0, pady=5, padx=5)
        self.annunci_entry = tk.Entry(form_frame)
        self.annunci_entry.grid(row=0, column=1, pady=5, padx=5)

        order_button = tk.Button(form_frame, text="Effettua Ordine", command=self.place_order)
        order_button.grid(row=1, columnspan=2, pady=10)

    def get_subscription_options(self):
        options = get_subscription_options()
        return [opt['tipoAbbonamento'] for opt in options]

    def create_subscription_form(self):
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Opzioni di Abbonamento").grid(row=0, column=0, pady=5, padx=5)
        self.abbonamento_options = tk.StringVar()
        self.abbonamento_menu = tk.OptionMenu(form_frame, self.abbonamento_options, *self.get_subscription_options())
        self.abbonamento_menu.grid(row=0, column=1, pady=5, padx=5)

        subscription_button = tk.Button(form_frame, text="Effettua Abbonamento", command=self.subscribe)
        subscription_button.grid(row=1, columnspan=2, pady=10)

    def create_review_form(self):
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Email Venditore").grid(row=0, column=0, pady=5, padx=5)
        self.email_venditore_entry = tk.Entry(form_frame)
        self.email_venditore_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Recensione").grid(row=1, column=0, pady=5, padx=5)
        self.recensione_entry = tk.Entry(form_frame)
        self.recensione_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Punteggio").grid(row=2, column=0, pady=5, padx=5)
        self.punteggio_entry = tk.Entry(form_frame)
        self.punteggio_entry.grid(row=2, column=1, pady=5, padx=5)

        review_button = tk.Button(form_frame, text="Lascia Recensione", command=self.leave_review)
        review_button.grid(row=3, columnspan=2, pady=10)

    def create_order_history_button(self):
        history_button = tk.Button(self, text="Visualizza Storico Ordini", command=self.show_order_history)
        history_button.pack(pady=10)

    def create_rating_buttons(self):
        rating_frame = tk.Frame(self)
        rating_frame.pack(pady=10)

        best_sellers_button = tk.Button(rating_frame, text="Visualizza Migliori Venditori", command=self.show_best_sellers)
        best_sellers_button.grid(row=0, columnspan=2, pady=5)

        worst_sellers_button = tk.Button(rating_frame, text="Visualizza Peggiori Venditori", command=self.show_worst_sellers)
        worst_sellers_button.grid(row=1, columnspan=2, pady=5)

    def add_payment_method(self):
        metodo_pagamento = self.metodo_pagamento_entry.get()
        
        result = add_payment_method(self.email, metodo_pagamento)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

    def place_order(self):
        annunci = self.annunci_entry.get().split(',')
        annunci = [annuncio.strip() for annuncio in annunci]
        
        result = place_order(self.email, annunci)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

    def subscribe(self):
        tipo_abbonamento = self.abbonamento_options.get()
        
        result = subscribe(self.email, tipo_abbonamento)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)

def leave_review(self):
    email_venditore = self.email_venditore_entry.get()
    recensione = self.recensione_entry.get()
    punteggio = self.punteggio_entry.get()
    
    result = leave_review(self.email, email_venditore, recensione, punteggio)
    if "Errore" in result:
        messagebox.showerror("Errore", result)
    else:
        messagebox.showinfo("Successo", result)

def show_order_history(self):
    result = get_order_history(self.email)
    if "Errore" in result:
        messagebox.showerror("Errore", result)
    else:
        self.display_order_history(result)

def show_best_sellers(self):
    result = get_best_sellers()
    if "Errore" in result:
        messagebox.showerror("Errore", result)
    else:
        self.display_sellers(result, "Migliori Venditori")

def show_worst_sellers(self):
    result = get_worst_sellers()
    if "Errore" in result:
        messagebox.showerror("Errore", result)
    else:
        self.display_sellers(result, "Peggiori Venditori")

def display_order_history(self, orders):
    window = tk.Toplevel(self)
    window.title("Storico Ordini")
    tk.Label(window, text="Storico Ordini", font=("Arial", 14)).pack(pady=10)

    for order in orders:
        text = f"ID Ordine: {order['idOrdine']}, Titolo: {order['titolo']}, Prezzo: {order['prezzo']}, Stato: {order['codStato']}"
        tk.Label(window, text=text).pack(pady=5, padx=10)

    close_button = tk.Button(window, text="Chiudi", command=window.destroy)
    close_button.pack(pady=10)

def display_sellers(self, sellers, title):
    window = tk.Toplevel(self)
    window.title(title)
    tk.Label(window, text=title, font=("Arial", 14)).pack(pady=10)

    for seller in sellers:
        text = f"Email: {seller['email']}, Media Valutazione: {seller['media_valutazione']:.2f}"
        tk.Label(window, text=text).pack(pady=5, padx=10)

    close_button = tk.Button(window, text="Chiudi", command=window.destroy)
    close_button.pack(pady=10)