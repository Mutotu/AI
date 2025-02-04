import re


# class RuleEngine:
#     def __init__(self):
#         self.rules = []
#
#     def add_rule(self, condition, response):
#         self.rules.append({"condition": condition, "response": response})
#
#     def apply_rules(self, text):
#         for rule in self.rules:
#             if re.search(rule["condition"], text, re.IGNORECASE):
#                 return f"Bot: {rule['response']}"
#         return "Bot: I don't understand."
#
# rule_engine = RuleEngine()
#
# rule_engine.add_rule(r'\bhello\b', 'Hi there!')
# rule_engine.add_rule(r'\bthank you\b', 'Hi there!')
# rule_engine.add_rule(r'\bgoodbye\b|\bbye\b', 'Goodbye!')
# rule_engine.add_rule(r'\bmy name is (.+?)\b', 'Nice to meet you, {0}!')
#
# res1 = rule_engine.apply_rules("hello")
# print(res1)
# res2 = rule_engine.apply_rules("My name is lol")
# print(res2)


class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, response):
        self.rules.append({"condition": condition, "response": response})

    def apply_rules(self, text):
        for rule in self.rules:
            if re.search(rule["condition"], text, re.IGNORECASE):
                return f"Bot: {rule['response']}"
        return "Bot: No entiendo"

rule_engine = RuleEngine()

def add_rule():
    # Add travel-related rules with different regex commands
    rule_engine.add_rule(r"\bhello\b",
                         "Hi there! What type of places do you like travelling to?")
    rule_engine.add_rule(r"\b(bye|goodbye)\b",
                         "Goodbye! Feel free to return for more travel suggestions.")
    rule_engine.add_rule(r"\bhow are you\b",
                         "I'm just a travel bot, but I'm here to help you plan your next adventure!")
    rule_engine.add_rule(r"\b(?:what|which)\s+places?\s+(should|can)\s+I\s+visit\b",
                         "I can suggest some amazing destinations for you!")
    rule_engine.add_rule(r"\b(?:recommend|suggest)\s+a\s+destination\b",
                         "Sure! What type of travel experience are you looking for?")
    rule_engine.add_rule(r"\b(?:thank you|thanks)\b",
                         "You're welcome! Enjoy your travels.")
    rule_engine.add_rule(r"\b(?:beach|mountain|city|countryside)\b",
                         "Excellent! Let me tailor my recommendations to your preferred travel style.")
    rule_engine.add_rule(r"\b(?:hotel|flight|activity)\s+recommendation\b",
                         "I enjoy discussing travel accommodations and activities!")

def apply_rules():
    while True:
        user_input = input("You: ")
        response = rule_engine.apply_rules(user_input)
        print(response)

        if "goodbye" in user_input:
            break

def main():
    add_rule()
    apply_rules()

if __name__ == "__main__":
    main()