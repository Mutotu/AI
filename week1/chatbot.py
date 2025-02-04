# class RuleEngine:
#     def __init__(self):
#         self.rules = []
#
#     def add_rule(self, condition, response):
#         self.rules.append({"condition": condition, "response": response})
#
#     def apply_rules(self, text):
#         for rule in self.rules:
#             if rule["condition"] in text.lower():
#                 return f"Bot: {rule['response']}"
#         return "Bot: I don't understand."
#
#
# # Example usage
# rule_engine = RuleEngine()
#
# # Add rules
# rule_engine.add_rule("hello", "Hi there!")
# rule_engine.add_rule("goodbye", "Goodbye!")
#
# # Have conversation
# while True:
#     user_input = input("You: ")
#     response = rule_engine.apply_rules(user_input)
#     print(response)
#
#     if user_input.lower() == "goodbye":
#         break
#


class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if rule["condition"] in text.lower():
                return f"Recommended movie: {rule['response']}"
        return "No Movie found"


rule_engine = RuleEngine()

def add_rule():
    # Add rules
    rule_engine.add_rule("hello",
                         "Hi there!")
    rule_engine.add_rule("goodbye",
                         "Goodbye!")
    rule_engine.add_rule("how are you",
                         "I am just a bot, but thanks for asking!")
    rule_engine.add_rule("your name",
                         "I'm a bot, you can call me ChatBot!")
    rule_engine.add_rule("movie recommendations",
                         "Sure, I can help you with movie recommendations. What type of movie are you looking for?")
    rule_engine.add_rule("best movie",
                         "There are many great movies out there. Can you specify a genre or theme you prefer?")
    rule_engine.add_rule("action movie",
                         "If you like action movies, I recommend checking out 'The Dark Knight' or 'Mad Max: Fury Road.'")
    rule_engine.add_rule("comedy movie",
                         "For a good laugh, try 'The Grand Budapest Hotel' or 'Superbad.'")
    rule_engine.add_rule("drama movie",
                         "If you enjoy drama, 'The Shawshank Redemption' or 'The Godfather' are classics.")
    rule_engine.add_rule("science fiction movie",
                         "If you're into sci-fi, 'Blade Runner 2049' and 'Interstellar' are worth watching.")
    rule_engine.add_rule("romantic movie",
                         "For a romantic vibe, consider 'The Notebook' or 'Pride and Prejudice.'")
    rule_engine.add_rule("favorite movie",
                         "I am just a bot, but many people enjoy 'The Matrix' or 'Inception.'")
    rule_engine.add_rule("recommend a classic",
                         "A classic choice would be 'Casablanca' or 'Gone with the Wind.'")
    rule_engine.add_rule("animated movie",
                         "If you like animated films, 'Toy Story' or 'Finding Nemo' are delightful.")
    rule_engine.add_rule("horror movie",
                         "For a good scare, try 'The Conjuring' or 'Get Out.'")
    rule_engine.add_rule("musical movie",
                         "If you enjoy musicals, 'The Sound of Music' or 'La La Land' are fantastic.")
    rule_engine.add_rule("documentary",
                         "For a dose of reality, check out the documentary 'The Act of Killing.'")
    rule_engine.add_rule("thank you",
                         "You're welcome! If you have more questions or need recommendations, feel free to ask.")
    rule_engine.add_rule("exit",
                         "Goodbye! If you ever want to chat again, just type 'hello.'")

def new_rule():
    while True:
        print("Add a new rule: (E/x: Exit)")
        movie_type = input("Add type: ")
        if movie_type.lower() == "x":
            break
        movie = input("Add movie: ")
        rule_engine.add_rule(movie_type, movie)

def display_result():
    while True:
        print("What kind of movie? ")
        user_input = input("")
        response = rule_engine.apply_rules(user_input)
        print(response)

        if user_input.lower() == "x" or user_input == "":
            break

def main():
    add_movie = input("Add movie: (y/n)")
    if add_movie == "y":
        new_rule()

    add_rule()
    display_result()

if __name__ == "__main__":
    main()