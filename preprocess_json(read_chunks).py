import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# embedding is a numerical representation of text that captures its semantic meaning. It is used in natural language processing tasks to convert text into a format that can be easily processed by machine learning models. The embedding is typically a high-dimensional vector that represents the meaning of the text in a way that allows for comparisons and calculations to be performed on it.

# bge-m3 is a specific embedding model that is designed to capture the meaning of text in a way that is useful for a variety of natural language processing tasks. It is trained on a large dataset of text and is able to generate high-quality embeddings that can be used for tasks such as text classification, sentiment analysis, and more.


def create_embedding(text_list):
    r= requests.post("http://localhost:11434/api/embed", json={   # ollama is running on localhost:11434
        "model": "bge-m3",
      # "prompt": "Sakshi is a good girl"
        "input": text_list
    })
    
    embedding = r.json()['embeddings']
    return embedding

jsons = os.listdir("jsons")  # List all JSON files in the "jsons" directory 
my_dicts = []
chunk_id = 0


# If cosine similarities of two vectors are close to 1(means they are parrellel, cos0=1), then the two vectors are similar in meaning. If the cosine similarity is close to 0, then the two vectors are virtical and have no similarity in meaning. If the cosine similarity is close to -1, then the two vectors are opposite in meaning.


# create embeddings for the "text" which are in the chunks, and store the results in a list of dictionaries.

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating Embeddings for {json_file}...")    
    embeddings = create_embedding([c['text'] for c in content['chunks']])
    
    for i, chunk in enumerate(content['chunks']):  # enumerate() gives us the index and the value of the chunk in the content['chunks'] list
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)
        #print(chunk)
    
        
# print(my_dicts)

df = pd.DataFrame.from_records(my_dicts)
# print(df)
# Save this dataframe
joblib.dump(df, 'embeddings.joblib')
