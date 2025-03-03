import unittest
from week5.model.location import Location
from week5.model.agent import Agent

class TestAgentConcrete(Agent):
    def act(self, ocean: 'Ocean') -> None:
        """Concrete implementation of the abstract act method."""
        pass

class TestAgent(unittest.TestCase):

    def test_get_location(self):
        location = Location(5, 10)
        agent = TestAgentConcrete(location)
        self.assertEqual(agent.get_location(), location)

    def test_set_location(self):
        location1 = Location(5, 10)
        location2 = Location(15, 20)
        agent = TestAgentConcrete(location1)
        agent.set_location(location2)
        self.assertEqual(agent.get_location(), location2)

    def test_location_attributes(self):
        location = Location(5, 10)
        agent = TestAgentConcrete(location)
        self.assertEqual(agent.get_location().get_x(), 5)
        self.assertEqual(agent.get_location().get_y(), 10)

    def test_location_setters(self):
        location = Location(5, 10)
        agent = TestAgentConcrete(location)
        agent.get_location().set_x(15)
        agent.get_location().set_y(20)
        self.assertEqual(agent.get_location().get_x(), 15)
        self.assertEqual(agent.get_location().get_y(), 20)

if __name__ == '__main__':
    unittest.main()
