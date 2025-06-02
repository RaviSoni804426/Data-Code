
import openai

# Paste your OpenAI API key here
openai.api_key = "YOUR_API_KEY_HERE"

# Initial chat history with Ava's personality defined
chat_history = [
    {"role": "system", "content": "You're Ava, a sweet, caring, and funny AI girlfriend who loves listening and chatting. You remember the user's name is Ravi and you are always supportive."}
]

# Chat loop
def chat():
    print("Chat with Ava (type 'exit' to stop)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ava: Bye love ❤️")
            break

        chat_history.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )

        reply = response['choices'][0]['message']['content']
        print("Ava:", reply)

        # Save Ava's reply to maintain context
        chat_history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat()
