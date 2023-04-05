import json
import openai


class OpenAI:
    def __init__(self):
        self.key = "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"
        openai.organization = "org-nVcfRvKHlZzuZmUk3kTRiXMP"
        openai.api_key = self.key

    def categorize(self, prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="what are some categories for the following phrase: " + prompt,
            temperature=0.1,
            max_tokens=1000,
            top_p=1,
            best_of=3,
            frequency_penalty=0,
            presence_penalty=1.1
        )

        return self.__format__(response)

    def summarize(self, prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="summarize this: " + prompt,
            temperature=0.1,
            max_tokens=1000,
            top_p=1,
            best_of=3,
            frequency_penalty=0,
            presence_penalty=1.1
        )

        return self.__format__(response)


    def __format__(self, response):
        data = json.loads(str(response))  # convert the response to a string and then load it as a json variable

        response = data["choices"][0]["text"]  # only get the response

        response = response.strip()  # strip all leading and trailing lines and spaces
        response = response.split("\n")  # split it to make a list

        if len(response) == 1:
            return response[0]  # return if the response is not a list

        return [elem.split('.q ')[1] for elem in response]  # remove the leading numbers and return it

# if __name__ == "__main__":
#     x = OpenAI()
#     print(x.chat("what are some related topics to the sentence 'dogs':"))