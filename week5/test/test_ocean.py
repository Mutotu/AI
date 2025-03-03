import unittest
from week5.model.location import Location
from week5.model.agent import Agent
from week5.model.ocean import Ocean

class TestOcean(unittest.TestCase):

    def setUp(self):
        self.ocean = Ocean(5, 5)
        self.agent = Agent(Location(2, 2))
        self.ocean.set_agent(self.agent, self.agent.get_location())

    def test_clear(self):
        self.ocean.clear()
        for row in range(self.ocean.get_height()):
            for col in range(self.ocean.get_width()):
                self.assertIsNone(self.ocean.get_agent(Location(col, row)))

    def test_get_agent(self):
        self.assertEqual(self.ocean.get_agent(Location(2, 2)), self.agent)

    def test_set_agent(self):
        new_agent = Agent(Location(3, 3))
        self.ocean.set_agent(new_agent, new_agent.get_location())
        self.assertEqual(self.ocean.get_agent(Location(3, 3)), new_agent)

    def test_find_free_adjacent_locations(self):
        free_locations = self.ocean.find_free_adjacent_locations(Location(2, 2))
        self.assertEqual(len(free_locations), 8)
        for loc in free_locations:
            self.assertIsNone(self.ocean.get_agent(loc))

if __name__ == '__main__':
    unittest.main()
