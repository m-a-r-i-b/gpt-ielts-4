import os
import re
from dotenv import load_dotenv
load_dotenv(".env")
import openai

openai.api_key =  os.environ.get("api_key")

delimiter = "####"

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
        max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
    )
    return response.choices[0].message["content"]


def separate_score_and_feedback(response):
    response_chunnks = response.split(delimiter)

    first_chunk = response_chunnks[0]
    score = int(re.findall(r'\d+', first_chunk)[0])

    second_chunk = response_chunnks[1]
    feedback = second_chunk.replace("Feedback:","") 

    return score, feedback