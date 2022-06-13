import unittest


class TestDummy(unittest.TestCase):
    def setUp(self):
        pass

    def test_dummy(self):
        self.assertEqual(True, True, "I leave Python!")


if __name__ == "__main__":
    unittest.main()
