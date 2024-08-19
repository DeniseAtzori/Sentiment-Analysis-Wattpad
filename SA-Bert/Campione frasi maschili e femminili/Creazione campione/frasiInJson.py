import json

frasi = open("Sentence.txt", "r", encoding='UTF-8')
stringaFrasi = frasi.read()

# Splitto la mia stringa in singole stringe e le inserisco in una lista
listaFrasi = stringaFrasi.split("', '")

with open("frasiEntità.json", "w") as final:
    final.write(json.dumps(listaFrasi, ensure_ascii=False))