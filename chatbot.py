import wikipedia

def greet_user():
    print("-" * 50)
    print("Hello! I am your Wikipedia Chatbot.")
    print("I can fetch information from Wikipedia for you.")
    print("Just type a topic (e.g., Python, Elon Musk, AI).")
    print("Type 'exit' anytime to quit.")
    print("-" * 50, "\n")


def chatbot():
    greet_user()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nBot: It was nice talking to you. Have a great day! 👋")
            break

        if user_input == "":
            print("\nBot: Please enter a topic so I can help you 😊\n")
            continue

        try:
            print("\nBot: Let me look that up for you...\n")
            summary = wikipedia.summary(user_input, sentences=2)
            print("Bot:", summary, "\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print("Bot: That topic has multiple meanings.")
            print("Bot: Please be more specific. For example:")
            print(e.options[:5], "\n")

        except wikipedia.exceptions.PageError:
            print("Bot: Sorry, I couldn't find information on that topic.")
            print("Bot: Try searching for something else.\n")

        except Exception:
            print("Bot: Oops! Something went wrong on my side. Please try again.\n")


if __name__ == "__main__":
    chatbot()
