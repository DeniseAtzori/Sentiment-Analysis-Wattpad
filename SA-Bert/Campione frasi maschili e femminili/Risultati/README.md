# Considerazioni sulle frasi analizzate

Campione iniziale: 500 frasi.

Dopo ripulitura (eliminazione frasi senza entità o prive di sufficiente contesto) e divisione con GPT:

- numero frasi femminili: 178
- numero frasi maschili: 281

Teoria: la differenza notevole di frasi presenti tra i due sottocampioni può dipendere dal fatto che molte delle storie del DataSet sono storie d'amore, scritte in prima persona e con protagoniste femminili (quindi, in proporzione, il numero di volte che viene scritto il loro nome è minore rispetto ai personaggi comprimari maschili).

--

Differenza nel numero di frasi negative (con probabilità negativa sopra lo 0.5)

- sentiment_maschi_bert: 36
- sentiment_femmine_bert: 18

Teoria: la differenza può dipendere dalla sommenzionata differenza nel numero delle frasi iniziali tra i due sottocampioni. Può essere però anche legata al fatto che la narrazione è spesso in prima persona e riflette i sentimenti delle protagonista (che sono spesso scatenati dai comprimari maschili)

--

Differenza nel tipo di sentimento rilevato con GPT:

- nelle frasi femminili, i sentimenti negativi preponderanti sono frustrazione, difficoltà, conflitto e confusione.
- nelle frasi maschili, i sentimenti negativi preponderanti sono indifferenza, frustrazione, irritazione, preoccupazione e conflitto.

Teoria: è bene osservare che, in entrambi i sottocampioni, i sentimenti analizzati sono in larga misura provati dalla voce narrante (quasi sempre femminile).

--

Frasi femminili notevoli e relativi contesti:

- È colpa sua se tra me e te le cose non funzionano più" "Madison, non è colpa di Holly se io e te ci siamo mollati, sei tu cazzo, tu devi sempre controllare tutto e tutti e sei così finta che non so se ci sia qualcosa di vero in te" esclamò lui freddo.

Commento: la frase mette in luce una rivalità tra due personaggi femminili, in competizione per lo stesso ragazzo.
Negative: 0,982874274253845
Sentimenti evidenziati da GPT: Risentimento e frustrazione, disappunto e critica, freddezza

- "Che cosa è successo" gridai fuori di me avvicinandomi pericolosamente a lei che chiuse gli occhi impaurita "Volevamo solo spaventarla un po‘" sussurrò tra le lacrime "le ho solo dato uno schiaffo" esclamò tremante "Impossibile, uno schiaffo non avrebbe mai potuta ridurla così" osservò Andrew "Volevo solo sapere se la storia del bambino fosse vera" sussurrò senza voce "Quale bambino?" domandai confuso "Ancora con questa storia?" domandò incredulo Lincoln "Mi dispiace" sussurrò ancora "Fammi capire" esclamò Blaire avvicinandosi a Sarah "Tu hai fatto tutto questo per una stupida e fasulla voce che si racconta nei corridoi della scuola?" gridò incredula "Quale voce?

Commento: come sopra, la frase mette in luce una rivalità tra due personaggi femminili, in competizione per lo stesso ragazzo.
Negative: 0,897296249866486
Sentimenti evidenziati da GPT: Confusione, intensità emotiva, shock, rabbia, disperazione, dolore, incredulità

- <<Cazzo Ariel dammi un bacio come si deve>> afferra deciso i miei fianchi portandomi verso di lui ma lo blocco.

Commento: possibile situazione di violenza (assenza di consenso).
Negative: 0,669631779193878
Sentimenti evidenziati da GPT: Tensione, determinazione, resistenza, conflitto interiore, desiderio e ritrosia (non percepisce la violenza).

- Adeline sembra andare improvvisamente su tutte le furie, la raggiunge a passo svelto e la spintona violentemente, facendola quasi rotolare sul pavimento.

Commento: anche in questo caso, rivalità tra donne.
Negative: 0,487277895212173
Sentimenti evidenziati da GPT: Rabbia, violenza, aggressività fisica, conflitto e tensione.

--

Frasi maschili notevoli e relativi contesti:

- Non so chi sia Blake, non conosco il suo passato o quante persone abbia fatto soffrire, non so quanto in fondo si trovi la sua anima dannata ma sono sicura che, anche se per qualche secondo, sia riuscita ad intravederla nella rabbia di stamattina, negli occhi insicuri e confusi prima che le nostre labbra si toccassero per la prima volta, nei silenzi prima dei suoi gesti.

Commento: possibile "taming of the beast?"
Negative: 0,618678629398346
Sentimenti evidenziati da GPT: Curiosità, ignoranza, tormento, connessione emotiva, vulnerabilità.

- Vedo Jasmine spalancare gli occhi e guardare Mason in attesa di una sua spiegazione, ma lui non le presta la minima attenzione, continua a guardare me con aria di sfida e con rabbia.

Commento: frase interessante sulla quale approfondire il contesto.
Negative: 0,522424817085266
Sentimenti evidenziati da GPT: Aspettativa, indifferenza, aggressività, conflitto

- E ho paura che Caleb spezzi il mio cuore, lo frantumi, portandomi così in basso che sarà quasi impossibile risalire.	

Negative: 0,9782918691635130
Commento: frase interessante da analizzare, potrebbe mettere in luce un rapporto con dislivello