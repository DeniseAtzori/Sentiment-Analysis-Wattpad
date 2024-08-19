import spacy
import json

# Apro il documento json e lo trasformo in un dizionario Python
storia = open("DataSet.json", "r")
storiaPy = json.loads(storia.read())

nlp = spacy.load("it_core_news_lg")
import it_core_news_lg
nlp = it_core_news_lg.load()

entInfo = {}
fileOutput = open("NER-solo-PROPN.json", "w")
# Passo le storie una alla volta alla pipeline per evitare il sovraccarico
for el in storiaPy:
    doc = nlp(storiaPy[el]["text"])
    for Token in doc:
        if Token.ent_type_=="PER" and Token.pos_=="PROPN":
            entInfo[Token.text] = Token.pos_
fileStoria = json.dumps(entInfo, ensure_ascii=False)
fileOutput.write(fileStoria)
fileOutput.close()