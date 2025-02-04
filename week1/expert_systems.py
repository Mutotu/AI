class WeatherExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, conditions, result):
        self.rules.append((conditions, result))

    def infer(self):
        for conditions, result in self.rules:
            if all(condition in self.facts for condition in conditions):
                return result
        return "Default"

expert_system = WeatherExpertSystem()

n_facts = int(input("How many facts would you like to enter?: "))

for count in range(n_facts):
    user_fact = input("Enter fact: ")
    expert_system.add_fact(user_fact)

expert_system.add_rule(["high temperature", "low humidity"], "Comfortable")
expert_system.add_rule(["high temperature", "high wind"], "Uncomfortable")

print(expert_system.infer())  # Output: Comfortable