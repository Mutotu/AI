class SmartThermostatFuzzySystem:
    def __init__(self):
        # Define membership functions for temperature levels
        self.temperature_memberships = {
            "Low": lambda x: max(0, min(1, (60 - x) / 20)),
            "Medium": lambda x: max(0, min(1, (x - 50) / 20 if x > 50 else (70 - x) / 20)),
            "High": lambda x: max(0, min(1, (x - 70) / 20))
        }

        # Define membership functions for humidity levels
        self.humidity_memberships = {
            "Low": lambda x: max(0, min(1, (40 - x) / 40)),
            "Medium": lambda x: max(0, min(1, (x - 30) / 40 if x > 30 else (70 - x) / 40)),
            "High": lambda x: max(0, min(1, (x - 70) / 30))
        }

        # Define fuzzy rules
        self.rules = {
            ("Low", "Medium"): "Heat",
            ("Low", "High"): "Heat",
            ("High", "Medium"): "Cool",
            ("High", "High"): "Cool",
            ("Medium", "Low"): "Do Nothing"
        }

    def __fuzzify(self, temperature_value, humidity_value):
        temperature_memberships = {key: func(temperature_value) for key, func in self.temperature_memberships.items()}
        humidity_memberships = {key: func(humidity_value) for key, func in self.humidity_memberships.items()}
        return temperature_memberships, humidity_memberships

    def __infer(self, temperature_membership, humidity_membership):
        consequents = {}
        for (temp_level, humid_level), action in self.rules.items():
            degree = min(temperature_membership[temp_level], humidity_membership[humid_level])
            if action not in consequents:
                consequents[action] = degree
            else:
                consequents[action] = max(consequents[action], degree)
        return consequents

    def __defuzzify(self, consequents):
        return max(consequents, key=consequents.get)

    def evaluate(self, temperature_value, humidity_value):
        temperature_membership, humidity_membership = self.__fuzzify(temperature_value, humidity_value)
        consequents = self.__infer(temperature_membership, humidity_membership)
        final_action = self.__defuzzify(consequents)
        return final_action

# Example usage
thermostat_fuzzy_system = SmartThermostatFuzzySystem()
action = thermostat_fuzzy_system.evaluate(65, 80)  # Example input values for temperature and humidity
print(f"The thermostat should: {action}")
