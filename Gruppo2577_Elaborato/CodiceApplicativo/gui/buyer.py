import tkinter as tk
from tkinter import messagebox, ttk
from db.buyer_queries import *
import matplotlib.pyplot as plt

class BuyerWindow(tk.Toplevel):
    def __init__(self, parent, email):
        super().__init__(parent)
        self.title("Pannello Acquirente")
        self.email = email
        self.parent = parent
        self.geometry("900x600")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.create_back_button()
         
        tk.Label(self, text="Pannello Acquirente", font=("Arial", 14)).pack(pady=10)

        self.carrello = []  # Lista per tenere traccia degli annunci nel carrello

        # Dividi la GUI in due colonne
        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Aggiungi gli oggetti nella parte sinistra
        self.create_payment_method_form()
        self.create_order_form()
        self.create_subscription_form()
        self.create_review_form()

        # Aggiungi gli oggetti nella parte destra
        self.create_order_history_button()
        self.create_cart_section()
        self.create_order_button()
        self.create_track_form()
        self.create_seller_button(self.right_frame)
        

    def on_closing(self):
        self.parent.destroy()
        self.quit()

    def create_back_button(self):
        back_button = tk.Button(self, text="←", command=self.go_back)
        back_button.place(x=10, y=10)

    def go_back(self):
        self.destroy()
        self.master.deiconify()

    def create_track_form(self):
        form_frame = tk.Frame(self.right_frame)
        form_frame.pack(pady=10)

        track_button = tk.Button(form_frame, text="Visualizza tracciamenti", command=self.open_track_window)
        track_button.grid(row=2, columnspan=2, pady=10)

    def open_track_window(self):
        self.track_window = tk.Toplevel(self)
        self.track_window.title("Tracciamenti")
        self.track_window.geometry("500x300")

        result = tracking(self.email)

        if isinstance(result, str):  # Se il risultato è una stringa, è un messaggio di errore
            tk.Label(self.track_window, text=result).pack(pady=5, padx=10)
        else:
            for track in result:
                text = f"L'annuncio {track['id_annuncio']} dell'ordine {track['idOrdine']} si trova nel magazzino: {track['nome_magazzino']}. \nStato: {track['stato']}"
                tk.Label(self.track_window, text=text).pack(pady=5, padx=10)

        close_button = tk.Button(self.track_window, text="Chiudi", command=self.track_window.destroy)
        close_button.pack(pady=10)
        

    def create_payment_method_form(self):
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        payment_button = tk.Button(form_frame, text="Aggiungi Metodo di Pagamento", command=self.open_payment_method_window)
        payment_button.pack(pady=10)

    def open_payment_method_window(self):
        self.payment_window = tk.Toplevel(self)
        self.payment_window.title("Aggiungi Metodo di Pagamento")
        self.payment_window.geometry("450x350")

        tk.Label(self.payment_window, text="Tipologia Carta (Debito / Credito)").pack(pady=5)
        self.tipologia_entry = tk.Entry(self.payment_window)
        self.tipologia_entry.pack(pady=5)

        tk.Label(self.payment_window, text="Circuito Pagamento").pack(pady=5)
        self.circuito_entry = tk.Entry(self.payment_window)
        self.circuito_entry.pack(pady=5)

        tk.Label(self.payment_window, text="Codice Carta").pack(pady=5)
        self.codice_entry = tk.Entry(self.payment_window)
        self.codice_entry.pack(pady=5)

        tk.Label(self.payment_window, text="Scadenza (YYYY-MM-DD)").pack(pady=5)
        self.scadenza_entry = tk.Entry(self.payment_window)
        self.scadenza_entry.pack(pady=5)

        add_button = tk.Button(self.payment_window, text="Aggiungi", command=self.add_payment_method)
        add_button.pack(pady=20)

    def create_order_form(self):
        form_frame = tk.Frame(self.left_frame)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Annunci Disponibili").grid(row=0, column=0, pady=5, padx=5)
        self.annunci_combobox = ttk.Combobox(form_frame, state="readonly")
        self.annunci_combobox.grid(row=0, column=1, pady=5, padx=5)
        self.load_annunci()

        add_to_cart_button = tk.Button(form_frame, text="Aggiungi al Carrello", command=self.add_to_cart)
        add_to_cart_button.grid(row=1, columnspan=2, pady=10)

    def create_cart_section(self):
        cart_frame = tk.LabelFrame(self.right_frame, text="Carrello")
        cart_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)

        self.cart_listbox = tk.Listbox(cart_frame)
        self.cart_listbox.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)

    def create_order_button(self):
        order_button = tk.Button(self.right_frame, text="Effettua ordine", command=self.place_order)
        order_button.pack(pady=10)

    def get_subscription_options(self):
        options = get_subscription_options()
        return [opt for opt in options]

    def create_subscription_form(self):
        form_frame = tk.Frame(self.left_frame)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Opzioni di Abbonamento").grid(row=0, column=0, pady=5, padx=5)
        self.abbonamento_options = tk.StringVar()
        self.abbonamento_menu = tk.OptionMenu(form_frame, self.abbonamento_options, *self.get_subscription_options())
        self.abbonamento_menu.grid(row=0, column=1, pady=5, padx=5)

        subscription_button = tk.Button(form_frame, text="Compra Abbonamento", command=self.subscribe)
        subscription_button.grid(row=1, columnspan=2, pady=10)

    def create_review_form(self):
        form_frame = tk.Frame(self.left_frame)
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
        history_button = tk.Button(self.right_frame, text="Visualizza Storico Ordini", command=self.show_order_history)
        history_button.pack(pady=10)

    def create_rating_buttons(self):
        rating_frame = tk.Frame(self.right_frame)
        rating_frame.pack(pady=10)

        best_sellers_button = tk.Button(rating_frame, text="Visualizza Migliori Venditori", command=self.show_best_sellers)
        best_sellers_button.grid(row=0, columnspan=2, pady=5)

        worst_sellers_button = tk.Button(rating_frame, text="Visualizza Peggiori Venditori", command=self.show_worst_sellers)
        worst_sellers_button.grid(row=1, columnspan=2, pady=5)

    def add_payment_method(self):
        tipologia = self.tipologia_entry.get()
        circuito = self.circuito_entry.get()
        codice = self.codice_entry.get()
        scadenza = self.scadenza_entry.get()
        
        result = add_payment_method(self.email, tipologia, circuito, codice, scadenza)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)
            self.payment_window.destroy()

    def place_order(self):
        if not self.carrello:
            messagebox.showerror("Errore", "Il carrello è vuoto")
            return

        id_annunci = [item for item in self.carrello]
        result = place_order(self.email, id_annunci)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)
            self.carrello = []
            self.update_cart_listbox()
            self.load_annunci()

    def add_to_cart(self):
        selected_annuncio = self.annunci_combobox.get()
        id_annuncio = self.annunci_dict.get(selected_annuncio)

        if not id_annuncio or id_annuncio in self.carrello:
            messagebox.showerror("Errore", "Seleziona un annuncio valido")
            return

        self.carrello.append(id_annuncio)
        self.update_cart_listbox()
        self.load_annunci()

    def show_cart(self):
        cart_window = tk.Toplevel(self)
        cart_window.title("Carrello Corrente")

        tk.Label(cart_window, text="Carrello Corrente", font=("Arial", 14)).pack(pady=10)

        cart_listbox = tk.Listbox(cart_window)
        cart_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for item in self.carrello:
            cart_listbox.insert(tk.END, f"ID Annuncio: {item}")

        close_button = tk.Button(cart_window, text="Chiudi", command=cart_window.destroy)
        close_button.pack(pady=10)

    def update_cart_listbox(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.carrello:
            self.cart_listbox.insert(tk.END, f"ID Annuncio: {item}")

    def subscribe(self):
        tipo_abbonamento = self.abbonamento_options.get()
        
        result = subscribe(self.email, tipo_abbonamento)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            messagebox.showinfo("Successo", result)
            self.show_subscription_history()

    def show_subscription_history(self):
        result = get_subscription_history(self.email)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            self.display_subscription_history(result)

    def display_subscription_history(self, history):
        window = tk.Toplevel(self)
        window.title("Storico Abbonamenti")
        tk.Label(window, text="Storico Abbonamenti", font=("Arial", 14)).pack(pady=10)

        for record in history:
            text = f"Tipo: {record['tipoAbbonamento']}, Inizio: {record['data_inizio']}, Fine: {record['data_fine']}"
            tk.Label(window, text=text).pack(pady=5, padx=10)

        close_button = tk.Button(window, text="Chiudi", command=window.destroy)
        close_button.pack(pady=10)

    def leave_review(self):
        email_venditore = self.email_venditore_entry.get()
        recensione = self.recensione_entry.get()
        punteggio = self.punteggio_entry.get()
        
        result = leave_review(self.email, email_venditore, recensione, punteggio)
        if "Errore" in result:
            messagebox.showerror("Errore",result)
        else:
            messagebox.showinfo("Successo", result)

    def show_order_history(self):
        result = get_order_history(self.email)
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            self.display_order_history(result)

    def show_valutazioni_medie_venditori(self):
        result = get_valutazioni_medie_venditori()
        if "Errore" in result:
            messagebox.showerror("Errore", result)
        else:
            venditori = [row['email_venditore'] for row in result]
            valutazioni = [row['valutazione_media'] for row in result]

            plt.figure(figsize=(10, 6))
            plt.bar(venditori, valutazioni, color='green')
            plt.xlabel('Venditore')
            plt.ylabel('Valutazione Media')
            plt.title('Valutazioni Medie dei Venditori')
            plt.xticks(rotation=45, ha='right')
            plt.show()

    def create_seller_button(self, parent):
        stats_frame = tk.Frame(parent)
        stats_frame.pack(pady=10)

        valutazioni_venditori_button = tk.Button(stats_frame, text="Valutazioni Venditori", command=self.show_valutazioni_medie_venditori)
        valutazioni_venditori_button.pack(side=tk.LEFT, padx=5, pady=5)

    def display_order_history(self, orders):
        window = tk.Toplevel(self)
        window.geometry("300x200")
        tk.Label(window, text="Storico Ordini", font=("Arial", 14)).pack(pady=10)

        for order in orders:
            text = f"ID Ordine: {order['idOrdine']}, Stato: {order['codStato']}"
            tk.Label(window, text=text).pack(pady=5, padx=10)

        close_button = tk.Button(window, text="Chiudi", command=window.destroy)
        close_button.pack(pady=10)

    def load_annunci(self):
        annunci = get_buyable_announcment()
        self.annunci_combobox['values'] = [f"{annuncio['titolo']} - {annuncio['email']} - {annuncio['descrizione']}" for annuncio in annunci]
        self.annunci_dict = {f"{annuncio['titolo']} - {annuncio['email']} - {annuncio['descrizione']}": annuncio['id'] for annuncio in annunci}
        if annunci:
            self.annunci_combobox.current(0)