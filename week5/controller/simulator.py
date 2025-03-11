import time

from week5.model.ocean import Ocean
from week5.view.gui import Gui


class Simulator:
    """Class representing a simulator."""

    def __init__(self) -> None:
        """
        Initialise the Simulator object.

        Initialises the environment, and generates the initial population of agents.
        """
        self.__ocean = Ocean(width=20, height=20)  # Define the ocean dimensions
        self.__agents = []
        self.__generate_initial_population()
        self.__is_running = False

        # Define a dictionary of agent_colours with class names and their associated colours
        self.__agent_colours = {
            "Shark": "blue",
            "Fish": "yellow",
            "Crab": "red"
        }

        # Initialise a new Gui object
        self.__gui = Gui(environment=self.__ocean, agent_colours=self.__agent_colours)

        # Render the Gui by invoking the appropriate method
        self.__gui.render()

    def __generate_initial_population(self) -> None:
        """
        Generate the initial population of agents.
        """
        # Example population generation logic
        for _ in range(10):
            self.__ocean.add_agent_randomly("Shark")
        for _ in range(20):
            self.__ocean.add_agent_randomly("Fish")
        for _ in range(15):
            self.__ocean.add_agent_randomly("Crab")

    def run(self) -> None:
        """Run the simulation."""
        self.__is_running = True

        while self.__is_running:
            self.__update()
            self.__render()
            time.sleep(1)
            if self.__gui.is_closed():
                self.__is_running = False

    def __render(self) -> None:
        """Render the current state of the simulation."""
        self.__gui.render()  # Render the current state of the Gui

    def __update(self) -> None:
        """Update the simulation state."""
        # Invoke the act method for each agent in the environment
        for agent in self.__agents:
            agent.act()


if __name__ == "__main__":
    """
    Entry point for running the simulation.
    """
    simulation = Simulator()
    simulation.run()
