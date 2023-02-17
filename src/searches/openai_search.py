import os
import openai

key = "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"
openai.organization = "org-PC7IkgKZEFh6bCosQAGwPx02"
openai.api_key = key

# prints the models that openai has
# with open("models.json", "w") as file:
#     file.write(str(openai.Model.list()))

response = openai.Completion.create(model="text-davinci-003", prompt="how would i import a file in a separate directory in python", temperature=0, max_tokens=3000)

print(response)
