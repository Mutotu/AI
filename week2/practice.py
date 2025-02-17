class VirtualPetFuzzySystem:
    def __init__(self):
        # Define membership functions for energy levels
        self.energy_memberships = {
            "Low": lambda x: max(0, min(1, (50 - x) / 50)),
            "Medium": lambda x: max(0, min(1, (x - 30) / 40 if x > 30 else (70 - x) / 40)),
            "High": lambda x: max(0, min(1, (x - 70) / 30))
        }

        # Define membership functions for hunger levels
        self.hunger_memberships = {
            "Not Hungry": lambda x: max(0, min(1, (30 - x) / 30)),
            "Hungry": lambda x: max(0, min(1, (x - 30) / 40 if x > 30 else (70 - x) / 40)),
            "Very Hungry": lambda x: max(0, min(1, (x - 70) / 30))
        }

        # Define fuzzy rules
        self.rules = {
            ("High", "Not Hungry"): "Play",
            ("Medium", "Hungry"): "Eat",
            ("Low", "Very Hungry"): "Sleep",
            ("Low", "Hungry"): "Sleep",
            ("Medium", "Very Hungry"): "Sleep"
        }

    def __fuzzify(self, energy_value, hunger_value):
        energy_memberships = {key: func(energy_value) for key, func in self.energy_memberships.items()}
        hunger_memberships = {key: func(hunger_value) for key, func in self.hunger_memberships.items()}
        return energy_memberships, hunger_memberships

    def __infer(self, energy_membership, hunger_membership):
        consequents = {}
        for (energy_level, hunger_level), action in self.rules.items():
            degree = min(energy_membership[energy_level], hunger_membership[hunger_level])
            if action not in consequents:
                consequents[action] = degree
            else:
                consequents[action] = max(consequents[action], degree)
        return consequents

    def __defuzzify(self, consequents):
        return max(consequents, key=consequents.get)

    def evaluate(self, energy_value, hunger_value):
        energy_membership, hunger_membership = self.__fuzzify(energy_value, hunger_value)
        consequents = self.__infer(energy_membership, hunger_membership)
        final_action = self.__defuzzify(consequents)
        return final_action

# Example usage
pet_fuzzy_system = VirtualPetFuzzySystem()
action = pet_fuzzy_system.evaluate(60, 80)  # Example input values for energy and hunger
print(f"The pet should: {action}")