import os
import openai

key = "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"
key2 = "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"
openai.organization = "org-PC7IkgKZEFh6bCosQAGwPx02"
openai.api_key = key

# prints the models that openai has
# with open("models.json", "w") as file:
#     file.write(str(openai.Model.list()))

response = openai.Completion.create(model="text-davinci-003", prompt="how would i import a file in a separate directory in python", temperature=0, max_tokens=3000)

print(response)
