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