import unittest


class test_circle(unittest.TestCase):
    def test_area(self):
        self.assertEqual((22 / 7) * 7 * 7, 154)


class test_rectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(2 * 5, 10)


if __name__ == '__main__':
    unittest.main()
