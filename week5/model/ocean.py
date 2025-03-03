from typing import List, Optional
from week5.model.environment import Environment
from week5.model.agent import Agent
from week5.model.location import Location


class Ocean(Environment):
    """Concrete class representing the Ocean, extending the abstract Environment class."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def clear(self):
        """Clears the environment of all agents."""
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]

    def get_agent(self, location: Location) -> Optional[Agent]:
        """Returns the agent at the specified location, if any."""
        return self.grid[location.get_y()][location.get_x()]

    def set_agent(self, agent: Agent, location: Location):
        """Sets an agent at the specified location."""
        self.grid[location.get_y()][location.get_x()] = agent

    def get_height(self) -> int:
        """Returns the height of the environment grid."""
        return self.height

    def get_width(self) -> int:
        """Returns the width of the environment grid."""
        return self.width

    def find_free_adjacent_locations(self, location: Location) -> List[Location]:
        """Finds and returns a list of free adjacent locations, considering the wrapping behavior."""
        offsets = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)]

        free_locations = []
        for offset_x, offset_y in offsets:
            new_x = (location.get_x() + offset_x) % self.width
            new_y = (location.get_y() + offset_y) % self.height
            new_location = Location(new_x, new_y)
            if self.get_agent(new_location) is None:
                free_locations.append(new_location)

        return free_locations
