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

for paragraph in dataset[:10]:
    formatted_paragraph = textwrap.fill(paragraph)
    print(f"{formatted_paragraph}\n")

def tokenizer (text : str):
    tokenized = text.split(' ')
    return tokenized

print(tokenizer(dataset[0]))

def ngram_generator(text: str, n: int):
    token = tokenizer(text)
    ngram = []
    for i in range(len(token)-n+1):
        
        ngram.append(tuple(token[i:i+n]))
    
    return ngram

print(ngram_generator(dataset[0],2))