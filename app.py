import os
import openai

from dotenv import load_dotenv
load_dotenv()
# Set up your OpenAI API credentials
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define a function to interact with the chatbot


class ChatBot:
    def __init__(self):
        self.chat_messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    def ask(self, message):
        # Define the initial user message
        user_message = message
        chat_messages = self.chat_messages
        # Initialize the chat history
        chat_history = user_message
        while True:
            chat_messages.append({"role": "user", "content": user_message})
            # print(chat_messages)
            # Call the OpenAI ChatCompletion API
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=chat_messages,
                    max_tokens=100,
                    temperature=0.6
                )
            except Exception as e:
                print("Chat Error: ", str(e))
                return

            # Get the model's reply from the response
            model_reply = response.choices[0].message
            chat_messages.append(model_reply)
            # Append the model's reply to the chat history
            chat_history += model_reply.content

            # Print the model's reply
            print('Bot:', model_reply.content)

            # Get the user's next message
            user_message = input('You: ')

            # Append the user's message to the chat history
            chat_history += '\nUser: ' + user_message
            self.chat_messages = chat_messages
            # Check if the user wants to exit
            if user_message.lower() == 'exit':
                break


if __name__ == '__main__':
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    user_input = input('You: ')
    chat = ChatBot()
    chat.ask(user_input)
