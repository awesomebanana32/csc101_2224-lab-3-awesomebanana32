import unittest
import logic

class TestCases(unittest.TestCase):
    def test_case(self):
        joe = logic.is_even(4)
        print("this is even", joe)
        self.assertAlmostEqual(joe, True)

    def test_case_again(self):
        joe = logic.is_even(5)
        print("this is even", joe)
        self.assertAlmostEqual(joe, False)

    def test_in_an_interval(self):
        range_num = logic.in_an_interval(3)
        print("this is in range", range_num)
        self.assertAlmostEqual(range_num, True)

    def test_in_an_interval_again(self):
        range_num = logic.in_an_interval(1000000)
        print("this is in range", range_num)
        self.assertAlmostEqual(range_num, False)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

