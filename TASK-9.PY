
# First, make sure to install the OpenAI library (run this in terminal, not inside Python)
# pip install --upgrade openai

from openai import OpenAI

# Initialize client (replace with your API key)
client = OpenAI(api_key="sk-your_api_key_here")

# Create the chat completion request
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me 3 ideas that I could build using OpenAI APIs"}
    ]
)

# Print the response safely
print(completion.choices[0].message.content)

