from abc import ABC, abstractmethod
from week5.model.location import Location
from week5.model.ocean import Ocean


class Agent(ABC):
    def __init__(self, location: Location):
        self.__location = location

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, new_location: Location) -> None:
        self.__location = new_location

    @abstractmethod
    def act(self, ocean: Ocean) -> None:
        """
        Abstract method that defines the behavior of the agent within the ocean environment.

        :param ocean: An instance of the Ocean class representing the environment.
        """
        pass
