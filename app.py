import os
import openai

from dotenv import load_dotenv
load_dotenv()
# Set up your OpenAI API credentials
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define a function to interact with the chatbot
def chat_with_bot(message):
    # Define the initial user message
    user_message = message

    # Initialize the chat history
    chat_history = user_message

    while True:
        # Call the OpenAI ChatCompletion API
        response = openai.Completion.create(
            engine='davinci',
            prompt=chat_history,
            max_tokens=100,
            temperature=0.6,
            n=1,
            stop=None,
            temperature=0.6
        )

        # Get the model's reply from the response
        model_reply = response.choices[0].text.strip()

        # Append the model's reply to the chat history
        chat_history += model_reply

        # Print the model's reply
        print('Bot:', model_reply)

        # Get the user's next message
        user_message = input('You: ')

        # Append the user's message to the chat history
        chat_history += '\nUser: ' + user_message

        # Check if the user wants to exit
        if user_message.lower() == 'exit':
            break

# Start the chatbot
print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
user_input = input('You: ')
chat_with_bot(user_input)