from abc import ABC, abstractmethod
from typing import Optional

from week5.model.agent import Agent
from week5.model.location import Location


class Environment(ABC):
    """Abstract class representing a 2D environment for agents."""

    @abstractmethod
    def clear(self):
        """Clears the environment of all agents."""
        pass

    @abstractmethod
    def get_agent(self, location: Location) -> Optional[Agent]:
        """Returns the agent at the specified location, if any."""
        pass

    @abstractmethod
    def set_agent(self, agent: Agent, location: Location):
        """Sets an agent at the specified location."""
        pass

    @abstractmethod
    def get_height(self) -> int:
        """Returns the height of the environment grid."""
        pass

    @abstractmethod
    def get_width(self) -> int:
        """Returns the width of the environment grid."""
