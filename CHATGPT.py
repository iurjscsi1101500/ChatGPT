import openai

# Set up your OpenAI API credentials
openai.api_key = 'API_KEY'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    if response.choices:
        return response.choices[0].text.strip()
    else:
        return ''
# Start a conversation
user_input = ''
while user_input.lower() != 'bye':
    user_input = input('You: ')
    prompt = 'User: ' + user_input + '\nChatGPT:'
    response = chat_with_gpt(prompt)
    print('ChatGPT:', response)
