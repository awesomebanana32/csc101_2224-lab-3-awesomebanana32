import unittest
import point


class TestCases(unittest.TestCase):
    def test_point_one(self):
        pt = point.Point(1, 2)
        self.assertAlmostEqual(pt.x, 1)
        self.assertAlmostEqual(pt.y, 2)

    def test_point_two(self):
        pt = point.Point(-4.7, 19.2)
        self.assertAlmostEqual(pt.x, -4.7)
        self.assertAlmostEqual(pt.y, 19.2)

    def test_equality_one(self):
        point1 = point.Point(7, 7)
        point2 = point.Point(7, 7)
        self.assertEqual(point1,point2)


    def test_equality_two(self):
        point1 = point.Point(2, 4)
        point2 = point.Point(5, 5)
        self.assertNotEqual(point1, point2)

        


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
