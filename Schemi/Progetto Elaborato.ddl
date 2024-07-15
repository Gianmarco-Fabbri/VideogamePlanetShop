-- *********************************************
-- * Standard SQL generation                   
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Sun Jul 14 11:19:06 2024 
-- * LUN file: C:\Users\forma\Desktop\VideogameShop (LOGICO).lun 
-- * Schema: Game-Universe/SQL 
-- ********************************************* 


-- Database Section
-- ________________ 

create database GameUniverse;


-- DBSpace Section
-- _______________


-- Tables Section
-- _____________ 

create table ABBONAMENTO (
     tipoAbbonamento char(20) not null,
     durata int not null,
     prezzo int not null,
     constraint ID_ABBONAMENTO_ID primary key (tipoAbbonamento));

create table ACCESSORIO (
     codice int not null,
     constraint ID_ACCES_PRODO_ID primary key (codice));

create table ACQUIRENTE (
     isAbbonato boolean not null,
     nome char(20) not null,
     e_mail char(30) not null,
     password char(15) not null,
     nome_account char(15) not null,
     puntiSconto int not null,
     citta char(10) not null,
     cap int not null,
     via char(20) not null,
     numero int not null,
     constraint ID_ACQUIRENTE_ID primary key (e_mail),
     constraint SID_ACQUIRENTE_ID unique (nome_account));

create table ANNUNCIO (
     verificato char not null,
     punti_prodotto int not null,
     id_annuncio int not null,
     titolo char(15) not null,
     descrizione char(50) not null,
     dataAnnuncio date not null,
     e_mail char(30) not null,
     constraint ID_ANNUNCIO_ID primary key (id_annuncio));

create table CASA_PRODUTTRICE (
     idCasaProduttrice int primary key);
     

create table codice (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint ID_codice_ID primary key (idCasaProduttrice, numeroGenerazione, codice));

create table Com_codice (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     Com_codice int not null,
     constraint ID_Com_codice_ID primary key (idCasaProduttrice, numeroGenerazione, Com_codice));

create table compatibilita_acc (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint ID_compatibilita_acc_ID primary key (idCasaProduttrice, numeroGenerazione, codice));

create table compatibilita_cons (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     codice int not null,
     constraint ID_compatibilita_cons_ID primary key (idCasaProduttrice, numeroGenerazione, codice));

create table CONSOLE (
     codice int not null,
     constraint ID_CONSO_PRODO_ID primary key (codice));

create table DETTAGLIO_ORDINE (
     id_annuncio int not null,
     idOrdine int not null,
     data_dettaglio date,
     ora char(5),
     constraint ID_DETTA_ANNUN_ID primary key (id_annuncio));

create table GENERAZIONE (
     idCasaProduttrice int not null,
     numeroGenerazione int not null,
     constraint ID_GENERAZIONE_ID primary key (idCasaProduttrice, numeroGenerazione));

create table GIOCO (
     codice int not null,
     constraint ID_GIOCO_PRODO_ID primary key (codice));

create table INDIRIZZO (
     citta char(10) not null,
     cap int not null,
     via char(20) not null,
     numero int not null,
     constraint ID_INDIRIZZO_ID primary key (citta, cap, via, numero));

create table METODO_PAGAMENTO (
     tipologiaCarta char(10) not null,
     circuitoPagamento char(20) not null,
     codCarta int not null,
     scadenza date not null,
     e_mail char(30) not null,
     Pos_e_mail char(30) not null,
     constraint ID_METODO_PAGAMENTO_ID primary key (circuitoPagamento, codCarta, scadenza));

create table ORDINE (
     idOrdine int not null,
     e_mail char(30) not null,
     codStato char(1) not null,
     constraint ID_ORDINE_ID primary key (idOrdine));

create table PRODOTTO (
     descrizione char(50) not null,
     codice int not null,
     CONSOLE int,
     ACCESSORIO int,
     GIOCO int,
     constraint ID_PRODOTTO_ID primary key (codice));

create table RECENSIONE (
     Compratore_e_mail char(30) not null,
     Venditore_e_mail char(30) not null,
     descrizione char(100) not null,
     valutazione numeric(1) not null,
     constraint ID_RECENSIONE_ID primary key (Compratore_e_mail, Venditore_e_mail));

create table SCONTO (
     dataInizio date not null,
     percentuale numeric(3) not null,
     dataFine date not null,
     id_annuncio numeric(10) not null,
     constraint ID_SCONTO_ID primary key (dataInizio));

create table specifica (
     codice numeric(10) not null,
     numeroSerie numeric(10) not null,
     id_annuncio numeric(10) not null,
     constraint ID_specifica_ID primary key (id_annuncio, codice, numeroSerie));

create table SPECIFICHE_PRODOTTO (
     isUsato char(1) not null,
     condizioni char(1) not null,
     codice numeric(10) not null,
     descrizione char(50) not null,
     numeroSerie numeric(10) not null,
     colore char(10) not null,
     constraint ID_SPECIFICHE_PRODOTTO_ID primary key (codice, numeroSerie));

create table STATO_ORDINE (
     codStato char(1) not null,
     descrizione char(1) not null,
     constraint ID_STATO_ORDINE_ID primary key (codStato));

create table STORICO (
     tipoAbbonamento char(20) not null,
     stato char(20) not null,
     data_inizio date not null,
     data_fine date not null,
     e_mail char(1) not null,
     constraint ID_STORICO_ID primary key (tipoAbbonamento, data_inizio, e_mail));

create table TRACCIAMENTO (
     nome_magazzino char(1) not null,
     descrizione char(50) not null,
     data date not null,
     ora char(5) not null,
     citta char(10) not null,
     cap numeric(6) not null,
     via char(20) not null,
     numero numeric(3) not null,
     constraint ID_TRACCIAMENTO_ID primary key (data, ora));

create table VENDITORE (
     isNegozio char not null,
     nome char(1) not null,
     e_mail char(1) not null,
     password char(1) not null,
     nome_account char(1) not null,
     citta char(10) not null,
     cap numeric(6) not null,
     via char(20) not null,
     numero numeric(3) not null,
     constraint ID_VENDITORE_ID primary key (e_mail),
     constraint SID_VENDITORE_ID unique (nome_account));


-- Constraints Section
-- ___________________ 

alter table ACCESSORIO add constraint ID_ACCES_PRODO_CHK
     check(exists(select * from compatibilita_acc
                  where compatibilita_acc.codice = codice)); 

alter table ACCESSORIO add constraint ID_ACCES_PRODO_FK
     foreign key (codice)
     references PRODOTTO;

alter table ACQUIRENTE add constraint ID_ACQUIRENTE_CHK
     check(exists(select * from METODO_PAGAMENTO
                  where METODO_PAGAMENTO.e_mail = e_mail)); 

alter table ACQUIRENTE add constraint REF_ACQUI_INDIR_FK
     foreign key (citta, cap, via, numero)
     references INDIRIZZO;

alter table ANNUNCIO add constraint REF_ANNUN_VENDI_FK
     foreign key (e_mail)
     references VENDITORE;

alter table codice add constraint FKGEN_cod
     foreign key (idCasaProduttrice, numeroGenerazione)
     references GENERAZIONE;

alter table Com_codice add constraint FKGEN_Com
     foreign key (idCasaProduttrice, numeroGenerazione)
     references GENERAZIONE;

alter table compatibilita_acc add constraint EQU_c_A_ACCES_FK
     foreign key (codice)
     references ACCESSORIO;

alter table compatibilita_acc add constraint EQU_c_A_GENER
     foreign key (idCasaProduttrice, numeroGenerazione)
     references GENERAZIONE;

alter table compatibilita_cons add constraint EQU_compa_CONSO_FK
     foreign key (codice)
     references CONSOLE;

alter table compatibilita_cons add constraint EQU_compa_GENER
     foreign key (idCasaProduttrice, numeroGenerazione)
     references GENERAZIONE;

alter table CONSOLE add constraint ID_CONSO_PRODO_CHK
     check(exists(select * from compatibilita_cons
                  where compatibilita_cons.codice = codice)); 

alter table CONSOLE add constraint ID_CONSO_PRODO_FK
     foreign key (codice)
     references PRODOTTO;

alter table DETTAGLIO_ORDINE add constraint EQU_DETTA_ORDIN_FK
     foreign key (idOrdine)
     references ORDINE;

alter table DETTAGLIO_ORDINE add constraint ID_DETTA_ANNUN_FK
     foreign key (id_annuncio)
     references ANNUNCIO;

alter table DETTAGLIO_ORDINE add constraint EQU_DETTA_TRACC_FK
     foreign key (data, ora)
     references TRACCIAMENTO;

alter table DETTAGLIO_ORDINE add constraint EQU_DETTA_TRACC_CHK
     check((data is not null and ora is not null)
           or (data is null and ora is null)); 

alter table GENERAZIONE add constraint ID_GENERAZIONE_CHK
     check(exists(select * from Com_codice
                  where Com_codice.idCasaProduttrice = idCasaProduttrice and Com_codice.numeroGenerazione = numeroGenerazione)); 

alter table GENERAZIONE add constraint ID_GENERAZIONE_CHK
     check(exists(select * from compatibilita_cons
                  where compatibilita_cons.idCasaProduttrice = idCasaProduttrice and compatibilita_cons.numeroGenerazione = numeroGenerazione)); 

alter table GENERAZIONE add constraint ID_GENERAZIONE_CHK
     check(exists(select * from compatibilita_acc
                  where compatibilita_acc.idCasaProduttrice = idCasaProduttrice and compatibilita_acc.numeroGenerazione = numeroGenerazione)); 

alter table GENERAZIONE add constraint REF_GENER_CASA_
     foreign key (idCasaProduttrice)
     references CASA_PRODUTTRICE;

alter table GIOCO add constraint ID_GIOCO_PRODO_FK
     foreign key (codice)
     references PRODOTTO;

alter table METODO_PAGAMENTO add constraint EQU_METOD_ACQUI_FK
     foreign key (e_mail)
     references ACQUIRENTE;

alter table METODO_PAGAMENTO add constraint EQU_METOD_VENDI_FK
     foreign key (Pos_e_mail)
     references VENDITORE;

alter table ORDINE add constraint ID_ORDINE_CHK
     check(exists(select * from DETTAGLIO_ORDINE
                  where DETTAGLIO_ORDINE.idOrdine = idOrdine)); 

alter table ORDINE add constraint REF_ORDIN_ACQUI_FK
     foreign key (e_mail)
     references ACQUIRENTE;

alter table ORDINE add constraint REF_ORDIN_STATO_FK
     foreign key (codStato)
     references STATO_ORDINE;

alter table PRODOTTO add constraint ID_PRODOTTO_CHK
     check(exists(select * from SPECIFICHE_PRODOTTO
                  where SPECIFICHE_PRODOTTO.codice = codice)); 

alter table PRODOTTO add constraint EXTONE_PRODOTTO
     check((ACCESSORIO is not null and CONSOLE is null and GIOCO is null)
           or (ACCESSORIO is null and CONSOLE is not null and GIOCO is null)
           or (ACCESSORIO is null and CONSOLE is null and GIOCO is not null)); 

alter table RECENSIONE add constraint REF_RECEN_VENDI_FK
     foreign key (Venditore_e_mail)
     references VENDITORE;

alter table RECENSIONE add constraint REF_RECEN_ACQUI
     foreign key (Compratore_e_mail)
     references ACQUIRENTE;

alter table SCONTO add constraint REF_SCONT_ANNUN_FK
     foreign key (id_annuncio)
     references ANNUNCIO;

alter table specifica add constraint REF_speci_ANNUN
     foreign key (id_annuncio)
     references ANNUNCIO;

alter table specifica add constraint REF_speci_SPECI_FK
     foreign key (codice, numeroSerie)
     references SPECIFICHE_PRODOTTO;

alter table SPECIFICHE_PRODOTTO add constraint EQU_SPECI_PRODO
     foreign key (codice)
     references PRODOTTO;

alter table STORICO add constraint REF_STORI_ABBON
     foreign key (tipoAbbonamento)
     references ABBONAMENTO;

alter table STORICO add constraint REF_STORI_ACQUI_FK
     foreign key (e_mail)
     references ACQUIRENTE;

alter table TRACCIAMENTO add constraint ID_TRACCIAMENTO_CHK
     check(exists(select * from DETTAGLIO_ORDINE
                  where DETTAGLIO_ORDINE.data = data and DETTAGLIO_ORDINE.ora = ora)); 

alter table TRACCIAMENTO add constraint REF_TRACC_INDIR_FK
     foreign key (citta, cap, via, numero)
     references INDIRIZZO;

alter table VENDITORE add constraint ID_VENDITORE_CHK
     check(exists(select * from METODO_PAGAMENTO
                  where METODO_PAGAMENTO.Pos_e_mail = e_mail)); 

alter table VENDITORE add constraint REF_VENDI_INDIR_FK
     foreign key (citta, cap, via, numero)
     references INDIRIZZO;


-- Index Section
-- _____________ 

create unique index ID_ABBONAMENTO_IND
     on ABBONAMENTO (tipoAbbonamento);

create unique index ID_ACCES_PRODO_IND
     on ACCESSORIO (codice);

create unique index ID_ACQUIRENTE_IND
     on ACQUIRENTE (e_mail);

create unique index SID_ACQUIRENTE_IND
     on ACQUIRENTE (nome_account);

create index REF_ACQUI_INDIR_IND
     on ACQUIRENTE (citta, cap, via, numero);

create unique index ID_ANNUNCIO_IND
     on ANNUNCIO (id_annuncio);

create index REF_ANNUN_VENDI_IND
     on ANNUNCIO (e_mail);

create unique index ID_CASA_PRODUTTRICE_IND
     on CASA_PRODUTTRICE (idCasaProduttrice);

create unique index ID_codice_IND
     on codice (idCasaProduttrice, numeroGenerazione, codice);

create unique index ID_Com_codice_IND
     on Com_codice (idCasaProduttrice, numeroGenerazione, Com_codice);

create unique index ID_compatibilita_acc_IND
     on compatibilita_acc (idCasaProduttrice, numeroGenerazione, codice);

create index EQU_c_A_ACCES_IND
     on compatibilita_acc (codice);

create unique index ID_compatibilita_cons_IND
     on compatibilita_cons (idCasaProduttrice, numeroGenerazione, codice);

create index EQU_compa_CONSO_IND
     on compatibilita_cons (codice);

create unique index ID_CONSO_PRODO_IND
     on CONSOLE (codice);

create index EQU_DETTA_ORDIN_IND
     on DETTAGLIO_ORDINE (idOrdine);

create unique index ID_DETTA_ANNUN_IND
     on DETTAGLIO_ORDINE (id_annuncio);

create index EQU_DETTA_TRACC_IND
     on DETTAGLIO_ORDINE (data, ora);

create unique index ID_GENERAZIONE_IND
     on GENERAZIONE (idCasaProduttrice, numeroGenerazione);

create unique index ID_GIOCO_PRODO_IND
     on GIOCO (codice);

create unique index ID_INDIRIZZO_IND
     on INDIRIZZO (citta, cap, via, numero);

create unique index ID_METODO_PAGAMENTO_IND
     on METODO_PAGAMENTO (circuitoPagamento, codCarta, scadenza);

create index EQU_METOD_ACQUI_IND
     on METODO_PAGAMENTO (e_mail);

create index EQU_METOD_VENDI_IND
     on METODO_PAGAMENTO (Pos_e_mail);

create unique index ID_ORDINE_IND
     on ORDINE (idOrdine);

create index REF_ORDIN_ACQUI_IND
     on ORDINE (e_mail);

create index REF_ORDIN_STATO_IND
     on ORDINE (codStato);

create unique index ID_PRODOTTO_IND
     on PRODOTTO (codice);

create unique index ID_RECENSIONE_IND
     on RECENSIONE (Compratore_e_mail, Venditore_e_mail);

create index REF_RECEN_VENDI_IND
     on RECENSIONE (Venditore_e_mail);

create unique index ID_SCONTO_IND
     on SCONTO (dataInizio);

create index REF_SCONT_ANNUN_IND
     on SCONTO (id_annuncio);

create unique index ID_specifica_IND
     on specifica (id_annuncio, codice, numeroSerie);

create index REF_speci_SPECI_IND
     on specifica (codice, numeroSerie);

create unique index ID_SPECIFICHE_PRODOTTO_IND
     on SPECIFICHE_PRODOTTO (codice, numeroSerie);

create unique index ID_STATO_ORDINE_IND
     on STATO_ORDINE (codStato);

create index REF_STORI_ACQUI_IND
     on STORICO (e_mail);

create unique index ID_STORICO_IND
     on STORICO (tipoAbbonamento, data_inizio, e_mail);

create unique index ID_TRACCIAMENTO_IND
     on TRACCIAMENTO (data, ora);

create index REF_TRACC_INDIR_IND
     on TRACCIAMENTO (citta, cap, via, numero);

create unique index ID_VENDITORE_IND
     on VENDITORE (e_mail);

create unique index SID_VENDITORE_IND
     on VENDITORE (nome_account);

create index REF_VENDI_INDIR_IND
     on VENDITORE (citta, cap, via, numero);

