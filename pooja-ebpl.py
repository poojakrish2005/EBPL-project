import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses with pattern-matching rules
pairs = [
    [r"hello|hi|hey", ["Hello! How can I assist you today?"]],
    [r"my order status", ["Can you provide your order number?"]],
    [r"refund process", ["Refunds are processed within 5-7 business days."]],
    [r"(.*)help(.*)", ["I'm here to help! Please specify your query."]],
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Start chatbot interaction
print("Welcome to EBPL-DS Automated Assistance! Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot.respond(user_input)
    print(f"Bot: {response}")
