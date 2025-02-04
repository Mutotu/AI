class TaxRules:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rules(self, income):
        for condition, result in self.rules:
            if condition(income):
                return result
        return "default"

# Initialize rule engine
engine = TaxRules()
# Test cases
test_incomes = [12567, 12571, 50271, 125141]
def calc_tax():
    # Add tax rules
    engine.add_rule(lambda x: x <= 12570, "Personal Allowance: 0%")
    engine.add_rule(lambda x: 12571 <= x <= 50270, "Basic Rate: 20%")
    engine.add_rule(lambda x: 50271 <= x <= 125140, "Higher Rate: 40%")
    engine.add_rule(lambda x: x > 125140, "Additional Rate: 45%")

def display_result():
    for income in test_incomes:
        result = engine.apply_rules(income)
        print(f"For an income of £{income}, the tax band is: {result}")

def main():
    calc_tax()
    display_result()

if __name__ == '__main__':
    main()