
import os
import re
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file
load_dotenv(".env")

# Set OpenAI API key
openai.api_key = os.getenv("api_key")

# Delimiter used to separate sections in responses
DELIMITER = "****"

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    """
    Gets a completion from OpenAI's ChatCompletion API based on provided messages.
    
    Args:
        messages (list): List of message dictionaries.
        model (str): Model to use for completion.
        temperature (float): Degree of randomness of the model's output.
        max_tokens (int): Maximum number of tokens the model can output.
        
    Returns:
        str: The content of the completion response.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message["content"]

def separate_score_and_feedback(response):
    """
    Separates score and feedback from the response.
    
    Args:
        response (str): The raw response string.
        
    Returns:
        tuple: A tuple containing the score (int) and feedback (str).
    """
    response_chunks = response.split(DELIMITER)
    score_str = response_chunks[0]
    feedback_str = response_chunks[1]
    
    score = int(re.findall(r'\d+', score_str)[0])
    feedback = feedback_str.replace("Feedback:", "").strip()

    return score, feedback
