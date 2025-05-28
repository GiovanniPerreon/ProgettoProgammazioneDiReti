# ProgettoProgammazioneDiReti
Progetto di un Server web minimale in Python per il servizio di pagine HTML statiche.

Descrizione:
Questo progetto implementa un semplice server HTTP in Python capace di servire
un sito web statico. Il server gestisce richieste GET e restituisce file HTML e immagini dalla cartella "www".

Come si usa:
Richiesto un ambiente con Python 3.
Aprire il file server.py e se necessario posizionarsi nella cartella contenente www/ e server.py.
Il server si avvia eseguendo il file server.py.
La connessione al server avviene tramite browser all'indirizzo: http://localhost:8080.

Struttura del progetto:
- server.py         -> Codice del server
- www/              -> Contenuti del sito (HTML, immagini, CSS)
- www/index.html    -> Pagina principale

Funzionalità:
- Gestione richieste GET
- Risposte HTTP con intestazioni corrette
- Supporto per file .html, .css, .png, .jpg, .ico
- Risposta 404 per file non trovati

Autore: Giovanni Perreon
