import openai
import os
import configparser
# Prompts Text
import prompts.story_writing
import prompts.readme_generation

# Set API key
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


def generateReadMe():
    prompt = ""
    with open("README.md", "r") as file:
        previous_readme = file.read()
        prompt =f"""
        {prompts.readme_generation.generation_instructions}

        Reference Text:```{prompts.readme_generation.project_notes}```

        Previously Generated README: <{previous_readme}>
        """
    response = get_completion(prompt)

    with open ("README.md", "w") as file:
        file.write(response)


def generateStory(reference_text, sample_story = ""):
    prompt = f"""
    {prompts.story_writing.task_intro}

    Before you write the biography, first check the reference material an make note of the following key details about the fallen. It is \
    okay if some details are missing.
    {prompts.story_writing.key_detail_list}

    {prompts.story_writing.story_structure}

    {prompts.story_writing.sbts_credit}

    At the end, include a formatted "Citations" section with any citations included in the reference text. All citations should be listed as \
    bullet point items. This section is in addition to the 3-5 paragraphs mentioned above.

    Again, only use facts and details found in this reference text: ```{reference_text}```
    """

    if sample_story != "":
        prompt = f"""
        {prompt}

        Base your writing style off of the sample biography, delimited by [], below:
        [{sample_story}]
        """

    response = get_completion(prompt)
    with open("output.txt", "w") as file:
        file.write(response)
        


def main():
    print("Pinging OpenAI...")
    ping_prompt = "Hi OpenAI! Can you hear me?"
    response = get_completion(ping_prompt)
    print("\n{}\n{}\n".format(ping_prompt, response))


    print("Checking README for needed updates...")
    generateReadMe()
    print("README updated.\n")

    print("Preparing to write story...")
    print("Reading research as reference...")
    file = open("research.txt", "r")
    reference_text = file.read()
    file.close()
    print("Sending request to AI...")
    generateStory(reference_text)
    print("Story is finished. See output.txt.")

main()