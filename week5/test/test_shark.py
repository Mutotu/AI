import unittest
from week5.model.location import Location
from week5.model.ocean import Ocean
from week5.model.shark import Shark

class TestShark(unittest.TestCase):

    def setUp(self):
        self.ocean = Ocean(5, 5)
        self.location = Location(2, 2)
        self.shark = Shark(self.location)
        self.ocean.set_agent(self.shark, self.location)

    def test_initial_location(self):
        self.assertEqual(self.shark.get_location(), self.location)

    def test_act_move_shark(self):
        initial_location = self.shark.get_location()
        self.shark.act(self.ocean)
        new_location = self.shark.get_location()
        self.assertNotEqual(initial_location, new_location)
        self.assertIsNone(self.ocean.get_agent(initial_location))
        self.assertEqual(self.ocean.get_agent(new_location), self.shark)

if __name__ == '__main__':
    unittest.main()
