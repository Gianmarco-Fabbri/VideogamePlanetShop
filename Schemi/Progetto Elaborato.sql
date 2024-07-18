-- *********************************************
-- * SQL MySQL generation                      
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Wed Jul 17 12:02:53 2024 
-- * LUN file: C:\Users\forma\Desktop\VideogamePlanetShop\Schemi\VideogameShop (LOGICO).lun 
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
     prezzo decimal(4,2) not null,
     constraint IDTARIFFARIO primary key (tipoAbbonamento));

create table ACCESSORIO (
     codice int not null,
     constraint FKPRO_ACC_ID primary key (codice));

create table ACQUIRENTE (
     isAbbonato boolean not null,
     email char(50) not null,
     puntiSconto int not null,
     constraint FKUTE_ACQ_ID primary key (email));

create table ADMIN (
     email char(20) not null,
     constraint FKUTE_ADM_ID primary key (email));

create table ANNUNCIO (
     punti_prodotto int not null,
     id_annuncio int not null,
     titolo char(20) not null,
     prezzo int not null,
     descrizione char(60) not null,
     email char(50) not null,
     sconto int default 0,
     constraint IDANNUNCIO_ID primary key (id_annuncio, email));

create table CASA_PRODUTTRICE (
     idCasaProduttrice char(15) not null,
     constraint IDCASA_PRODUTTRICE primary key (idCasaProduttrice));

create table compatibilità_accessorio (
     idCasaProduttrice char(15) not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint IDcompatibilità_accessorio primary key (idCasaProduttrice, numeroGenerazione, codice));

create table compatibilità_console (
     idCasaProduttrice char(15) not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint IDcompatibilità_console primary key (idCasaProduttrice, numeroGenerazione, codice));

create table CONSOLE (
     codice int not null,
     constraint FKPRO_CON_ID primary key (codice));

create table DETTAGLIO (
     isUsato boolean not null,
     condizioni char(20) not null,
     id_annuncio int not null,
     email char(50) not null,
     codice int not null,
     numeroSerie int not null,
     constraint IDdettaglio primary key (codice, numeroSerie));

create table DETTAGLIO_ORDINE (
     id_annuncio int not null,
     email char(50) not null,
     idOrdine int not null,
     constraint IDDETTAGLIO_ORDINE primary key (id_annuncio, email));

create table GENERAZIONE (
     idCasaProduttrice char(15) not null,
     numeroGenerazione int not null,
     constraint IDGENERAZIONE_ID primary key (idCasaProduttrice, numeroGenerazione));

create table GIOCO (
     codice int not null,
     constraint FKPRO_GIO_ID primary key (codice));

create table INDIRIZZO (
     città char(20) not null,
     cap int not null,
     via char(30) not null,
     numero int not null,
     constraint IDINDIRIZZO primary key (città, cap, via, numero));

create table METODO_PAGAMENTO (
     tipologiaCarta char(20) not null,
     circuitoPagamento char(20) not null,
     codCarta bigint not null,
     scadenza date not null,
     email char(50) not null,
     constraint IDMETODO_PAGAMENTO primary key (circuitoPagamento, codCarta, scadenza));

create table ORDINE (
     idOrdine int not null,
     email char(50) not null,
     codStato char(1) not null,
     constraint IDORDINE_ID primary key (idOrdine));

create table PRODOTTO (
     descrizione char(50) not null,
     codice int not null,
     CONSOLE int,
     ACCESSORIO int,
     GIOCO int,
     idCasaProduttrice char(15) not null,
     numeroGenerazione int not null,
     constraint IDPRODOTTO primary key (codice));

create table RECENSIONE (
     email_acquirente char(50) not null,
     email_venditore char(50) not null,
     descrizione char(100) not null,
     valutazione int not null,
     constraint IDRECENSIONE primary key (email_acquirente, email_venditore));

create table SPECIFICHE_PRODOTTO (
     codice int not null,
     descrizione char(50) not null,
     numeroSerie int not null,
     colore char(10) default "-",
     constraint IDSPECIFICHE_PRODOTTO primary key (codice, numeroSerie));

create table STATO_ORDINE (
     codStato char(1) not null,
     descrizione char(20) not null,
     constraint IDSTATO_ORDINE primary key (codStato));

create table STORICO (
     Sto_tipoAbbonamento char(20) not null,
     email char(50) not null,
     tipoAbbonamento char(20) not null,
     stato char(20) not null,
     data_inizio date not null,
     data_fine date not null,
     constraint IDSTORICO primary key (email, Sto_tipoAbbonamento, tipoAbbonamento));

create table TRACCIAMENTO (
     città char(10) not null,
     cap int not null,
     via char(20) not null,
     numero int not null,
     id_annuncio int not null,
     nome_magazzino char(20) not null,
     descrizione char(50) not null,
     data date not null,
     ora char(5) not null,
     constraint IDTRACCIAMENTO primary key (id_annuncio, città, cap, via, numero));

create table UTENTE (
     nome char(20) not null,
     email char(50) not null,
     nome_account char(20) not null,
     password char(10) not null,
     ACQUIRENTE char(50),
     ADMIN char(50),
     VENDITORE char(50),
     città char(15) not null,
     cap int not null,
     via char(30) not null,
     numero int not null,
     constraint IDUTENTE_ID primary key (email),
     constraint IDUTENTE_1 unique (nome_account));

create table VENDITORE (
     email char(50) not null,
     isBloccato tinyint not null,
     isNegozio boolean not null,
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

alter table ACQUIRENTE add constraint FKUTE_ACQ_FK
     foreign key (email)
     references UTENTE (email);

alter table ADMIN add constraint FKUTE_ADM_FK
     foreign key (email)
     references UTENTE (email);

-- Not implemented
-- alter table ANNUNCIO add constraint IDANNUNCIO_CHK
--     check(exists(select * from dettaglio
--                  where dettaglio.id_annuncio = id_annuncio)); 

alter table ANNUNCIO add constraint FKvendita
     foreign key (email)
     references VENDITORE (email);

alter table compatibilità_accessorio add constraint FKcom_ACC
     foreign key (codice)
     references ACCESSORIO (codice);

alter table compatibilità_console add constraint FKcom_CON
     foreign key (codice)
     references CONSOLE (codice);

alter table compatibilità_console add constraint FKcom_GEN
     foreign key (idCasaProduttrice, numeroGenerazione)
     references GENERAZIONE (idCasaProduttrice, numeroGenerazione);

-- Not implemented
-- alter table CONSOLE add constraint FKPRO_CON_CHK
--     check(exists(select * from compatibilità_console
--                  where compatibilità_console.codice = codice)); 

alter table CONSOLE add constraint FKPRO_CON_FK
     foreign key (codice)
     references PRODOTTO (codice);

alter table DETTAGLIO add constraint FKdettaglio_prodotto
     foreign key (codice, numeroSerie)
     references SPECIFICHE_PRODOTTO (codice, numeroSerie);

alter table DETTAGLIO add constraint FKdettaglio_annuncio
     foreign key (id_annuncio, email)
     references ANNUNCIO (id_annuncio, email);

alter table DETTAGLIO_ORDINE add constraint FKcomposizione
     foreign key (idOrdine)
     references ORDINE (idOrdine);

alter table DETTAGLIO_ORDINE add constraint FKinclusione_FK
     foreign key (id_annuncio, email)
     references ANNUNCIO (id_annuncio, email);

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

alter table SPECIFICHE_PRODOTTO add constraint FKcaratteristica
     foreign key (codice)
     references PRODOTTO (codice);

alter table STORICO add constraint FKstorico_acquirente
     foreign key (email)
     references ACQUIRENTE (email);

alter table STORICO add constraint FKstorico_abbonamento
     foreign key (Sto_tipoAbbonamento)
     references ABBONAMENTO (tipoAbbonamento);

alter table TRACCIAMENTO add constraint FKstorico_tracciamento_ordine
     foreign key (id_annuncio)
     references DETTAGLIO_ORDINE (id_annuncio);

alter table TRACCIAMENTO add constraint FKstorico_tracciamento_indirizzo
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

