import unittest
import inflect
from number_to_words import translate_number as translate
en = inflect.engine()


class TestNumbersToWords(unittest.TestCase):
    def test_zero(self):
        self.assertEqual("zero", translate(0))

    def test_single_digit(self):
        nums = ['one',
                'two',
                'three',
                'four',
                'five',
                'six',
                'seven',
                "eight",
                "nine"]
        for num, num_name in enumerate(nums, start=1):
            self.assertEqual(num_name + " ", translate(num))

    # ------------- TESTING AGAINST inflect.number_to_words ------------ #
    def test_double_digits(self):
        for i in range(10, 100):
            print(en.number_to_words(i))
            self.assertEqual(en.number_to_words(i) + " ", translate(i))


if __name__ == '__main__':
    unittest.main()
