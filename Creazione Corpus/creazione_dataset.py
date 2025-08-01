# -*- coding: utf-8 -*-
"""Creazione dataset.ipynb

Automatically generated by Colab.

PRIMO PASSO: CREAZIONE DELLE LISTE CHE CONTENGONO LE STORIE DA INSERIRE NEL DATASET (250 STORIE)

NB: i link contenuti nelle liste sono stati oscurati per ragioni di copyright.

Lista che contiene i link alla prime 50 storie "Sensazionali" in Romanzi rosa (solo complete) - estratte in data 25 marzo 2024
"""
romanziRosa = []
"""Lista che contiene i link alla prime 50 storie "Sensazionali" in Vampiri (solo complete) - estratte in data 5 aprile 2024"""
vampiri = []
"""Lista che contiene i link alla prime 50 storie "Sensazionali" in Teen Fiction (solo complete) - estratte in data 5 aprile 2024"""
teenFiction = []
"""Lista che contiene i link alla prime 50 storie "Sensazionali" in Fantasia (solo complete) - estratte in data 10 aprile 2024"""
fantasia = []
"""Lista che contiene i link alla prime 50 storie "Sensazionali" in Fanfiction (solo complete) - estratte in data 10 aprile 2024"""
fanfiction = []
"""SECONDO PASSO: CONFRONTO TRA LE LISTE PER ELIMINARE I DUPLICATI

Creo una lista unica
"""

listaStorieDup = romanziRosa + vampiri + teenFiction + fantasia + fanfiction

"""Elimino i duplicati"""

listaStorie = list(dict.fromkeys(listaStorieDup))

len(listaStorie)

from pprint import *

"""\DIVIDO LA LISTA IN SOTTOLISTE PER VELOCIZZARE L'ESTRAZIONE (RIMUOVO DUE STORIE NON PIU' DISPONIBILI)"""

listaStorie.remove()

from itertools import islice

length_to_split = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
Inputt = iter(listaStorie)
listaSplittata = [list(islice(Inputt, elem))
        for elem in length_to_split]

"""TERZO PASSO: ESTRAZIONE DELLE STORIE

Importo il modulo per l'estrazione delle storie
"""

from google.colab import files
uploaded = files.upload()

import WattpadConnect

"""Creo una lista che contiene il dataset e un dizionario che memorizza:

*   Come chiave, il titolo della storia
*   Come valore, il nome dell'autore e il testo

Cicli for annidati:

*   Primo ciclo: scorre la listaStorie (che contiene tutti gli url delle storie), per ciascun elemento lancia il WattpadConnect, estrae il titolo e le parti e li butta il primo in una stringa e il secondo in una lista
*   Secondo ciclo: scorre la lista parts (che contiene gli url delle parti della storia), per ciascun elemento estrae solo l'url e lo butta nella lista urlCapitoli
*   Terzo ciclo: scorre la lista urlCapitoli (che contiene gli url delle parti della storia), per ogni elemento rilancia il WattpadConnct ed estrae lo storytext, che aggiunge alla stringa dataSet.

Completato i due cicli interni, ripulisco il testo con le regex e lo inserisco nel dizionario, con chiave storytitle e valore (authorname,testoStoria)
"""

import json

bla = {
    "ID_testo":{
        "metadata":{
            "title":"Bla",
            "author":"BlaBla"
        },
        "text":"blablablabla"
    }
}

def estrazioneStorie(lista,numeroStoria):
  dizionarioStorie = {}
  scorri = range(239,248)
  for n in scorri:
    testoStoria = ''
    jsonStoria = WattpadConnect.extractInformationFromWattpad(lista[n])
    if not(jsonStoria["metadata"]["data"]["group"]["title"]!=None and jsonStoria["metadata"]["data"]["group"]["user"]["name"]!=None and jsonStoria["metadata"]["data"]["group"]["parts"]!=None):
      print("fuck")
      return
    else:
      storytitle = jsonStoria["metadata"]["data"]["group"]["title"]
      authorname = jsonStoria["metadata"]["data"]["group"]["user"]["name"]
      parts = jsonStoria["metadata"]["data"]["group"]["parts"]
      urlCapitoli = []
      for el in parts:
        urlCapitoli.append(el['url'])
      for i in urlCapitoli:
        jsonCapitolo = WattpadConnect.extractInformationFromWattpad(i)
        if not(jsonCapitolo["metadata"]["data"]["storyText"]!=None):
          print("fuck2")
          return
        else:
          storytext = jsonCapitolo["metadata"]["data"]["storyText"]
          testoStoria = testoStoria+storytext
      storia = {
        "metadata":{
            "title": storytitle,
            "author": authorname
        },
        "text": testoStoria
      }
      dizionarioStorie[numeroStoria] = storia

      dizionarioWattpad = open("corpusStorie.json", "a")
      dizionarioWattpad.write(f"\"{numeroStoria}\": "+json.dumps(dizionarioStorie[numeroStoria]))
      dizionarioWattpad.write(',')
      dizionarioWattpad.close()
      numeroStoria += 1

"""LANCIO LA MIA FUNZIONE, INSERENDO I RISULTATI IN UNA VARIABILE DIZIONARIOCOMPLETO"""

corpus = estrazioneStorie(listaStorie,239)

files.download('corpusStorie.json')

dizionarioCompleto1 = estrazioneStorie(listaSplittata[0],0)

dizionarioWattpad = open("corpusCompleto.json", "w")
dizionarioWattpad.write(json.dumps(dizionarioCompleto1))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto2 = estrazioneStorie(listaSplittata[1],25)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto2))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto3 = estrazioneStorie(listaSplittata[2],25)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto3))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto4 = estrazioneStorie(listaSplittata[3],75)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto4))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto5 = estrazioneStorie(listaSplittata[4],100)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto5))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto6 = estrazioneStorie(listaSplittata[5],125)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto6))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto7 = estrazioneStorie(listaSplittata[6],150)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto7))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto8 = estrazioneStorie(listaSplittata[7],175)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto8))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto9 = estrazioneStorie(listaSplittata[8],200)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto9))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

dizionarioCompleto10 = estrazioneStorie(listaSplittata[9],225)

dizionarioWattpad = open("corpusCompleto.json", "a")
dizionarioWattpad.write(json.dumps(dizionarioCompleto10))

dizionarioWattpad.close()

files.download('corpusCompleto.json')

"""APRO UN FILE E SCRIVO AL SUO INTERNO IL CORPUS"""

files.download('corpusCompleto.json')

"""PULIZIA DEL TESTO CON LE REGEX

Importo il modulo per le Regex
"""

import re

"""Definisco la mia lista di regex e la funzione di sostituzione"""

listaRegex1 = [
    ('&lt;p data-.+?&gt;',''),
    ('&lt;a href=.+?&gt;(.+?)&lt;\/a&gt;','\1'),
    ('&#x[0-9A-Za-z]{5};',''),
    ('&lt;img.+?&gt;','')
]

listaRegex2= [
    ('&#xA1;','¡'),
    ('&#xF2;','ò'),
    ('&#xE9;','é'),
    ('&amp;','&'),
    ('&#xE8;','è'),
    ('&apos;','‘'),
    ('&#xEC;','ì'),
    ('&#xE0;','à'),
    ('&#xF3;','ó'),
    ('&#xE1;','á'),
    ('&#xF9;','ù'),
    ('&#xAB;','«'),
    ('&#xBB;','»'),
    ('&#xC8;','È'),
    ('&#xFA;','ú'),
    ('&#x2013;','-'),
    ('&quot;','"'),
    ('&#xA0;',' '),
    ('&#xB2;','²'),
    ('&lt;','<'),
    ('&gt;','>'),
    ('&#xe7;','ç'),
    ('&#xa9;','©'),
    ('&#xED;','í'),
    ('&#x2019;','’'),
    ('&#xC9;','É'),
    ('&#xEB;','ë'),
    ('&#xa9;',"©"),
    ('&#x107;','ć'),
    ('&#x2026;','…'),
    ('&#x300B;','»'),
    ('&#x300A;','«'),
    ('&#xFB;','û'),
    ('&#xB0;','°'),
    ('&#x2728;',''),
    ('&#x1F31F;',''),
    ('&#x1F60C;',''),
    ('&#x1F384;',''),
    ('&#x1F385;',''),
    ('&#x1F381;',''),
    ('#xD7;',''),
    ('&#x1F63B;',''),
    ('&#x1F445;',''),
    ('&#x1F498;',''),
    ('&#x1F496;',''),
    ('&#x1F31F;',''),
    ('&#xF04;',''),
    ('&#x2661;',''),
    ('&#x2661;',''),
    ('&#x1F92B;',''),
    ('&#x1F525;',''),
    ('#x1F60F;',''),
    ('&#x1F91D;',''),
    ('&#x1F3FB;',''),
    ('&#xFE0F;',''),
    ('&lt;br&gt;',''),
    ('&lt;/p&gt;',''),
    ('&lt;b&gt;',''),
    ('&lt;i&gt;',''),
    ('&lt;/i&gt;',''),
    ('&lt;/b&gt;',''),
    ('&lt;strong&gt;&lt;em&gt;',''),
    ('&lt;/em&gt;&lt;/strong&gt;',''),
    ('&lt;em&gt;&lt;strong&gt;',''),
    ('&lt;/strong&gt;&lt;/em&gt;',''),
    ('&lt;strong&gt;',''),
    ('&lt;/strong&gt;',''),
    ('&lt;em&gt;',''),
    ('&lt;u&gt;',''),
    ('&lt;/u&gt;',''),
    ('&lt;/em&gt;',''),
    ('&lt;3',''),
    ('&#x200B;',''),
    ('&#x2764;',''),
    ('&#x200D;',''),
    ('&#x2640;',''),
    ('&#x270B;',''),
    ('&#x2665;',''),
    ('&#x2022;',''),
    ('&#x25CF;',''),
    ('&#x2B50;',''),
    ('&#x261D;',''),
    ('&#x2763;',''),
    ('&#x300;',''),
    ('&#x26A0;',''),
    ('&#xD6;','Ö'),
    ('&#x25B6;',''),
    ('&#xF6;','ö'),
    ('&#x201C','“'),
    ('&#x201D;','”'),
    ('&#x2014;','—'),
    ('&#x20AC;','€'),
    ('&#xD9;','Ù'),
    ('&#xD2;','Ò'),
    ('&#xF4;','ô'),
    ('&#xEA;','ê'),
    ('&#xF1;','ñ'),
    ('&#xC0;','À'),
    ('&#xFFFC;',''),
    ('&#x203A;','›'),
    ('&#x2039;','‹'),
    ('&#x263A;',''),
    ('&#x270D;',''),
    ('&#x2601;',''),
    ('&#xA7;',''),
    ('&#xC7;','Ç'),
    ('&#x11F','ğ'),
    ('&#x2744;',''),
    ('&#x26C5;',''),
    ('&#x2600;',''),
    ('&#x26C8;',''),
    ('&#xA9;',''),
    ('&#xB9;','¹'),
    ('&#xCC;','Ì'),
    ('&#x25CE;',''),
    ('&#x23E9;',''),
    ('&#xBA;','º'),
    ('&#x301;','\''),
    ('&#xB7;',''),
    ('&#x75BC;','疼'),
    ('&#x3C0;','π'),
    ('&#x2018;','‘'),
    ('&#xFC;','ü'),
    ('&#x2B06;',''),
    ('&#x2714;',''),
    ('&#xD3;','Ó'),
    ('&#x2606;',''),
    ('&#xBE;','¾'),
    ('&#xE4;','ä'),
    ('&#xE2;','â'),
    ('&#xC2;',''),
    ('&#xE3;','ã'),
    ('&#xC1;','Á'),
    ('&#xCA;','Ê'),
    ('&#x26C4;',''),
    ('&#x3030;',''),
    ('&#xBF;','¿'),
    ('&#x2049;',''),
    ('&#x2753;',''),
    ('&#xA3;','£'),
    ('&#x103;','ă'),
    ('&#x219;','ș'),
    ('&#x1EC7;','ệ'),
    ('#x1ED9;','ộ'),
    ('&#x1EC1;','ề'),
    ('&#x1EA3;','ả'),
    ('&#x1ED1;','ố'),
    ('&#xE7;','ç'),
    ('&#xFF08;',''),
    ('&#xFF3E;',''),
    ('&#xFF3F;',''),
    ('&#xFF3E;',''),
    ('&#xFF09;',','),
    ('&#x2B07;',''),
    ('&#x15F;','ş'),
    ('&#x2134;',''),
    ('&#x212F;',''),
    ('&#xFF0C;',''),
    ('#x210A;',''),
    ('&#xFF0E;',''),
    ('&#xFF0D;',''),
    ('&#x212C;',''),
    ('&#x21DD;',''),
    ('&#x2112;',''),
    ('&#x2110;',''),
    ('&#x21DC;',''),
    ('&#x210B;',''),
    ('&#xFF01;',''),
    ('&#xFF01;',''),
    ('&#x2130;',''),
    ('&#x2133;',''),
    ('&#xFF1F;',''),
    ('&#x2012;','‒'),
    ('&#xDA;','Ú'),
    ('&#x159;','ř'),
    ('&#x161;','š'),
    ('&#x435;','е'),
    ('&#x13E;',''),
    ('&#x2705;',''),
    ('&#xFE0E;',''),
    ('&#xF8;','ø'),
    ('&#xAA;','ª'),
    ('&#x10D;','č'),
    ('&#x2667;',''),
    ('&#xF7;',''),
    ('&#x275D;',''),
    ('&#x275E;',''),
    ('&#x2741;',''),
    ('&#x394;',''),
    ('&#x259;',''),
    ('&#xE5;','å'),
    ('&#x26AA;',''),
    ('&#x26AB;',''),
    ('&#xD1;','Ñ'),
    ('&#x2698;',''),
    ('&#x25FB;',''),
    ('&#x25FB;'),
    ('&#x25FC;',''),
    ('&#x2192;',''),
    ('&#x3063;',''),
    ('&#x25D4;',''),
    ('&#x25E1;',''),
    ('&#x400;','Ѐ'),
    ('&#x25C4;',''),
    ('&#x25BA;',''),
    ('&#x266A;',''),
    ('&#x2015;',''),
    ('&#x2010;',''),
    ('&#x6F5;',''),
    ('&#x2500;',''),
    ('&#x2642;',''),
    ('&#xAD;',''),
    ('&#x2122;',''),
    ('&#x2605;',''),
    ('&#x20E3;',''),
    ('&#x2757;',''),
    ('&#x2005;',''),
    ('&#x27A1;',''),
    ('&#x269C;',''),
    ('&#xE6;','æ'),
    ('&#xF0;','ð'),
    ('&#x14D;','ō'),
    ('&#xA8;',''),
    ('&#xC3;','Ã'),
    ('&#xAC;',''),
    ('&#x29F;',''),
    ('&#x280;',''),
    ('&#x26A;',''),
    ('&#x274;',''),
    ('&#x299;',''),
    ('&#x29C;',''),
    ('&#x262;',''),
    ('&#xF5;','õ'),
    ('&#x3BA;','κ')
]

def sostRegex1(stringa):
  for el in listaRegex1:
    print(el)
    print(stringa)
    stringa = re.sub(el[0],el[1],stringa)
  return stringa

def sostRegex2(stringa):
  for el in listaRegex2:
    stringa = re.sub(el[0],el[1],stringa)
  return stringa

def regexDizionario(dizionarioCompleto):
  for el in dizionarioCompleto:
    dizionarioCompleto[el]["text"]=(sostRegex1(dizionarioCompleto[el]["text"]))
    dizionarioCompleto[el]["text"]=(sostRegex2(dizionarioCompleto[el]["text"]))

"""RIAPRO IL FILE JSON PRODOTTO"""

uploaded = files.upload()

"""CHIAMO LE FUNZIONI SOSTREGEX SUL JSON"""

dizionario = open("corpusStorie.json", "r")

dizionarioCompleto = json.loads(dizionario.read())

print(dizionarioCompleto["0"]["text"])

regexDizionario(dizionarioCompleto)

dizionarioPulito = open("corpusPulito.json", "w")
dizionarioPulito.write(json.dumps(dizionarioCompleto))

dizionarioPulito.close()

files.download('corpusPulito.json')