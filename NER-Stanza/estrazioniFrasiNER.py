import stanza
import json
from contextlib import redirect_stdout

stanza.download('it') # download italian model
nlp = stanza.Pipeline('it') # initialize italian neural pipeline

storia = open("DataSet.json", "r")
storiaPy = json.loads(storia.read())

# NERList = []
# i = 1
# fileOutput = open("NER-Stanza.txt", "w")
listaFrasiStoria = []
for el in storiaPy:
    doc = nlp(storiaPy[el]["text"])
            # scorro le frasi nel doc, per ciascuna verifico che abbia delle entità, se le ha appendo la frase in una lista
    for sentence in doc.sentences:
        if len(sentence.entities) != 0:
            listaFrasiStoria.append(sentence.text)
with open("Sentence.txt", "w") as file:
    with redirect_stdout(file):
        print(listaFrasiStoria)
    # fileStoria = json.dumps(NERList, ensure_ascii=False)
    # fileOutput.write(fileStoria)
    # i=i+1
file.close()

# Comando da lanciare per eseguire il file
# time python estrazioneNER-primastoria.py   