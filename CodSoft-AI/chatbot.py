def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if "hello" in user or "hi" in user:
            print("Chatbot: Hello! How can I help you?")
        elif "how are you" in user:
            print("Chatbot: I'm just a bot, but I'm doing great!")
        elif "your name" in user:
            print("Chatbot: I am CodSoft Bot.")
        elif "bye" in user:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()