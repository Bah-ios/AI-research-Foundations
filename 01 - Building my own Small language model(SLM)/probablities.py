# Packages used.
import random # For sampling from probability distributions.
from collections import Counter, defaultdict # For counting n-grams.

import textwrap # For automatically adding linebreaks to long texts.
import pandas as pd # For constructing and visualizing tables.

#Custom functions for providing feedback on your solutions.
# from ai_foundations.feedback.course_1 import ngrams
from IPython.display import display

africa_galore = pd.read_json(
    "https://storage.googleapis.com/dm-educational/assets/ai_foundations/africa_galore.json"
)
dataset = africa_galore["description"]
# print(type(dataset))
# print(f"The dataset consists of {dataset.shape[0]} paragraphs.")

# for paragraph in dataset[:10]:
#     formatted_paragraph = textwrap.fill(paragraph)
#     print(f"{formatted_paragraph}\n") 

def tokenizer (text : str):
    tokenized = text.split(' ')
    return tokenized

# print(tokenizer(dataset[0]))

all_unigrams = []
all_bigrams = []
all_trigrams = []

state = "table mountain is beautiful"
def ngram_generator(text, n: int):
    token = tokenizer(text)
    ngram = []
    for i in range(len(token)-n+1):
        
        ngram.append(tuple(token[i:i+n]))
    
    return ngram

for paragraph in dataset:
    #all_unigrams.extend(ngram_generator(paragraph, 1))
    all_bigrams.extend(ngram_generator(paragraph,2))
    all_trigrams.extend(ngram_generator(paragraph, 3))

# print(all_unigrams[:10])
print(all_bigrams[:10])
print(all_trigrams[:10])

bigram_counter = Counter(all_bigrams[:10])
trigram_counter = Counter(all_trigrams[:10])
print(bigram_counter)
print(trigram_counter)
print("\n\n Most common bigrams:")
for bigram, count in bigram_counter.most_common(10):
    print(f"({bigram}, {count})\n")

print("\n\nMost common trigrams:")
for trigram, count in trigram_counter.most_common(10):
    print(f"({trigram}, {count})\n") 
text = "tabel mountain is beautiful"
def ngram_counter(dataset , n : int) -> dict[str, Counter]:
    dict = defaultdict(Counter)
    for paragraph in dataset:
        for ngram in ngram_generator(paragraph, n):
                context = " ".join(ngram[:-1])
                value = ngram[-1]
                dict[context][value] += 1

    
    return dict       
 


### printing the data in tables

#print(bigram_counts)
# bigram_counts_matrix = {
#     context: dict(counts) for context, counts in bigram_counts.items()
# }
# bigram_data_frame = pd.DataFrame.from_dict(
#     bigram_counts_matrix, orient="index").fillna(0)

# display(bigram_data_frame)

# zero_count = (bigram_data_frame == 0).sum().sum()
# print(
#     f"Number of bigrams with a count of 0: {zero_count:,}"
#     f" ({zero_count/bigram_data_frame.size * 100:.2f}%)")



# # Use the pandas library to display the counts in a table.
# trigram_counts_matrix = {
#     context: dict(counts) for context, counts in trigram_counts.items()
# }
# trigram_data_frame = pd.DataFrame.from_dict(
#     trigram_counts_matrix, orient="index").fillna(0)

# display(trigram_data_frame)

# zero_count = (trigram_data_frame == 0).sum().sum()
# print(
#     f"Number of trigrams with a count of 0: {zero_count:,}"
#     f" ({zero_count/trigram_data_frame.size * 100:.2f}%)")

context = "a staple" 

bigram_counts = ngram_counter(dataset, 2)

print(
    'Bigram count of "a staple" computed directly from the Bigrams: ',
    bigram_counts["a"]["staple"],
)

trigram_counts = ngram_counter(dataset, 3)
print(f"\n {trigram_counts[context]} \n")
next_token_total_appearance = sum(trigram_counts[context].values())

print(
    'Bigram count of "a staple" computed indirectly( By sum()) from trigram counts: ',
    next_token_total_appearance,
)
