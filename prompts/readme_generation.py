# Change notes about the project here. The AI will take care of formatting and other niceties when it generates the README.
project_notes = f"""
Name: ValorVerse

About:
The name came from a list of possible project names that were brainstormed by ChatGPT. 
This README is also generated by OpenAI. You can see the prompts used to generate it in app.py.
Still in intial development

Goal: Assist story writers for the volunteer project "Stories Behind the Stars" in writing accurate and compelling stories about \
WWII fallen based off of provided research.

Dependencies: python 3.10, openai (these should be formatted as a list)

How It Works:
Each user needs to get their own API key and save it in secret.config. For sample see sample_secret.config
Create 'research.txt'. Copy and paste relevant research into it.
The story will be saved to 'output.txt'. If you like a story, save it elsewhere so it doesn't get overwritten.

"""


generation_instructions =f"""
Write a software project README.md file explaining the project in the reference text delimited by ```. Make sure to include all details \
given in the provided text. It is important that all details are included.

This new README should match the format of the sample text delimited by <>. Use the same headers, when possible. All deviations \
from the sample text should be minimal.

First, generate a README without looking at the sample text. Next, compare the information with the sample text. Use this to create your final \
README. If the sample text contains extra information, remove it. If the sample text is missing information, add it.

Welcome the reader. Use a friendly tone. You are writing to both software engineers and potential story writers.

At the end, note that this README was generated by OpenAI.

Provide output in markdown format. Include headers and subheaders, as needed.
"""