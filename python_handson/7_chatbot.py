print("Hello! I am School Bot.")

while True:
    user = input("You: ")
    
    if user == "hello":
        print("Bot: Hi there!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")