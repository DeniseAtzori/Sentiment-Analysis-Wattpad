import json
import pandas as pd

# Load sentences from file
file = open("frasiStoria1Pol.json", "r")
frasi = json.load(file)


# Convert results to DataFrames
df_sentiments = pd.DataFrame.from_dict(frasi, orient="index", columns=['Negative', 'Neutral','Positive'])

# df_corpus_sentiments = pd.DataFrame(corpus_sentiment_results, columns=['Original Text', 'Translated Text', 'Polarity', 'Sentiment'])

# Save results to CSV files
df_sentiments.to_csv('sentiment_storia1_bert.csv', index=True, encoding='utf-8')
# df_corpus_sentiments.to_csv('sentiment_corpus_vader.csv', index=False, encoding='utf-8')