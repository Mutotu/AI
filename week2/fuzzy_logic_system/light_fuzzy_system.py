class LightFuzzySystem:
    def __init__(self):
        self.rules = {
            ("Low", "Partially Occupied"): "Brighten",
            ("Low", "Fully Occupied"): "Brighten",
            ("Medium", "Partially Occupied"): "Maintain",
            ("High", "Unoccupied"): "Dim",
            ("High", "Partially Occupied"): "Dim"
        }

        self.ambient_light_memberships = {
            "Low": lambda x: max(0, min(1, (30 - x) / 30)),
            "Medium": lambda x: max(0, min(1, (x - 30) / 40 if x > 30 else (70 - x) / 40)),
            "High": lambda x: max(0, min(1, (x - 70) / 30))
        }

        self.room_occupancy_memberships = {
            "Unoccupied": lambda x: max(0, min(1, (30 - x) / 30)),
            "Partially Occupied": lambda x: max(0, min(1, (x - 30) / 40 if x > 30 else (70 - x) / 40)),
            "Fully Occupied": lambda x: max(0, min(1, (x - 70) / 30))
        }

    def __fuzzify(self, light_value, occupancy_value):
        light_membership = {key: func(light_value) for key, func in self.ambient_light_memberships.items()}
        occupancy_membership = {key: func(occupancy_value) for key, func in self.room_occupancy_memberships.items()}

        return light_membership, occupancy_membership

    def __infer(self, light_membership, occupancy_membership):
        consequents = {}
        for (light_level, occupancy_level), action in self.rules.items():
            degree = min(light_membership[light_level], occupancy_membership[occupancy_level])
            if action not in consequents:
                consequents[action] = degree
            else:
                consequents[action] = max(consequents[action], degree)
        return consequents

    def __defuzzify(self, consequents):
        return max(consequents, key=consequents.get)

    def evaluate(self, light_value, occupancy_value):
        light_membership, occupancy_membership = self.__fuzzify(light_value, occupancy_value)
        consequents = self.__infer(light_membership, occupancy_membership)
        final_action = self.__defuzzify(consequents)

        return final_action


# Example usage
fuzzy_system = LightFuzzySystem()
action = fuzzy_system.evaluate(25, 50)
print(f"The recommended action is to: {action}")