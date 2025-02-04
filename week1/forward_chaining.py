class MedicalDiagnosisExpertSystem:
    def __init__(self):
        self.symptoms = {}
        self.rules = []

    def add_symptom(self, name, present):
        self.symptoms[name] = present

    def add_rule(self, conditions, diagnosis):
        self.rules.append({"conditions": conditions, "diagnosis": diagnosis})

    def diagnose(self):
        for rule in self.rules:
            conditions_met = all(self.symptoms[condition] for condition in rule["conditions"])

            if conditions_met:
                return f"The patient is diagnosed with: {rule['diagnosis']}"

        return "No specific diagnosis based on the observed symptoms."

# Example Usage:
medical_system = MedicalDiagnosisExpertSystem()
medical_system.add_symptom("fever", True)
medical_system.add_symptom("cough", True)
medical_system.add_symptom("headache", True)

medical_system.add_rule(["fever", "cough", "headache"], "Common Cold")
medical_system.add_rule(["fever", "cough"], "Flu")
medical_system.add_rule(["headache"], "Migraine")

# result = medical_system.diagnose()
# print(result)

class TechnicalSupportSystem:
    def __init__(self):
        self.symptoms = {}
        self.rules = []

    def add_symptom(self, name, problem):
        self.symptoms[name] = problem

    def add_rule(self, condition, diagnosis):
        self.rules.append({"conditions": condition, "diagnosis": diagnosis})

    def diagnose(self):
        for rule in self.rules:
            conditions_met = all(self.symptoms[condition] for condition in rule["conditions"])

            if conditions_met:
                return f"The tech is diagnosed with: {rule['diagnosis']}"

        return "No specific diagnosis based on the observed symptoms."

technical_support = TechnicalSupportSystem()
technical_support.add_symptom("slow", True)
technical_support.add_symptom("lagging", True)
technical_support.add_symptom("power off", True)

# technical_support.add_rule(["slow", "lagging", "power off"], "Computer virus")
# technical_support.add_rule(["slow", "lagging"], "Software update needed")
technical_support.add_rule(["slow"], "Needs cleaning")

result = technical_support.diagnose()
print(result)