import os
import openai

#Load API keys saved in keys.txt
f = open("keys.txt", "r")
openai.api_key = f.readline().strip()

#DOCS: https://beta.openai.com/docs/api-reference?lang=python
#Engines:
#davinci
#curie
#babbage
#ada
response = openai.Completion.create(
    engine="davinci",
    temperature = 0.0,
    top_p = 1,
    prompt="This is a test",
    max_tokens=50,
    stop='\n'
    )
print(response)
print(response["choices"]["text"])