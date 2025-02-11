import matplotlib.pyplot as plt
from typing import Dict


class TemperatureFuzzySystem:
    def __init__(self):
        self.__rules = {
            ("very cold", "cold"): "heat",
            "warm": "no change",
            ("very hot", "hot"): "cool",
        }
        self.__memberships = {
            "very cold": lambda temp: max(0, min((10 - temp) / 10, 1)),
            "cold": lambda temp: max(0, min((temp - 0) / 10, (20 - temp) / 10, 1)),
            "warm": lambda temp: max(0, min((temp - 10) / 10, (30 - temp) / 10, 1)),
            "hot": lambda temp: max(0, min((temp - 20) / 10, (40 - temp) / 10, 1)),
            "very hot": lambda temp: max(0, min((temp - 30) / 10, 1))
        }

        # Crisp values for defuzzification
        self.__crisp_values = {"cool": -1, "no change": 0, "heat": 1}
        self.__weights = {"cool": 0.5, "no change": 1.0, "heat": 0.5}

    def plot_membership_functions(self, temp_range: tuple = (0, 50)) -> None:
        x = list(range(temp_range[0], temp_range[1] + 1))
        memberships = {key: [self.__memberships[key](val) for val in x] for key in self.__memberships}

        for label, y_vals in memberships.items():
            plt.plot(x, y_vals, label=label)

        plt.xlabel("Temperature (°C)")
        plt.ylabel("Membership Degree")
        plt.title("Fuzzy Membership Functions")
        plt.legend()
        plt.grid()
        plt.show()

    def fuzzify(self, current_temp: float) -> Dict[str, float]:
        return {key: self.__memberships[key](current_temp) for key in self.__memberships}

    def infer(self, antecedents: Dict[str, float]) -> Dict[str, float]:
        return {
            "heat": antecedents["very cold"] + antecedents["cold"],
            "no change": antecedents["warm"],
            "cool": antecedents["hot"] + antecedents["very hot"]
        }

    def __defuzzify_mom(self, consequents: Dict[str, float]) -> float:
        max_membership = max(consequents.values())
        max_keys = [key for key, value in consequents.items() if value == max_membership]
        return sum(self.__crisp_values[key] for key in max_keys) / len(max_keys)

    def __defuzzify_centroid(self, consequents: Dict[str, float]) -> float:
        numerator = sum(consequents[term] * self.__crisp_values[term] * self.__weights[term] for term in consequents)
        denominator = sum(consequents[term] * self.__weights[term] for term in consequents)
        return numerator / denominator if denominator != 0 else 0.0

    def defuzzify(self, consequents: Dict[str, float], method: str = "mom") -> float:
        if method == "mom":
            return self.__defuzzify_mom(consequents)
        elif method == "centroid":
            return self.__defuzzify_centroid(consequents)
        else:
            raise ValueError("Invalid defuzzification method")

    def evaluate(self, temperature: float, method: str = "mom") -> float:
        fuzzy_values = self.fuzzify(temperature)
        consequents = self.infer(fuzzy_values)
        return self.defuzzify(consequents, method)


# Example Usage:
system = TemperatureFuzzySystem()
system.plot_membership_functions()

print("Crisp Output (MoM) at 15°C:", system.evaluate(15, method="mom"))
print("Crisp Output (Centroid) at 15°C:", system.evaluate(15, method="centroid"))
