import random
from contextlib import redirect_stdout

frasi = open("Sentence.txt", "r", encoding='UTF-8')
stringaFrasi = frasi.read()

# Splitto la mia stringa in singole stringe e le inserisco in una lista
listaFrasi = stringaFrasi.split("', '")

# Estraggo k frasi random per l'analisi
frasiRandom = random.choices(listaFrasi, k=500)

# Mi assicuro che non ci siano frasi ripetute
frasiuniche = set(frasiRandom)

listafrasiuniche = list(frasiuniche)

i = True
k= 0
while i:
    frasi50 = listafrasiuniche[k:k+50]
    with open(f"frasiDivise/frasiPerSA{k}.txt", "w", encoding='UTF-8') as file:
        with redirect_stdout(file):
            for el in frasi50:
                print(el)
                print("\n")
    k = k+50
    if k > len(listafrasiuniche):
        i = False


# print(len(listaFrasi))




# print(type(listaFrasi))
# print(listaFrasi)