import unittest
from week5.model.location import Location

class TestLocation(unittest.TestCase):
    def test_init(self):
        loc = Location(3, 4)
        self.assertEqual(loc.get_x(), 3)
        self.assertEqual(loc.get_y(), 4)

    def test_setters(self):
        loc = Location(3, 4)
        loc.set_x(10)
        loc.set_y(20)
        self.assertEqual(loc.get_x(), 10)
        self.assertEqual(loc.get_y(), 20)

    def test_equals(self):
        loc1 = Location(3, 4)
        loc2 = Location(3, 4)
        loc3 = Location(5, 6)
        self.assertTrue(loc1.equals(loc2))
        self.assertFalse(loc1.equals(loc3))

    def test_str(self):
        loc = Location(3, 4)
        self.assertEqual(str(loc), "Location(x=3, y=4)")

if __name__ == '__main__':
    unittest.main()
