# SA-Wattpad

Questa cartella contiene i risultati di un percorso di tirocinio e tesi triennale in Informatica Umanistica, che si è concentrato sull'analisi sentimentale di un DataSet di 247 storie di Wattpad Italia.

Le storie sono state estratte da Wattpad tra marzo e aprile 2024, con l'ausilio della wattpad-api di felixApps (https://github.com/topics/wattpad-api) e sono state selezionate tra le prime 50 concluse nelle categorie italiane "Romanzi Rosa", "Vampiri", "Teen Fiction", "Fantasia" e "Fanfiction".

Per questioni di copyright, il DataSet è disponibile solo su richiesta diretta e solo ai fini della ricerca.

All'interno del progetto sono presenti:

- Una cartella "Crezione corpus" con il codice Python usato per l'estrazione, la pulizia e la normalizzazione del DataSet

- Una cartella "NER" contenente il codice Python usato per l'estrazione delle Entità Nominali attraverso Stanza e SpaCy.

- Una cartella "SA-Bert" contenente il codice Python usato per l'analisi sentimentale, eseguita sulle frasi contenenti entità estratte dal DataSet, con il modello Hugging Face di neuraly, bert-base-italian-cased-sentiment, disponibile al seguente link: https://huggingface.co/neuraly/bert-base-italian-cased-sentiment

- Una cartella "SA-Syuzhet" contenente il codice R usato per l'estrazione del sentiment e l'analisi eseguite su due storie singole.




