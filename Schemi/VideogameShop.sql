-- *********************************************
-- * SQL MySQL generation                      
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Tue Jul 16 10:08:08 2024 
-- * LUN file: C:\Users\forma\Desktop\VideogamePlanetShop\Gruppo2577_Elaborato\VideogameShop (LOGICO).lun 
-- * Schema: Game-Universe/1 
-- ********************************************* 


-- Database Section
-- ________________ 

create database GameUniverse;
use GameUniverse;


-- Tables Section
-- _____________ 

create table ABBONAMENTO (
     tipoAbbonamento char(20) not null,
     durata bigint not null,
     prezzo decimal(2,2) not null,
     constraint IDTARIFFARIO primary key (tipoAbbonamento));

create table ACCESSORIO (
     codice int not null,
     constraint FKPRO_ACC_ID primary key (codice));

create table ACQUIRENTE (
     isAbbonato char(1) not null,
     nome char(20) not null,
     email char(20) not null,
     password char(20) not null,
     nome_account char(20) not null,
     puntiSconto int not null,
     città char(10) not null,
     cap int not null,
     via char(20) not null,
     numero int not null,
     constraint IDCOMPRATORE_ID primary key (email),
     constraint IDCOMPRATORE_1 unique (nome_account));

create table ANNUNCIO (
     verificato char not null,
     punti_prodotto int not null,
     id_annuncio int not null,
     titolo char(15) not null,
     descrizione char(50) not null,
     dataAnnuncio date not null,
     email char(20) not null,
     constraint IDANNUNCIO primary key (id_annuncio));

create table CASA_PRODUTTRICE (
     idCasaProduttrice int not null,
     constraint IDCASA_PRODUTTRICE primary key (idCasaProduttrice));

create table compatibilità_acc (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint IDcompatibilità_acc primary key (idCasaProduttrice, numeroGenerazione, codice));

create table compatibilità_cons (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint IDcompatibilità_cons primary key (idCasaProduttrice, numeroGenerazione, codice));

create table CONSOLE (
     codice int not null,
     constraint FKPRO_CON_ID primary key (codice));

create table DETTAGLIO_ORDINE (
     id_annuncio int not null,
     idOrdine int not null,
     data date,
     ora char(5),
     constraint FKR_ID primary key (id_annuncio));

create table GENERAZIONE (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     codice int,
     Com_codice int not null,
     constraint IDGENERAZIONE_ID primary key (idCasaProduttrice, numeroGenerazione));

create table GIOCO (
     codice int not null,
     constraint FKPRO_GIO_ID primary key (codice));

create table INDIRIZZO (
     città char(10) not null,
     cap int not null,
     via char(20) not null,
     numero int not null,
     constraint IDINDIRIZZO primary key (città, cap, via, numero));

create table METODO_PAGAMENTO (
     tipologiaCarta char(10) not null,
     circuitoPagamento char(20) not null,
     codCarta bigint not null,
     scadenza date not null,
     email char(20) not null,
     Pos_email char(20) not null,
     constraint IDMETODO_PAGAMENTO primary key (circuitoPagamento, codCarta, scadenza));

create table ORDINE (
     idOrdine int not null,
     email char(20) not null,
     codStato char(1) not null,
     constraint IDORDINE_ID primary key (idOrdine));

create table PRODOTTO (
     descrizione char(50) not null,
     codice int not null,
     CONSOLE int,
     ACCESSORIO int,
     GIOCO int,
     constraint IDPRODOTTO_ID primary key (codice));

create table RECENSIONE (
     Compratore_email char(20) not null,
     Venditore_email char(20) not null,
     descrizione char(100) not null,
     valutazione int not null,
     constraint IDRECENSIONE primary key (Compratore_email, Venditore_email));

create table SCONTO (
     dataInizio date not null,
     percentuale int not null,
     dataFine date not null,
     id_annuncio int not null,
     constraint IDSCONTO primary key (dataInizio));

create table specifica (
     codice int not null,
     numeroSerie int not null,
     id_annuncio int not null,
     constraint IDspecifica primary key (id_annuncio, codice, numeroSerie));

create table SPECIFICHE_PRODOTTO (
     isUsato char(1) not null,
     condizioni char(10) not null,
     codice int not null,
     descrizione char(50) not null,
     numeroSerie int not null,
     colore char(10) not null,
     constraint IDSPECIFICHE_PRODOTTO primary key (codice, numeroSerie));

create table STATO_ORDINE (
     codStato char(1) not null,
     descrizione char(1) not null,
     constraint IDSTATO_ORDINE primary key (codStato));

create table STORICO (
     tipoAbbonamento char(20) not null,
     stato char(20) not null,
     data_inizio date not null,
     data_fine date not null,
     email char(1) not null,
     constraint IDSTORICO primary key (tipoAbbonamento, data_inizio, email));

create table TRACCIAMENTO (
     nome_magazzino char(1) not null,
     descrizione char(50) not null,
     data date not null,
     ora char(5) not null,
     città char(10) not null,
     cap int not null,
     via char(20) not null,
     numero int not null,
     constraint IDTRACCIATO_ID primary key (data, ora));

create table VENDITORE (
     isNegozio char not null,
     nome char(20) not null,
     email char(20) not null,
     password char(20) not null,
     nome_account char(20) not null,
     città char(10) not null,
     cap int not null,
     via char(20) not null,
     numero int not null,
     constraint IDVENDITORE_ID primary key (email),
     constraint IDVENDITORE_1 unique (nome_account));


-- Constraints Section
-- ___________________ 

-- Not implemented
-- alter table ACCESSORIO add constraint FKPRO_ACC_CHK
--     check(exists(select * from compatibilità_acc
--                  where compatibilità_acc.codice = codice)); 

alter table ACCESSORIO add constraint FKPRO_ACC_FK
     foreign key (codice)
     references PRODOTTO (codice);

-- Not implemented
-- alter table ACQUIRENTE add constraint IDCOMPRATORE_CHK
--     check(exists(select * from METODO_PAGAMENTO
--                  where METODO_PAGAMENTO.e-mail = e-mail)); 

alter table ACQUIRENTE add constraint FKindirizzo_compratore
     foreign key (città, cap, via, numero)
     references INDIRIZZO (città, cap, via, numero);

alter table ANNUNCIO add constraint FKvendita
     foreign key (email)
     references VENDITORE (email);

alter table compatibilità_acc add constraint FKcom_ACC
     foreign key (codice)
     references ACCESSORIO (codice);

alter table compatibilità_acc add constraint FKcom_GEN
     foreign key (idCasaProduttrice, numeroGenerazione)
     references GENERAZIONE (idCasaProduttrice, numeroGenerazione);

alter table compatibilità_cons add constraint FKcom_CON
     foreign key (codice)
     references CONSOLE (codice);

-- Not implemented
-- alter table CONSOLE add constraint FKPRO_CON_CHK
--     check(exists(select * from compatibilità_cons
--                  where compatibilità_cons.codice = codice)); 

alter table CONSOLE add constraint FKPRO_CON_FK
     foreign key (codice)
     references PRODOTTO (codice);

alter table DETTAGLIO_ORDINE add constraint FKcomposizione
     foreign key (idOrdine)
     references ORDINE (idOrdine);

alter table DETTAGLIO_ORDINE add constraint FKR_FK
     foreign key (id_annuncio)
     references ANNUNCIO (id_annuncio);

alter table DETTAGLIO_ORDINE add constraint FKR_1_FK
     foreign key (data, ora)
     references TRACCIAMENTO (data, ora);

alter table DETTAGLIO_ORDINE add constraint FKR_1_CHK
     check((data is not null and ora is not null)
           or (data is null and ora is null)); 

-- Not implemented
-- alter table GENERAZIONE add constraint IDGENERAZIONE_CHK
--     check(exists(select * from compatibilità_cons
--                  where compatibilità_cons.idCasaProduttrice = idCasaProduttrice and compatibilità_cons.numeroGenerazione = numeroGenerazione)); 

-- Not implemented
-- alter table GENERAZIONE add constraint IDGENERAZIONE_CHK
--     check(exists(select * from compatibilità_acc
--                  where compatibilità_acc.idCasaProduttrice = idCasaProduttrice and compatibilità_acc.numeroGenerazione = numeroGenerazione)); 

alter table GENERAZIONE add constraint FKrealizzazione
     foreign key (idCasaProduttrice)
     references CASA_PRODUTTRICE (idCasaProduttrice);

alter table GIOCO add constraint FKPRO_GIO_FK
     foreign key (codice)
     references PRODOTTO (codice);

alter table METODO_PAGAMENTO add constraint FKpossessione_compratore
     foreign key (email)
     references ACQUIRENTE (email);

alter table METODO_PAGAMENTO add constraint FKpossessione_venditore
     foreign key (Pos_email)
     references VENDITORE (email);

-- Not implemented
-- alter table ORDINE add constraint IDORDINE_CHK
--     check(exists(select * from DETTAGLIO_ORDINE
--                  where DETTAGLIO_ORDINE.idOrdine = idOrdine)); 

alter table ORDINE add constraint FKeffettuazione
     foreign key (email)
     references ACQUIRENTE (email);

alter table ORDINE add constraint FKstato
     foreign key (codStato)
     references STATO_ORDINE (codStato);

-- Not implemented
-- alter table PRODOTTO add constraint IDPRODOTTO_CHK
--     check(exists(select * from SPECIFICHE_PRODOTTO
--                  where SPECIFICHE_PRODOTTO.codice = codice)); 

alter table PRODOTTO add constraint ISAPRODOTTO
     check((ACCESSORIO is not null and CONSOLE is null and GIOCO is null)
           or (ACCESSORIO is null and CONSOLE is not null and GIOCO is null)
           or (ACCESSORIO is null and CONSOLE is null and GIOCO is not null)); 

alter table RECENSIONE add constraint FKvalutazione
     foreign key (Venditore_email)
     references VENDITORE (email);

alter table RECENSIONE add constraint FKfeedback
     foreign key (Compratore_email)
     references ACQUIRENTE (email);

alter table SCONTO add constraint FKprodotto_sconto
     foreign key (id_annuncio)
     references ANNUNCIO (id_annuncio);

alter table specifica add constraint FKspe_ANN
     foreign key (id_annuncio)
     references ANNUNCIO (id_annuncio);

alter table specifica add constraint FKspe_SPE
     foreign key (codice, numeroSerie)
     references SPECIFICHE_PRODOTTO (codice, numeroSerie);

alter table SPECIFICHE_PRODOTTO add constraint FKcaratteristica
     foreign key (codice)
     references PRODOTTO (codice);

alter table STORICO add constraint FKabbonamento_storico
     foreign key (tipoAbbonamento)
     references ABBONAMENTO (tipoAbbonamento);

alter table STORICO add constraint FKabbonato_storico
     foreign key (email)
     references ACQUIRENTE (email);

-- Not implemented
-- alter table TRACCIAMENTO add constraint IDTRACCIATO_CHK
--     check(exists(select * from DETTAGLIO_ORDINE
--                  where DETTAGLIO_ORDINE.data = data and DETTAGLIO_ORDINE.ora = ora)); 

alter table TRACCIAMENTO add constraint FKattuale_posizione
     foreign key (città, cap, via, numero)
     references INDIRIZZO (città, cap, via, numero);

-- Not implemented
-- alter table VENDITORE add constraint IDVENDITORE_CHK
--     check(exists(select * from METODO_PAGAMENTO
--                  where METODO_PAGAMENTO.Pos_e-mail = e-mail)); 

alter table VENDITORE add constraint FKindirizzo_venditore
     foreign key (città, cap, via, numero)
     references INDIRIZZO (città, cap, via, numero);


-- Index Section
-- _____________ 

