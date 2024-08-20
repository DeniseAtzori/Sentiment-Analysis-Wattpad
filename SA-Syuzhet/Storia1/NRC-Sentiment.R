# Caricamento libreria Json e apertura documento con le frasi

library(rjson)
Storia1 <- fromJSON(file = "frasiStoria1.json")
frasiStoria1 <- unlist(frasiStoria1)

# Caricamento libreria Syuzhet
library(syuzhet)

# Definizione parametri per il sentiment con NRC

method="nrc"
lang <- "italian"

# Esecuzione sentiment con NRC-italian
sentimentStoria1 <- get_sentiment(frasiStoria1, method=method, language=lang)

# Simple plot: prende in input un vettore sentiment e applica tre metodi di smoothing (moving average, loess e discrete cosine transformation)
simple_plot(sentimentStoria1)

# Estrazione emozioni dalle frasi
emotionsStoria1 <-get_nrc_sentiment(frasiStoria1, language="italian")
View(emotionsStoria1)

# Creazione DataFrame ed esportazione in cvs
dataFrameFrasiEmotionsStoria1 <- data.frame
dataFrameFrasiEmotionsStoria1 <- data.frame(frasi=frasiStoria1, emotionsStoria)
View(dataFrameFrasiEmotionsStoria1)
write.csv(dataFrameFrasiEmotionsStoria1, "sentimentNRC.csv")

# Visualizzazione del barplot con le emozioni in percentuale
barplot(
  sort(colSums(prop.table(emotionsStoria1[, 1:8]))),
  horiz = TRUE,
  cex.names = 0.7,
  las = 1,
  main = "Emozioni in Storia105", xlab="Percentage"
)

# Creazione dei file con le frasi divise per emozione
frasiRabbia <-which(emotionsStoria1$anger > 1)
write.table(frasiStoria1[frasiRabbia], file="Risultati/frasiRabbia.txt")

frasiAnticipazione <-which(emotionsStoria1$anticipation > 1)
write.table(frasiStoria1[frasiAnticipazione], file="Risultati/frasiAnticipazione.txt")

frasiDisgusto <-which(emotionsStoria1$disgust > 1)
write.table(frasiStoria1[frasiDisgusto], file="Risultati/frasiDisgusto.txt")

frasiPaura <-which(emotionsStoria1$fear > 1)
write.table(frasiStoria1[frasiPaura], file="Risultati/frasiPaura.txt")

frasiGioia <-which(emotionsStoria1$joy > 1)
write.table(frasiStoria105[frasiGioia], file="Risultati/frasiGioia.txt")

frasiTristezza <-which(emotionsStoria1$sadness > 1)
write.table(frasiStoria1[frasiTristezza], file="Risultati/frasiTristezza.txt")
frasiSorpresa <-which(emotionsStoria1$surprise > 1)
write.table(frasiStoria1[frasiSorpresa], file="Risultati/frasiSorpresa.txt")

frasiFiducia <-which(emotionsStoria1$trust > 1)
write.table(frasiStoria1[frasiFiducia], file="Risultati/frasiFiducia.txt")