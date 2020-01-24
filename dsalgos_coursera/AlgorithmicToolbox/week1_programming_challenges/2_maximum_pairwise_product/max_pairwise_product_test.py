import unittest
import random
from max_pairwise_product import max_pairwise_product


class TestMaxPairwiseProduct(unittest.TestCase):
    def setUp(self):
        len = 1010
        test_arr = []
        call_arr = []
        for i in range(len):
            ran_num = random.randint(3, 100000000)
            if ran_num not in test_arr:
                test_arr.append(ran_num)
            call_arr.append(ran_num)

        sorted_arr = sorted(call_arr)
        self.expected = sorted_arr[-1] * sorted_arr[-2]
        self.callable_arr = call_arr

    def test_random_inputs(self):
        self.assertEqual(max_pairwise_product(self.callable_arr), self.expected)

if __name__ == "__main__":
     unittest.main()