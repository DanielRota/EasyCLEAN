![Title](EasyCLEAN//Images//Logo.png)

# INTRODUZIONE

Il Plugin EasyCLEAN nasce dalla necessità di velocizzare il processo di semplificazione dei profili utensili, tramite il software EasyWOOD. Esso mette a disposizione una serie di funzionalità dedite all'automatizzazione di attività prima svolte manualmente, come la rimozione di entità, la creazione della sagoma di un utensile e la selezione delle parti taglienti.

# FUNZIONALITÀ E UTILIZZO

La casella di testo *"Fase d'esecuzione"* mostra l'operazione corrente da eseguire e si aggiorna con il progredire di quest'ultime.

1. **APRI FILE**: Permette di aprire un file .dwg o .dxf direttamente dal proprio *"Esplora file"*.

2. **AZZERA**: Apre nuovamente il file selezionato in precedenza, ripristinando tutte le modifiche effettuate.

3. **NASCONDI ALTRI UTENSILI**: Rende l'area selezionata dall'utente l'unica visibile all'interno del disegno corrente.

4. **ELIMINA**: Rimuove tutte le entità corrispondenti al tipo scelto dall'utente nelle apposite CheckBox a lato, rendendo il piano libero da oggetti non necessari; è possibile eliminare automaticamente le seguenti entità: testi, cerchi, quote e superfici.

5. **SELEZIONA ORIGINE**: Ottiene l'origine selezionata dall'utente, ovvero la linea dalla quale verrà sviluppato il profilo dell'utensile (Essa non necessità di una specifica angolazione o posizione).  

6. **RICAVA SAGOMA**: Dopo aver selezionato i coltelli e aver premuto il pulsante, verrà calcolata la sagoma dell'utensile scelto inizialmente. Il profilo utensile verrà inoltre ruotato a seconda dell'inclinazione dell'origine
Dopo aver ricavato la sagoma, viene caricata a schermo l'anteprima della stessa attraverso una scena.

7. **SELEZIONA PARTI TAGLIENTI**: Selezionando le parti taglienti della sagoma, queste vengono colorate di rosso. è possibile annullare l'operazione premendo il tasto destro del mouse sul bottone, facendo in modo che le entità selezionate tornino ad essere blu.

8. **SALVA FILE**: Consente di salvare un nuovo file .ewd, l'utensile specchiato, spostato sull'origine e ruotato adeguatamente.

**Nota bene**: Alcune fra le diverse funzionalità vengono abilitate solo con l'avanzamento nelle operazioni, non è quindi possibile, ad esempio, ricavare la silhouette dell'utensile prima di averne selezionata l'origine.

## SVILUPPO

Il seguente Plugin è stato sviluppato durante un periodo di stage, le singole attività sono state distribuite nel seguente modo:

* Dialogo e Interfaccia Grafica: *Riccardo Nasatti* e *Mattia Rocchi*
* Modulo funzioni e Documentazione: *Daniel Rota*
* Creazione Loghi, Icone e Messaggi: *Filippo Graziano*
