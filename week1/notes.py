# Basic Rule-Based System:
#
# A simple system using basic if-else conditions to classify input.

def basic_rule_based_system(input_value):
    if input_value < 10:
        return "Low"
    else:
        return "High"

result = basic_rule_based_system(7)
print(result)  # Output: Low
#
# Rule-Based System with Multiple Conditions:
#
# This version incorporates several conditions using if-elif-else to provide more detailed classifications.

def multiple_condition_rule_system(input_value):
    if input_value < 5:
        return "Very Low"
    elif 5 <= input_value < 10:
        return "Low"
    elif 10 <= input_value < 20:
        return "Medium"
    else:
        return "High"

result = multiple_condition_rule_system(15)
print(result)  # Output: Medium

# Rule-Based System with Functions as Rules:
#
# Here, individual rules are defined as functions, and the system applies them dynamically.

def rule_1(input_value):
    return input_value < 5

def rule_2(input_value):
    return 5 <= input_value < 10

def rule_3(input_value):
    return 10 <= input_value < 20

def rule_based_system(input_value):
    if rule_1(input_value):
        return "Very Low"
    elif rule_2(input_value):
        return "Low"
    elif rule_3(input_value):
        return "Medium"
    else:
        return "High"

result = rule_based_system(15)
print(result)  # Output: Medium
#
# Rule-Based System with a Rule Engine:
#
# This version introduces a RuleEngine class, allowing for better organisation and flexibility by dynamically adding and applying rules.

class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, input_value):
        for condition, result in self.rules:
            if condition(input_value):
                return result
        return "Default"

engine = RuleEngine()
engine.add_rule(lambda x: x < 5, "Very Low")
engine.add_rule(lambda x: 5 <= x < 10, "Low")
engine.add_rule(lambda x: 10 <= x < 20, "Medium")

result = engine.apply_rules(15)
print(result)  # Output: Medium