-- *********************************************
-- * SQL MySQL generation                      
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Tue Jul 16 12:11:47 2024 
-- * LUN file: C:\Users\forma\Desktop\Nuova cartella\VideogameShop (LOGICO).lun 
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
     email char(20) not null,
     puntiSconto int not null,
     NON_ABBONATO char(20),
     ABBONATO char(20),
     constraint FKUTE_ACQ_ID primary key (email));

create table ANNUNCIO (
     verificato char not null,
     punti_prodotto int not null,
     id_annuncio int not null,
     titolo char(15) not null,
     descrizione char(50) not null,
     dataAnnuncio date not null,
     email char(20) not null,
     constraint IDANNUNCIO_ID primary key (id_annuncio));

create table CASA_PRODUTTRICE (
     idCasaProduttrice int not null,
     constraint IDCASA_PRODUTTRICE primary key (idCasaProduttrice));

create table CONSOLE (
     codice int not null,
     constraint FKPRO_CON_ID primary key (codice));

create table DETTAGLIO_ORDINE (
     id_annuncio int not null,
     Inc_id_annuncio int not null,
     idOrdine int not null,
     data date,
     ora char(5),
     constraint IDDETTAGLIO_ORDINE primary key (id_annuncio),
     constraint FKinclusione_ID unique (Inc_id_annuncio));

create table ADMIN (
     email char(20) not null,
     constraint FKUTE_ADM_ID primary key (email));

create table GENERAZIONE (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
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
     constraint IDMETODO_PAGAMENTO primary key (circuitoPagamento, codCarta, scadenza));

create table compatibilità_accessorio (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint IDcompatibilità_accessorio primary key (idCasaProduttrice, numeroGenerazione, codice));

create table compatibilità_console (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint IDcompatibilità_console primary key (idCasaProduttrice, numeroGenerazione, codice));

create table dettaglio (
     id_annuncio int not null,
     codice int not null,
     numeroSerie int not null,
     constraint IDdettaglio primary key (id_annuncio, codice, numeroSerie));

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
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     constraint IDPRODOTTO primary key (codice));

create table RECENSIONE (
     email_acquirente char(20) not null,
     email_venditore char(20) not null,
     descrizione char(100) not null,
     valutazione int not null,
     constraint IDRECENSIONE primary key (email_acquirente, email_venditore));

create table SCONTO (
     dataInizio date not null,
     percentuale int not null,
     dataFine date not null,
     id_annuncio int not null,
     constraint IDSCONTO primary key (dataInizio));

create table SPECIFICHE_PRODOTTO (
     codice int not null,
     condizioni char(1) not null,
     isUsato char(1) not null,
     descrizione char(50) not null,
     numeroSerie int not null,
     colore char(10) not null,
     constraint IDSPECIFICHE_PRODOTTO primary key (codice, numeroSerie));

create table STATO_ORDINE (
     codStato char(1) not null,
     descrizione char(1) not null,
     constraint IDSTATO_ORDINE primary key (codStato));

create table STORICO (
     Sto_tipoAbbonamento char(20) not null,
     email char(20) not null,
     tipoAbbonamento char(20) not null,
     stato char(20) not null,
     data_inizio date not null,
     data_fine date not null,
     constraint IDSTORICO primary key (email, Sto_tipoAbbonamento, tipoAbbonamento));

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

create table UTENTE (
     nome char(15) not null,
     email char(20) not null,
     nome_account char(20) not null,
     password char(10) not null,
     ACQUIRENTE char(20),
     ADMIN char(20),
     VENDITORE char(20),
     città char(10) not null,
     cap int not null,
     via char(20) not null,
     numero int not null,
     constraint IDUTENTE_ID primary key (email),
     constraint IDUTENTE_1 unique (nome_account));

create table VENDITORE (
     email char(20) not null,
     isNegozio char(1) not null,
     constraint FKUTE_VEN_ID primary key (email));


-- Constraints Section
-- ___________________ 

-- Not implemented
-- alter table ACCESSORIO add constraint FKPRO_ACC_CHK
--     check(exists(select * from compatibilità_accessorio
--                  where compatibilità_accessorio.codice = codice)); 

alter table ACCESSORIO add constraint FKPRO_ACC_FK
     foreign key (codice)
     references PRODOTTO (codice);

alter table ACQUIRENTE add constraint ISAACQUIRENTE
     check((ABBONATO is not null and NON_ABBONATO is null)
           or (ABBONATO is null and NON_ABBONATO is not null)); 

alter table ACQUIRENTE add constraint FKUTE_ACQ_FK
     foreign key (email)
     references UTENTE (email);

-- Not implemented
-- alter table ANNUNCIO add constraint IDANNUNCIO_CHK
--     check(exists(select * from dettaglio
--                  where dettaglio.id_annuncio = id_annuncio)); 

alter table ANNUNCIO add constraint FKvendita
     foreign key (email)
     references VENDITORE (email);

-- Not implemented
-- alter table CONSOLE add constraint FKPRO_CON_CHK
--     check(exists(select * from compatibilità_console
--                  where compatibilità_console.codice = codice)); 

alter table CONSOLE add constraint FKPRO_CON_FK
     foreign key (codice)
     references PRODOTTO (codice);

alter table DETTAGLIO_ORDINE add constraint FKcomposizione
     foreign key (idOrdine)
     references ORDINE (idOrdine);

alter table DETTAGLIO_ORDINE add constraint FKtracciato_FK
     foreign key (data, ora)
     references TRACCIAMENTO (data, ora);

alter table DETTAGLIO_ORDINE add constraint FKtracciato_CHK
     check((data is not null and ora is not null)
           or (data is null and ora is null)); 

alter table DETTAGLIO_ORDINE add constraint FKinclusione_FK
     foreign key (Inc_id_annuncio)
     references ANNUNCIO (id_annuncio);

alter table ADMIN add constraint FKUTE_ADM_FK
     foreign key (email)
     references UTENTE (email);

-- Not implemented
-- alter table GENERAZIONE add constraint IDGENERAZIONE_CHK
--     check(exists(select * from compatibilità_console
--                  where compatibilità_console.idCasaProduttrice = idCasaProduttrice and compatibilità_console.numeroGenerazione = numeroGenerazione)); 

-- Not implemented
-- alter table GENERAZIONE add constraint IDGENERAZIONE_CHK
--     check(exists(select * from compatibilità_accessorio
--                  where compatibilità_accessorio.idCasaProduttrice = idCasaProduttrice and compatibilità_accessorio.numeroGenerazione = numeroGenerazione)); 

alter table GENERAZIONE add constraint FKrealizzazione
     foreign key (idCasaProduttrice)
     references CASA_PRODUTTRICE (idCasaProduttrice);

alter table GIOCO add constraint FKPRO_GIO_FK
     foreign key (codice)
     references PRODOTTO (codice);

alter table METODO_PAGAMENTO add constraint FKpossessione
     foreign key (email)
     references UTENTE (email);

alter table compatibilità_accessorio add constraint FKcom_ACC
     foreign key (codice)
     references ACCESSORIO (codice);

alter table compatibilità_accessorio add constraint FKcom_GEN
     foreign key (idCasaProduttrice, numeroGenerazione)
     references GENERAZIONE (idCasaProduttrice, numeroGenerazione);

alter table compatibilità_console add constraint FKcom_CON
     foreign key (codice)
     references CONSOLE (codice);

alter table dettaglio add constraint FKdet_SPE
     foreign key (codice, numeroSerie)
     references SPECIFICHE_PRODOTTO (codice, numeroSerie);

alter table dettaglio add constraint FKdet_ANN
     foreign key (id_annuncio)
     references ANNUNCIO (id_annuncio);

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

alter table PRODOTTO add constraint ISAPRODOTTO
     check((ACCESSORIO is not null and CONSOLE is null and GIOCO is null)
           or (ACCESSORIO is null and CONSOLE is not null and GIOCO is null)
           or (ACCESSORIO is null and CONSOLE is null and GIOCO is not null)); 

alter table PRODOTTO add constraint FKappartenenza
     foreign key (idCasaProduttrice, numeroGenerazione)
     references GENERAZIONE (idCasaProduttrice, numeroGenerazione);

alter table RECENSIONE add constraint FKvalutazione
     foreign key (email_venditore)
     references VENDITORE (email);

alter table RECENSIONE add constraint FKfeedback
     foreign key (email_acquirente)
     references ACQUIRENTE (email);

alter table SCONTO add constraint FKsconto
     foreign key (id_annuncio)
     references ANNUNCIO (id_annuncio);

alter table SPECIFICHE_PRODOTTO add constraint FKcaratteristica
     foreign key (codice)
     references PRODOTTO (codice);

alter table STORICO add constraint FKstorico_acquirente
     foreign key (email)
     references ACQUIRENTE (email);

alter table STORICO add constraint FKstorico_abbonamento
     foreign key (Sto_tipoAbbonamento)
     references ABBONAMENTO (tipoAbbonamento);

-- Not implemented
-- alter table TRACCIAMENTO add constraint IDTRACCIATO_CHK
--     check(exists(select * from DETTAGLIO_ORDINE
--                  where DETTAGLIO_ORDINE.data = data and DETTAGLIO_ORDINE.ora = ora)); 

alter table TRACCIAMENTO add constraint FKposizione_corrente
     foreign key (città, cap, via, numero)
     references INDIRIZZO (città, cap, via, numero);

-- Not implemented
-- alter table UTENTE add constraint IDUTENTE_CHK
--     check(exists(select * from METODO_PAGAMENTO
--                  where METODO_PAGAMENTO.email = email)); 

alter table UTENTE add constraint ISAUTENTE
     check((ADMIN is not null and ACQUIRENTE is null and VENDITORE is null)
           or (ADMIN is null and ACQUIRENTE is not null and VENDITORE is null)
           or (ADMIN is null and ACQUIRENTE is null and VENDITORE is not null)); 

alter table UTENTE add constraint FKindirizzo
     foreign key (città, cap, via, numero)
     references INDIRIZZO (città, cap, via, numero);

alter table VENDITORE add constraint FKUTE_VEN_FK
     foreign key (email)
     references UTENTE (email);


-- Index Section
-- _____________ 

