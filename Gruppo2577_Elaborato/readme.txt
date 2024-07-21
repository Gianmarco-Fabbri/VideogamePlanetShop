# Videogame Planet Shop

Prima di eseguire l'applicativo è necessario creare e popolare il database GameUniverse.
Si devono eseguire i file "GameUniverse.sql" e "FillDataBase.sql" collocati nella directory "DataBase" tramite l'applicazione MySQL Workbench.

Prima di spiegare come avviare l'applicazione specifichiamo che è necessario scaricare i seguenti pacchetti:
-MySQL Connector, Pandas, Matplotlib e PyInstaller.
Lo si può fare tramite i seguenti comandi da terminale:
-pip install mysql-connector-python
-pip install pandas
-pip install matplotlib
-pip install pyinstaller

Ancor prima di avviare l'applicazione è necessario modificare il file "config.py" e aggiornare i dati con i dati della propria connessione.

Una volta creato e popolato il database si deve eseguire il file main.py che avvia l'applicazione tramite:
-Un terminale collocandosi all'interno della directory "CodiceApplicativo" e digitare
il comando "python main.py".
-Un ambiente di sviluppo come Visual Studio Code aprendo la cartella "CodiceApplicativo" ed eseguendo il file di avvio.

Una volta avviata si presenterà la finestra di login in cui sarà possibile inserire email e password di un utente.
Lasciamo 3 esempi di email e password che saranno presenti nel database se tutto è andato a buon fine:

-ADMIN -->       email: gianmarcof@unibo.it              password: gian03
-VENDITORE -->   email: martina.bianchi@example.com      password: password12
-COMPRATORE -->  email: carla.esposito@example.com       password: password5

Attraverso l'inserimento di questi tre utenti sarà possibile visualizzare tutte e tre le interfacce principali e svolgere
le operazioni fornite dal sistema.
