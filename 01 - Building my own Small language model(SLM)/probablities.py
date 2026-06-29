# Packages used.
import random # For sampling from probability distributions.
from collections import Counter, defaultdict # For counting n-grams.

import textwrap # For automatically adding linebreaks to long texts.
import pandas as pd # For constructing and visualizing tables.

# Custom functions for providing feedback on your solutions.
#from ai_foundations.feedback.course_1 import ngrams


africa_galore = pd.read_json(
    "https://storage.googleapis.com/dm-educational/assets/ai_foundations/africa_galore.json"
)
dataset = africa_galore["description"]
print(f"The dataset consists of {dataset.shape[0]} paragraphs.")

""" for paragraph in dataset[:10]:
    formatted_paragraph = textwrap.fill(paragraph)
    print(f"{formatted_paragraph}\n") """

def tokenizer (text : str):
    tokenized = text.split(' ')
    return tokenized

print(tokenizer(dataset[0]))

all_unigrams = []
all_bigrams = []
all_trigrams = []

def ngram_generator(text: str, n: int):
    token = tokenizer(text)
    ngram = []
    for i in range(len(token)-n+1):
        
        ngram.append(tuple(token[i:i+n]))
    
    return ngram
for paragraph in dataset:
    all_unigrams.extend(ngram_generator(paragraph, 1))
    all_bigrams.extend(ngram_generator(paragraph,2))
    all_trigrams.extend(ngram_generator(paragraph, 3))

print(all_unigrams[:4])
print(all_bigrams[:4])
print(all_trigrams[:4])

bigram_counter = Counter(all_bigrams)
trigram_counter = Counter(all_trigrams)
for bigram, count in bigram_counter.most_common(10):
    print(f"  ({bigram}, {count})")

print("\n\nMost common trigrams:")
for trigram, count in trigram_counter.most_common(10):
    print(f"  ({trigram}, {count})")