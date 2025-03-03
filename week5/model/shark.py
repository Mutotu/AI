from typing import List
import random
from week5.model.agent import Agent
from week5.model.location import Location
from week5.model.ocean import Ocean


class Shark(Agent):
    def __init__(self, location: Location):
        super().__init__(location)

    def act(self, ocean: Ocean) -> None:
        """
        Defines the behavior of the shark within the ocean environment.

        :param ocean: An instance of the Ocean class representing the environment.
        """
        self.__swim(ocean)

    def __swim(self, ocean: Ocean) -> None:
        """
        Moves the shark to a free adjacent location within the ocean.

        :param ocean: An instance of the Ocean class representing the environment.
        """
        current_location = self.get_location()
        free_locations = ocean.find_free_adjacent_locations(current_location)
        if free_locations:
            new_location = random.choice(free_locations)
            ocean.set_agent(self, new_location)
            ocean.set_agent(None, current_location)
            self.set_location(new_location)
