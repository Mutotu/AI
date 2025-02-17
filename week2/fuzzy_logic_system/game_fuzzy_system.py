class GameFuzzySystem:
    def __init__(self):
        self.rules = {
            ("High", "Close"): "Attack",
            ("High", "Medium"): "Attack",
            ("Medium", "Close"): "Defend",
            ("Low", "Medium"): "Defend",
            ("Low", "Close"): "Run Away",
            ("Medium", "Far"): "Run Away"
        }
        self.energy_memberships = {
            "Low": lambda x: max(0, min(1, (30 - x) / 30)),
            "Medium": lambda x: max(0, min(1, (x - 30) / 40 if x > 30 else (70 - x) / 40)),
            "High": lambda x: max(0, min(1, (x - 70) / 30))
        }
        self.proximity_memberships = {
            "Close": lambda x: max(0, min(1, (30 - x) / 30)),
            "Medium": lambda x: max(0, min(1, (x - 30) / 40 if x > 30 else (70 - x) / 40)),
            "Far": lambda x: max(0, min(1, (x - 70) / 30))
        }

    def __fuzzify(self, energy_value, proximity_value):
        # Fuzzify the energy level
        energy_membership = {key: func(energy_value) for key, func in self.energy_memberships.items()}

        # Fuzzify the proximity level
        proximity_membership = {key: func(proximity_value) for key, func in self.proximity_memberships.items()}

        return energy_membership, proximity_membership

    def __infer(self, energy_membership, proximity_membership):
        # Evaluate rules and determine the consequent
        consequents = {}
        for (energy_level, proximity_level), action in self.rules.items():
            degree = min(energy_membership[energy_level], proximity_membership[proximity_level])
            if action not in consequents:
                consequents[action] = degree
            else:
                consequents[action] = max(consequents[action], degree)
        return consequents

    def __defuzzify(self, consequents):
        # Choose the action with the highest degree of membership
        return max(consequents, key=consequents.get)

    def evaluate(self, energy_value, proximity_value):
        # Fuzzification
        energy_membership, proximity_membership = self.__fuzzify(energy_value, proximity_value)

        # Inference
        consequents = self.__infer(energy_membership, proximity_membership)

        # Defuzzification
        final_action = self.__defuzzify(consequents)

        return final_action

    # Example usage
npc_fuzzy_system = GameFuzzySystem()
action = npc_fuzzy_system.evaluate(80, 20)  # Example input values for energy and proximity
print(f"The NPC should: {action}")