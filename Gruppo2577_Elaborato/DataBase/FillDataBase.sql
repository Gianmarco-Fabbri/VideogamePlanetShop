-- Popolamento della tabella ABBONAMENTO
INSERT INTO ABBONAMENTO (tipoAbbonamento, durata, prezzo) VALUES
('Mensile', 30, 9.99),
('Trimestrale', 90, 27.99),
('Semestrale', 180, 54.99),
('Annuale', 365, 99.99);

-- Popolamento della tabella CASA_PRODUTTRICE
INSERT INTO CASA_PRODUTTRICE (idCasaProduttrice) VALUES
('Sony'),
('Microsoft'),
('Nintendo'),
('Sega'),
('Atari'),
('Capcom'),
('Ubisoft'),
('Electronic Arts');

-- Popolamento della tabella GENERAZIONE
INSERT INTO GENERAZIONE (idCasaProduttrice, numeroGenerazione) VALUES
('Sony', 5),
('Microsoft', 4),
('Nintendo', 8),
('Sega', 3),
('Atari', 1),
('Capcom', 2),
('Ubisoft', 1),
('Electronic Arts', 1),
('Sony', 4),
('Microsoft', 3),
('Nintendo', 7),
('Sega', 2),
('Atari', 2);

-- Popolamento della tabella INDIRIZZO
INSERT INTO INDIRIZZO (città, cap, via, numero) VALUES
('Roma', 00100, 'Via Roma', 1),
('Milano', 20121, 'Via Milano', 2),
('Napoli', 80100, 'Via Napoli', 3),
('Bologna', 40126, 'Via Rizzoli', 1),
('Torino', 10121, 'Via Torino', 4),
('Firenze', 50123, 'Via Firenze', 5),
('Genova', 16121, 'Via Genova', 6),
('Venezia', 30121, 'Via Venezia', 7);

-- Popolamento della tabella UTENTE
INSERT INTO UTENTE (nome, email, nome_account, password, ACQUIRENTE, ADMIN, VENDITORE, città, cap, via, numero) VALUES
("GimboStar", "gianmarcof@unibo.it", "Gimbo", "gian03", NULL, "gianmarcof@unibo.it", NULL, "Bologna", 40126, "Via Rizzoli", 1), 
("FiloFraf", "filippof@unibo.it", "Filo", "filipp03", NULL, "filippof@unibo.it", NULL, "Milano", 20121, "Via Milano", 2), 
('Mario Rossi', 'mario.rossi@example.com', 'mrossi', 'mrossi1', NULL, NULL, 'mario.rossi@example.com', 'Roma', 00100, 'Via Roma', 1),
('Luigi Verdi', 'luigi.verdi@example.com', 'lverdi', 'password2', NULL, NULL, 'luigi.verdi@example.com', 'Milano', 20121, 'Via Milano', 2),
('Anna Bianchi', 'anna.bianchi@example.com', 'abianchi', 'password3', 'anna.bianchi@example.com', NULL, NULL, 'Napoli', 80100, 'Via Napoli', 3),
('Marco Neri', 'marco.neri@example.com', 'mneri', 'password4', 'marco.neri@example.com', NULL, NULL, 'Torino', 10121, 'Via Torino', 4),
('Carla Esposito', 'carla.esposito@example.com', 'cesposito', 'password5', 'carla.esposito@example.com', NULL, NULL, 'Firenze', 50123, 'Via Firenze', 5),
('Giorgio Bianchi', 'giorgio.bianchi@example.com', 'gbianchi', 'password6', 'giorgio.bianchi@example.com', NULL, NULL, 'Genova', 16121, 'Via Genova', 6),
('Sara Neri', 'sara.neri@example.com', 'sneri', 'password7', 'sara.neri@example.com', NULL, NULL, 'Venezia', 30121, 'Via Venezia', 7),
('Francesca Verdi', 'francesca.verdi@example.com', 'fverdi', 'password8', 'francesca.verdi@example.com', NULL, NULL, 'Roma', 00100, 'Via Roma', 1),
('Luca Rossi', 'luca.rossi@example.com', 'lrossi', 'password9', 'luca.rossi@example.com', NULL, NULL, 'Milano', 20121, 'Via Milano', 2),
('Elena Ferri', 'elena.ferri@example.com', 'eferri', 'password10', NULL, NULL, 'elena.ferri@example.com', 'Napoli', 80100, 'Via Napoli', 3),
('Riccardo Fontana', 'riccardo.fontana@example.com', 'rfontana', 'password11', NULL, NULL, 'riccardo.fontana@example.com', 'Bologna', 40126, 'Via Rizzoli', 1),
('Martina Bianchi', 'martina.bianchi@example.com', 'mbianchi', 'password12', NULL, NULL, 'martina.bianchi@example.com', 'Torino', 10121, 'Via Torino', 4);

-- Popolamento della tabella ADMIN
INSERT into ADMIN values
("gianmarcof@unibo.it"),
("filippof@unibo.it");

-- Popolamento della tabella ACQUIRENTE
INSERT INTO ACQUIRENTE (isAbbonato, email, puntiSconto) VALUES
(false, 'anna.bianchi@example.com', 30),
(false, 'carla.esposito@example.com', 10),
(false, 'giorgio.bianchi@example.com', 20),
(false, 'sara.neri@example.com', 30),
(false, 'francesca.verdi@example.com', 15),
(false, 'luca.rossi@example.com', 25),
(false, 'marco.neri@example.com', 40);

-- Popolamento della tabella VENDITORE
INSERT INTO VENDITORE (email, isBloccato, isNegozio) VALUES
('mario.rossi@example.com', false, true),
('elena.ferri@example.com', false, false),
('riccardo.fontana@example.com', false, true),
('martina.bianchi@example.com', false, false),
('luigi.verdi@example.com', false, false);

-- Popolamento della tabella PRODOTTO
INSERT INTO PRODOTTO (descrizione, codice, CONSOLE, ACCESSORIO, GIOCO, idCasaProduttrice, numeroGenerazione) VALUES
('PlayStation 5', 1001, 1, NULL, NULL, 'Sony', 5),
('Xbox Series X', 1002, 1, NULL, NULL, 'Microsoft', 4),
('Nintendo Switch', 1003, 1, NULL, NULL, 'Nintendo', 8),
('Controller PS5', 2001, NULL, 1, NULL, 'Sony', 5),
('Halo Infinite', 3001, NULL, NULL, 1, 'Microsoft', 4),
('Super Mario Odyssey', 3002, NULL, NULL, 1, 'Nintendo', 8),
('Genesis Mini', 1004, 1, NULL, NULL, 'Sega', 3),
('Pac-Man', 3003, NULL, NULL, 1, 'Atari', 1),
('Street Fighter', 3004, NULL, NULL, 1, 'Capcom', 2),
('Assassin\'s Creed', 3005, NULL, NULL, 1, 'Ubisoft', 1),
('FIFA 21', 3006, NULL, NULL, 1, 'Electronic Arts', 1),
('PlayStation 4', 1005, 1, NULL, NULL, 'Sony', 4),
('Xbox One', 1006, 1, NULL, NULL, 'Microsoft', 3),
('Wii U', 1007, 1, NULL, NULL, 'Nintendo', 7);

-- Popolamento della tabella SPECIFICHE_PRODOTTO
INSERT INTO SPECIFICHE_PRODOTTO (codice, descrizione, numeroSerie, colore) VALUES
(1001, 'PlayStation 5', 1, 'Bianco'),
(1002, 'Xbox Series X', 2, 'Nero'),
(1003, 'Nintendo Switch', 3, 'Rosso'),
(2001, 'Controller PS5', 4, 'Bianco'),
(3001, 'Halo Infinite', 5, 'Blu'),
(3002, 'Super Mario Odyssey', 6, 'Rosso'),
(1004, 'Genesis Mini', 7, 'Nero'),
(3003, 'Pac-Man', 8, 'Giallo'),
(3004, 'Street Fighter', 9, 'Verde'),
(3005, 'Assassin\'s Creed', 10, 'Grigio'),
(3006, 'FIFA 21', 11, 'Blu'),
(1005, 'PlayStation 4', 12, 'Nero'),
(1006, 'Xbox One', 13, 'Nero'),
(1007, 'Wii U', 14, 'Bianco');

-- Popolamento della tabella ANNUNCIO
INSERT INTO ANNUNCIO (punti_prodotto, id_annuncio, titolo, prezzo, descrizione, email, sconto) VALUES
(4000, 131, "PlayStation 5 Nuova", 499.99, "Consolle PlayStation 5 nuova con garanzia", "mario.rossi@example.com", 0),
(2500, 222, "Nintendo Switch Usata", 299.99, "Consolle Nintendo Switch usata ma in buone condizioni", "luigi.verdi@example.com", 0),
(3000, 31, "Xbox Series X", 499.99, "Consolle Xbox Series X nuova", "mario.rossi@example.com", 0),
(1000, 4422, "Controller PS5", 69.99, "Controller PlayStation 5 nuovo", "luigi.verdi@example.com", 0),
(1500, 567, "Super Mario Odyssey", 59.99, "Gioco Super Mario Odyssey per Nintendo Switch", "mario.rossi@example.com", 0),
(3500, 678, "Genesis Mini", 79.99, "Consolle Sega Genesis Mini", "luigi.verdi@example.com", 0),
(4000, 789, "PlayStation 4", 199.99, "Consolle PlayStation 4 usata in ottime condizioni", "mario.rossi@example.com", 0),
(3000, 890, "Xbox One", 179.99, "Consolle Xbox One usata", "luigi.verdi@example.com", 0),
(2000, 901, "Wii U", 129.99, "Consolle Wii U usata in buone condizioni", "mario.rossi@example.com", 0);

-- Popolamento della tabella DETTAGLIO
INSERT INTO DETTAGLIO (isUsato, condizioni, id_annuncio, email, codice, numeroSerie) VALUES
(0, 'Nuovo', 131, 'mario.rossi@example.com', 1001, 1),
(1, 'Buone', 222, 'luigi.verdi@example.com', 1003, 3),
(0, 'Nuovo', 31, 'mario.rossi@example.com', 1002, 2),
(0, 'Nuovo', 4422, 'luigi.verdi@example.com', 2001, 4),
(0, 'Nuovo', 567, 'mario.rossi@example.com', 3002, 6),
(0, 'Nuovo', 678, 'luigi.verdi@example.com', 1004, 7),
(1, 'Ottime', 789, 'mario.rossi@example.com', 1005, 12),
(1, 'Buone', 890, 'luigi.verdi@example.com', 1006, 13),
(1, 'Buone', 901, 'mario.rossi@example.com', 1007, 14);

-- Popolamento della tabella STATO_ORDINE
INSERT INTO STATO_ORDINE (codStato, descrizione) VALUES
('0', 'In lavorazione'),
('1', 'Spedito'),
('2', 'Consegnato');

