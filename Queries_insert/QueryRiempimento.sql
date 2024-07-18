-- Popolamento della tabella ABBONAMENTO
INSERT INTO ABBONAMENTO (tipoAbbonamento, durata, prezzo) VALUES
('Mensile', 30, 9.99),
('Trimestrale', 90, 27.99),
('Semestrale', 365, 54.99),
('Annuale', 365, 99.99);

-- Popolamento della tabella CASA_PRODUTTRICE
INSERT INTO CASA_PRODUTTRICE (idCasaProduttrice) VALUES
('Sony'),
('Microsoft'),
('Nintendo');

-- Popolamento della tabella GENERAZIONE
INSERT INTO GENERAZIONE (idCasaProduttrice, numeroGenerazione) VALUES
('Sony', 5),
('Microsoft', 4),
('Nintendo', 8);

-- Popolamento della tabella INDIRIZZO
INSERT INTO INDIRIZZO (città, cap, via, numero) VALUES
('Roma', 00100, 'Via Roma', 1),
('Milano', 20121, 'Via Milano', 2),
('Napoli', 80100, 'Via Napoli', 3),
('Bologna', 40126, 'Via Rizzoli', 1),
('Torino', 10121, 'Via Torino', 4);

-- Popolamento della tabella UTENTE
INSERT INTO UTENTE (nome, email, nome_account, password, ACQUIRENTE, ADMIN, VENDITORE, città, cap, via, numero) VALUES
("GimboStar", "gianmarcof@unibo.it", "Gimbo", "gian03", NULL, "gianmarcof@unibo.it", NULL, "Bologna", 40126, "Via Rizzoli", 1), 
("FiloFraf", "filippof@unibo.it", "Filo", "filipp03", NULL, "filippof@unibo.it", NULL, "Milano", 20121, "Via Milano", 2), 
('Mario Rossi', 'mario.rossi@example.com', 'mrossi', 'mrossi1', NULL, NULL, 'mario.rossi@example.com', 'Roma', 00100, 'Via Roma', 1),
('Luigi Verdi', 'luigi.verdi@example.com', 'lverdi', 'password2', NULL, NULL, 'luigi.verdi@example.com', 'Milano', 20121, 'Via Milano', 2),
('Anna Bianchi', 'anna.bianchi@example.com', 'abianchi', 'password3', 'anna.bianchi@example.com', NULL, NULL, 'Napoli', 80100, 'Via Napoli', 3),
('a', 'a', 'b', 'b', NULL, NULL, 'a', "Bologna", 40126, "Via Rizzoli", 1),
('Marco Neri', 'marco.neri@example.com', 'mneri', 'password4', 'marco.neri@example.com', NULL, NULL, 'Torino', 10121, 'Via Torino', 4);


-- Popolamento della tabella ACQUIRENTE
INSERT INTO ACQUIRENTE (isAbbonato, email, puntiSconto) VALUES
(true, 'anna.bianchi@example.com', 30),
(false, 'marco.neri@example.com', 40);

-- Popolamento della tabella ADMIN
INSERT into ADMIN values
("gianmarcof@unibo.it"),
("filippof@unibo.it");

-- Popolamento della tabella VENDITORE
INSERT INTO VENDITORE (email, isBloccato, isNegozio) VALUES
('mario.rossi@example.com', false, true),
('a', false, false),
('luigi.verdi@example.com', false, false);

-- Popolamento della tabella METODO_PAGAMENTO
INSERT INTO METODO_PAGAMENTO (tipologiaCarta, circuitoPagamento, codCarta, scadenza, email) VALUES
('Credito', 'Visa', 1234567890123456, '2024-12-31', 'mario.rossi@example.com'),
('Debito', 'MasterCard', 9876543210987654, '2023-06-30', 'luigi.verdi@example.com');

-- Popolamento della tabella PRODOTTO
INSERT INTO PRODOTTO (descrizione, codice, CONSOLE, ACCESSORIO, GIOCO, idCasaProduttrice, numeroGenerazione) VALUES
('PlayStation 5', 1001, 1, NULL, NULL, 'Sony', 5),
('Xbox Series X', 1002, 1, NULL, NULL, 'Microsoft', 4),
('Nintendo Switch', 1003, 1, NULL, NULL, 'Nintendo', 8),
('Controller PS5', 2001, NULL, 1, NULL, 'Sony', 5),
('Halo Infinite', 3001, NULL, NULL, 1, 'Microsoft', 4);

-- Popolamento della tabella ANNUNCIO
INSERT INTO ANNUNCIO (punti_prodotto, id_annuncio, titolo, prezzo, descrizione, email) VALUES
(100, 1, 'Vendo PS5', 499, 'PlayStation 5 nuova', 'marco.neri@example.com'),
(150, 2, 'Vendo Xbox Series X', 499, 'Xbox Series X usata', 'marco.neri@example.com'),
(200, 3, 'Vendo Nintendo Switch', 299, 'Nintendo Switch in ottime condizioni', 'luigi.verdi@example.com');

-- Popolamento della tabella RECENSIONE
INSERT INTO RECENSIONE (email_acquirente, email_venditore, descrizione, valutazione) VALUES
('mario.rossi@example.com', 'marco.neri@example.com', 'Ottimo venditore', 5),
('luigi.verdi@example.com', 'marco.neri@example.com', 'Venditore affidabile', 4),
('anna.bianchi@example.com', 'luigi.verdi@example.com', 'Non molto soddisfatta', 2),
('marco.neri@example.com', 'luigi.verdi@example.com', 'Prodotto come descritto', 3);

-- Popolamento della tabella ORDINE
INSERT INTO ORDINE (idOrdine, email, codStato) VALUES
(1, 'mario.rossi@example.com', 'A'),
(2, 'luigi.verdi@example.com', 'B'),
(3, 'anna.bianchi@example.com', 'C');

-- Popolamento della tabella DETTAGLIO_ORDINE
INSERT INTO DETTAGLIO_ORDINE (id_annuncio, Inc_id_annuncio, idOrdine) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3);

-- Popolamento della tabella STATO_ORDINE
INSERT INTO STATO_ORDINE (codStato, descrizione) VALUES
('A', 'In lavorazione'),
('B', 'Spedito'),
('C', 'Consegnato');

-- Popolamento della tabella SCONTO
INSERT INTO SCONTO (percentuale, id_annuncio) VALUES
(10, 1),
(20, 2);

-- Popolamento della tabella DETTAGLIO
INSERT INTO DETTAGLIO (isUsato, condizioni, id_annuncio, codice, numeroSerie) VALUES
(false, 'Nuovo', 1, 1001, 1),
(true, 'Buone', 2, 1002, 2),
(false, 'Ottime', 3, 1003, 3);

-- Popolamento della tabella SPECIFICHE_PRODOTTO
INSERT INTO SPECIFICHE_PRODOTTO (codice, descrizione, numeroSerie, colore) VALUES
(1001, 'PlayStation 5', 1, 'Bianco'),
(1002, 'Xbox Series X', 2, 'Nero'),
(1003, 'Nintendo Switch', 3, 'Rosso-Blu');