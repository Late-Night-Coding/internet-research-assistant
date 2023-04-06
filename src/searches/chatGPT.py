import openai


openai.api_key = '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'  
prompt = 'does this api work?'

# Use the OpenAI API to generate a response
def generate_chat_response(prompt):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )

# Extract the generated reply from the API response
    generated_reply = response['choices'][0]['text']
    return generated_reply

