class RuleBasedSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "Default"

engine = RuleBasedSystem()
engine.add_rule(lambda x: x < 12570, "0%")
engine.add_rule(lambda x: 12571 <= x <= 50270, "20%")
engine.add_rule(lambda x: 50271 <= x <= 125140, "40%")
engine.add_rule(lambda x: x > 125140, "45%")

result1 = engine.apply_rules(12567)
result2 = engine.apply_rules(12571)
result3 = engine.apply_rules(50271)
result4 = engine.apply_rules(125141)
print(f"For an income of ${12567}, the tax band is: {result1}")
print(f"For an income of ${12571}, the tax band is: {result2}")
print(f"For an income of ${50271}, the tax band is: {result3}")
print(f"For an income of ${125141}, the tax band is: {result4}")