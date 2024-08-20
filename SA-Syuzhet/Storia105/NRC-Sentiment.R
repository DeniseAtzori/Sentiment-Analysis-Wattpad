# Caricamento libreria Json e apertura documento con le frasi

library(rjson)
Storia105 <- fromJSON(file = "frasiStoria105.json")
frasiStoria105 <- unlist(Storia105)

# Caricamento libreria Syuzhet
library(syuzhet)

# Definizione parametri per il sentiment con NRC

method="nrc"
lang <- "italian"

# Esecuzione sentiment con NRC-italian
sentimentStoria105 <- get_sentiment(frasiStoria105, method=method, language=lang)

# Simple plot: prende in input un vettore sentiment e applica tre metodi di smoothing (moving average, loess e discrete cosine transformation)
simple_plot(sentimentStoria105)

# Estrazione emozioni dalle frasi
emotionsStoria105 <-get_nrc_sentiment(frasiStoria105, language="italian")
View(emotionsStoria105)

# Creazione DataFrame ed esportazione in cvs
dataFrameFrasiEmotionsStoria105 <- data.frame
dataFrameFrasiEmotionsStoria105 <- data.frame(frasi=frasiStoria105, emotionsStoria105)
View(dataFrameFrasiEmotionsStoria105)
write.csv(dataFrameFrasiEmotionsStoria105, "sentimentNRC.csv")

# Visualizzazione del barplot con le emozioni in percentuale
barplot(
  sort(colSums(prop.table(emotionsStoria105[, 1:8]))),
  horiz = TRUE,
  cex.names = 0.7,
  las = 1,
  main = "Emozioni in Storia105", xlab="Percentage"
)

# Creazione dei file con le frasi divise per emozione
frasiRabbia <-which(emotionsStoria105$anger > 1)
write.table(frasiStoria105[frasiRabbia], file="Risultati/frasiRabbia.txt")

frasiAnticipazione <-which(emotionsStoria105$anticipation > 1)
write.table(frasiStoria105[frasiAnticipazione], file="Risultati/frasiAnticipazione.txt")

frasiDisgusto <-which(emotionsStoria105$disgust > 1)
write.table(frasiStoria105[frasiDisgusto], file="Risultati/frasiDisgusto.txt")

frasiPaura <-which(emotionsStoria105$fear > 1)
write.table(frasiStoria105[frasiPaura], file="Risultati/frasiPaura.txt")

frasiGioia <-which(emotionsStoria105$joy > 1)
write.table(frasiStoria105[frasiGioia], file="Risultati/frasiGioia.txt")

frasiTristezza <-which(emotionsStoria105$sadness > 1)
write.table(frasiStoria105[frasiTristezza], file="Risultati/frasiTristezza.txt")
frasiSorpresa <-which(emotionsStoria105$surprise > 1)
write.table(frasiStoria105[frasiSorpresa], file="Risultati/frasiSorpresa.txt")

frasiFiducia <-which(emotionsStoria105$trust > 1)
write.table(frasiStoria105[frasiFiducia], file="Risultati/frasiFiducia.txt")