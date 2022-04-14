import unittest
import conditional

class TestCases(unittest.TestCase):
    def test_max_101(self):
        condi = conditional.max_101(1,6)
        print("this is the max", condi)

    def test_max_101_again(self):
        condi = conditional.max_101(10,1)
        print("this is the max", condi)

    def test_max_of_three(self):
        three = conditional.max_of_three(10, 1, 2)
        print("this is the max of three:", three)

    def test_max_of_three_again(self):
        three = conditional.max_of_three(0, 1, 20)
        print("this is the max of three:", three)

    def test_max_of_three_again_2(self):
        three = conditional.max_of_three(0, 100, 20)
        print("this is the max of three:", three)

    def test_rental_late_fee(self):
        fee = conditional.rental_late_fee(0)
        print("this is the late fee:", fee)

    def test_rental_late_fee_1(self):
        fee = conditional.rental_late_fee(7)
        print("this is the late fee:", fee)

    def test_rental_late_fee_2(self):
        fee = conditional.rental_late_fee(15)
        print("this is the late fee:", fee)

    def test_rental_late_fee_3(self):
        fee = conditional.rental_late_fee(20)
        print("this is the late fee:", fee)

    def test_rental_late_fee_4(self):
        fee = conditional.rental_late_fee(100)
        print("this is the late fee:", fee)
# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

