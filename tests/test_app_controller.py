import unittest
from app.app_controller import AppController

class TestAppController(unittest.TestCase):
    def setUp(self):
        self.controller = AppController()

    def test_initial_counter(self):
        self.assertEqual(self.controller.counter, 0)

    def test_increment(self):
        self.controller.increment()
        self.assertEqual(self.controller.counter, 1)

    def test_decrement(self):
        self.controller.decrement()
        self.assertEqual(self.controller.counter, -1)

    def test_reset(self):
        self.controller.increment()
        self.controller.increment()
        self.controller.reset()
        self.assertEqual(self.controller.counter, 0)

    def test_property_setter(self):
        self.controller.counter = 42
        self.assertEqual(self.controller.counter, 42)

if __name__ == "__main__":
    unittest.main()
