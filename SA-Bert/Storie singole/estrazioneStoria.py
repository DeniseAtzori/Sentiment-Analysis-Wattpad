import stanza
import json
from contextlib import redirect_stdout

stanza.download('it') # download italian model
nlp = stanza.Pipeline('it') # initialize italian neural pipeline

storie = open("DataSet.json", "r")
storiePy = json.load(storie)

doc = nlp(storiePy["2"]["text"])
i = 0
dizionarioFrasi = {}
for sentence in doc.sentences:
        dizionarioFrasi[i] = sentence.text
        i = i + 1
storiaJson = json.dumps(dizionarioFrasi, ensure_ascii=False)

fileJson = open("frasiStoria5.json","w")
fileJson.write(storiaJson)

# fileStoria = json.dumps(NERList, ensure_ascii=False)
# fileOutput.write(fileStoria)
# i=i+1

# Comando da lanciare per eseguire il file
# time python estrazioneNER-primastoria.py

