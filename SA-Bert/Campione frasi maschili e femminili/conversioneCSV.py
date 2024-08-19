import json
import pandas as pd

# Load female sentences from file
fileFem = open("Risultati/SABert/FemPol.json", "r")
frasiFem = json.load(fileFem)

# Load male sentences from file
fileMale = open("Risultati/SABert/MascPol.json", "r")
frasiMale = json.load(fileMale)


# Convert results to DataFrames
df_male_sentiments = pd.DataFrame.from_dict(frasiMale, orient="index", columns=['Negative', 'Neutral','Positive'])
df_female_sentiments = pd.DataFrame.from_dict(frasiFem, orient="index", columns=['Negative', 'Neutral','Positive'])


# df_corpus_sentiments = pd.DataFrame(corpus_sentiment_results, columns=['Original Text', 'Translated Text', 'Polarity', 'Sentiment'])

# Save results to CSV files
df_male_sentiments.to_csv('Risultati/SABert/sentiment_maschi_vader.csv', index=True, encoding='utf-8')
df_female_sentiments.to_csv('Risultati/SABert/sentiment_femmine_vader.csv', index=True, encoding='utf-8')

# df_corpus_sentiments.to_csv('sentiment_corpus_vader.csv', index=False, encoding='utf-8')