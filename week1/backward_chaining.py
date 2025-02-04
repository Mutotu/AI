class DiscountEligibilitySystem:
    def __init__(self):
        self.purchase_history = {}
        self.rules = []

    def add_purchase(self, item, price):
        if item in self.purchase_history:
            self.purchase_history[item] += price
        else:
            self.purchase_history[item] = price

    def add_rule(self, goal, condition_amount):
        self.rules.append({"goal": goal, "conditions": condition_amount})

    def check_discount_eligibility(self, goal):
        total_purchase_amount = sum(self.purchase_history.values())

        if total_purchase_amount == 0:
            return "Customer has no purchase history for evaluation."

        for rule in self.rules:
            if rule["goal"] == goal and total_purchase_amount >= rule["conditions"]:
                return f"The customer is eligible for a {goal} discount. Conditions met: {rule['conditions']}"

        return f"The customer is not eligible for a {goal} discount based on their purchase history."

# Example Usage:
# discount_system = DiscountEligibilitySystem()
#
# # Add purchase history
# discount_system.add_purchase("Electronics", 800)
# discount_system.add_purchase("Clothing", 150)
# discount_system.add_purchase("Books", 50)
#
# # Define rules for discount eligibility based on overall purchase amount
# discount_system.add_rule("10% Off Electronics", 500)
# discount_system.add_rule("20% Off Clothing", 100)
#
# # Check discount eligibility
# result = discount_system.check_discount_eligibility("10% Off Electronics")
# print(result)

class LoanEligibilitySystem:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, fact_type, value):
        self.facts[fact_type] = value

    def add_rule(self, goal, conditions):
        self.rules.append({"goal": goal, "conditions": conditions})

    def check_loan_eligibility(self, goal):
        if not all(self.facts.values()):
            return "Incomplete financial information for evaluation."

        for rule in self.rules:
            if rule["goal"] == goal:
                conditions_met = all(self.facts[condition] >= threshold for condition, threshold in rule["conditions"].items())

                if conditions_met:
                    return f"The individual is eligible for a {goal} loan."

        return f"The individual is not eligible for a {goal} loan based on their financial situation."

# Example Usage:
loan_system = LoanEligibilitySystem()

# Add facts for individual's income and credit score
loan_system.add_fact("income", 60000)
loan_system.add_fact("credit_score", 700)

# Define rules for loan eligibility
loan_system.add_rule("Mortgage", {"income": 50000, "credit_score": 650})
loan_system.add_rule("Personal", {"income": 30000, "credit_score": 600})

# Check mortgage loan eligibility
print(loan_system.check_loan_eligibility("Personal"))