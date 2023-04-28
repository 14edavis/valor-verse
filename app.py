import openai
import os
import configparser

config = configparser.ConfigParser()
config.readfp(open(r'secret.config'))
openai.api_key=config.get('API', 'api_key')

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    repsonse = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature #ie degree of randomness, 0-1
    )
    return repsonse.choices[0].message["content"]

print(get_completion("Hello AI!")) #Will get a response from openai

