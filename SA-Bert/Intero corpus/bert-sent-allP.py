import torch
from torch import nn  
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import json

# Caricamento delle frasi
fileJson = open("frasiEntità.json","r")
frasi = json.load(fileJson)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("neuraly/bert-base-italian-cased-sentiment")
# Load the model, use .cuda() to load it on the GPU
model = AutoModelForSequenceClassification.from_pretrained("neuraly/bert-base-italian-cased-sentiment")

# Scorro la lista e per ciascuna frase chiamo bert

def chiamaBert(listaFrasi, nome):
    dicFrasiPol = {}
    for sentence in listaFrasi:
        # Se la frase è più lunga del massimo consentito da Bert, la splitto in sottofrasi
        if(len(sentence)<512):

        # Se la frase è più corta, procedo normalmente
            input_ids = tokenizer.encode(sentence, add_special_tokens=True)
            # Create tensor, use .cuda() to transfer the tensor to GPU
            tensor = torch.tensor(input_ids).long()
            # Fake batch dimension
            tensor = tensor.unsqueeze(0)

            # Call the model and get the logits
            logits = model(tensor).logits

            # Remove the fake batch dimension
            logits = logits.squeeze(0)

            # The model was trained with a Log Likelyhood + Softmax combined loss, hence to extract probabilities we need a softmax on top of the logits tensor
            proba = nn.functional.softmax(logits, dim=0)

            # Unpack the tensor to obtain negative, neutral and positive probabilities
            negative, neutral, positive = proba

            # Converto le probabilità da tensori a interi
            valNeg = negative.item()
            valNeu = neutral.item()
            valPos = positive.item()

            # Appendo i valori a una lista
            listaPol = []
            listaPol.append(valNeg)
            listaPol.append(valNeu)
            listaPol.append(valPos)

            # Assegno la lista come valore nel dizionario
            dicFrasiPol[sentence] = listaPol

    # Apro il file e ci scrivo il dizionario
    fileJson = open(f"{nome}Pol.json","w")
    fileJson.write(json.dumps(dicFrasiPol, ensure_ascii=False))

chiamaBert(frasi, "frasiTotali")


# print(f"Questo è il valore negativo: {negative}, questo il valore neutrale: {neutral}, questo il valore positivo: {positive}")