import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
import requests
from openai import OpenAI
from config import api_key

client = OpenAI(api_key=api_key)

def create_embedding(text_list):
    r= requests.post("http://localhost:11434/api/embed", json={   # ollama is running on localhost:11434
        "model": "bge-m3",
      # "prompt": "Sakshi is a good girl"
        "input": text_list
    })
    
    embedding = r.json()["embeddings"] 
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        #"model": " deepseek-r1:latest",
        "model" : "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    response = r.json()
    print(response)
    return response

def inference_openai(prompt):
    print("Thinking....") 
    response = client.responses.create(
        model="gpt-5.5",
        input = prompt
    )
    return response.output_text  

df = joblib.load('embeddings.joblib')

incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0]
# print(question_embedding)  
# a = create_embedding("Cat sat on the mat")
# print(a)

# Find similarities of question_embedding with other embeddings
# print(np.vstack(df['embedding'].values))
print(np.vstack(df['embedding']).shape)
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
# print(similarities)
top_result = 5

# print(similarities.argsort()) gives us the indices of the similarities array in sorted order. The last index will be the index of the highest similarity, which is the most relevant chunk for the incoming query. The second last index will be the index of the second highest similarity, and so on.

max_indx = similarities.argsort()[::-1][0:top_result]
# gives us the indices of the top 3 most similar chunks for the incoming query. [::-1] is used to reverse the order of the similarities array, so that we get the indices of the highest similarities first. [0:3] is used to get only the top 3 indices.

# print(max_indx)
new_df = df.loc[max_indx]
# print(new_df[["title", "number", "text"]])

prompt = f''' I am teaching web development course. Here are video chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

--------------

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}

----------------

"{incoming_query}"
User asked this question related to the video chunks, you have to answer in a human way  (Don't mention the above format, its just for you) where and how much content is taught (in which video and timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer question related to the course.

'''


with open("prompt.txt", "w") as f:
    f.write(prompt)

# response = inference(prompt)["response"]
# print(response)

response = inference_openai(prompt)
print(response)

with open("response.txt", "w") as f:
    f.write(response)
# for index, item in new_df.iterrows():
#     print(index, item['title'], item['number'], item['text'], item['start'], item['end'])