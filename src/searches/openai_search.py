import json
import openai


class OpenAI:
    def __init__(self):
        self.key = "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"
        openai.organization = "org-PC7IkgKZEFh6bCosQAGwPx02"
        openai.api_key = self.key

    def chat(self, prompt):
        response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0, max_tokens=3000)


        data = json.loads(str(response))        # convert the response to a string and then load it as a json variable

        response = data["choices"][0]["text"]   # only get the response

        response = response.strip()             # strip all leading and trailing lines and spaces
        response = response.split("\n")         # split it to make a list

        return [elem.split('. ')[1] for elem in response]   # remove the leading numbers and return it



# if __name__ == "__main__":
#     x = OpenAI()
#     print(x.chat("what are some related topics to the sentence 'dogs':"))
