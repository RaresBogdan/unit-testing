import unittest
from string_problems import StringExercises


class TestStringExercises(unittest.TestCase, StringExercises):

    # 1. Palindrome Function
    def test_is_str_palindrome_true(self):
        self.assertTrue(StringExercises.is_str_palindrome("racecar"))
        self.assertTrue(StringExercises.is_str_palindrome("A man, a plan, a canal: Panama!"))

    def test_is_str_palindrome_false(self):
        self.assertFalse(StringExercises.is_str_palindrome("hello world"))

    def test_is_str_palindrome_empty_input(self):
        with self.assertRaises(ValueError):
            StringExercises.is_str_palindrome("")

    def test_is_str_palindrome_non_string_input(self):
        with self.assertRaises(TypeError):
            StringExercises.is_str_palindrome(123)

    # 2. Longest Word Function
    def test_longest_word_single_word(self):
        self.assertEqual(self.longest_word("hello"), "hello")

    def test_longest_word_multiple_words(self):
        self.assertEqual(self.longest_word("the quick brown fox"), "There are multiple same length words: quick, brown")
        self.assertEqual(self.longest_word("the quick brown fox jumps over the lazy dog"),
                         "There are multiple same length words: quick, brown, jumps")

    def test_longest_word_empty_input(self):
        with self.assertRaises(ValueError):
            self.longest_word("")

    def test_longest_word_non_string_input(self):
        with self.assertRaises(TypeError):
            self.longest_word(123)

    def test_longest_word_special_character_input(self):
        with self.assertRaises(ValueError):
            self.longest_word("!@#$%^&*()")

    # 3. Reversed String Function
    def test_reverse_string_valid(self):
        self.assertEqual(self.reverse_string("hello"), "olleh")
        self.assertEqual(self.reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(self.reverse_string("hello!@#$%^&*()_+"), "+_)(*&^%$#@!olleh")

    def test_reverse_string_with_uppercase(self):
        self.assertEqual(self.reverse_string("Hello"), "olleh")

    def test_reverse_string_empty_input(self):
        with self.assertRaises(ValueError):
            self.reverse_string("")
        with self.assertRaises(ValueError):
            self.reverse_string("     ")

    def test_reverse_string_non_string_input(self):
        with self.assertRaises(TypeError):
            self.reverse_string(123)
        with self.assertRaises(TypeError):
            self.reverse_string([])

    # 4. Largest Number in List Function
    def test_largest_number_valid_input(self):
        self.assertEqual(self.largest_number([1, 2, 3]), 3)
        self.assertEqual(self.largest_number([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(self.largest_number([-1.5, -2.5, -3.5]), -1.5)

    def test_largest_number_empty_list(self):
        with self.assertRaises(ValueError):
            self.largest_number([])

    def test_largest_number_non_list_input(self):
        with self.assertRaises(TypeError):
            self.largest_number("not a list")
        with self.assertRaises(TypeError):
            self.largest_number(123)
        with self.assertRaises(TypeError):
            self.largest_number({"key": "value"})

    def test_largest_number_invalid_input(self):
        with self.assertRaises(TypeError):
            self.largest_number([1, 2, "3"])
        with self.assertRaises(TypeError):
            self.largest_number([1, 2, None])
        with self.assertRaises(TypeError):
            self.largest_number([1, 2, [3, 4]])

    # 5. Smallest Number in List Function
    def test_smallest_number_valid_input(self):
        self.assertEqual(self.smallest_number([1, 2, 3]), 1)
        self.assertEqual(self.smallest_number([1.5, 2.5, 3.5]), 1.5)
        self.assertEqual(self.smallest_number([-1.5, -2.5, -3.5]), -3.5)

    def test_smallest_number_empty_list(self):
        with self.assertRaises(ValueError):
            self.smallest_number([])

    def test_smallest_number_non_list_input(self):
        with self.assertRaises(TypeError):
            self.smallest_number("not a list")
        with self.assertRaises(TypeError):
            self.smallest_number(123)
        with self.assertRaises(TypeError):
            self.smallest_number({"key": "value"})

    def test_smallest_number_invalid_input(self):
        with self.assertRaises(TypeError):
            self.smallest_number([1, 2, "3"])
        with self.assertRaises(TypeError):
            self.smallest_number([1, 2, None])
        with self.assertRaises(TypeError):
            self.smallest_number([1, 2, [3, 4]])

    # 6. Most Common Word Function
    def test_most_common_word_valid_input(self):
        self.assertEqual(self.common_word("The quick brown fox jumps over the lazy dog."), "the")

    def test_most_common_word_multiple_common_words(self):
        self.assertIn(
            self.common_word
            ("The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy cat."),
            ["the", "quick", "brown", "fox", "jumps", "over", "lazy"])

    def test_common_word_same_frequency(self):
        self.assertEqual(self.common_word("The quick brown fox"), "All the words in the string have the same frequency")

    def test_common_word_empty_string(self):
        with self.assertRaises(ValueError):
            self.common_word("")

    def test_common_word_input_not_string(self):
        with self.assertRaises(TypeError):
            self.common_word(123)

    def test_common_word_only_punctuation(self):
        with self.assertRaises(ValueError):
            self.common_word("!@#$%^&*()")

    def test_common_word_mixed_case(self):
        self.assertEqual(self.common_word("The QUICK Brown fOx juMps over tHe lazy dog."), "the")

    # 7. Most Frequent Letter Function
    def test_uppercase_letters(self):
        self.assertEqual(self.most_frequent_letter("HELLO"), "The most frequent letter is l")

    def test_multiple_common_letters(self):
        self.assertEqual(self.most_frequent_letter("mississippi"), "There are multiple most frequent letters: i, s")

    def test_empty_string(self):
        with self.assertRaises(TypeError):
            self.most_frequent_letter("")

    def test_whitespace_string(self):
        with self.assertRaises(TypeError):
            self.most_frequent_letter("   ")

    def test_punctuation_marks(self):
        self.assertEqual(self.most_frequent_letter("hello! world!!"), "The most frequent letter is l")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            self.most_frequent_letter(123)


if __name__ == '__main__':
    unittest.main()
