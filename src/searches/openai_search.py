import os
import openai


class OpenAI:
    def __init__(self):
        self.key = "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"
        openai.organization = "org-PC7IkgKZEFh6bCosQAGwPx02"
        openai.api_key = self.key

    def chat(self, prompt):
        return openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0, max_tokens=3000)
