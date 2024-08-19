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
for el in storiaPy:
    doc = nlp(storiaPy[el]["text"])
    with open("NER-stanza.txt", "w") as file:
        with redirect_stdout(file):
            print(doc.entities)
    
    # fileStoria = json.dumps(NERList, ensure_ascii=False)
    # fileOutput.write(fileStoria)
    # i=i+1
    exit()

file.close()

# Comando da lanciare per eseguire il file
# time python estrazioneNER-primastoria.py   