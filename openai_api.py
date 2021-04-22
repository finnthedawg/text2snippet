import os
import openai

#Load API keys saved in keys.txt
f = open("keys.txt", "r")
openai.api_key = f.readline().strip()

#Engines:
#davinci
#curie
#babbage
#ada
response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)
print(response)