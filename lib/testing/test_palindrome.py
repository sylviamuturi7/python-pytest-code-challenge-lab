import pytest
from palindrome import longest_palindromic_substring


class TestLongestPalindromicSubstring:
    
    @pytest.mark.parametrize("input_str,expected", [
        ("babad", ["bab", "aba"]),  # Multiple valid answers
        ("cbbd", ["bb"]),           # Single valid answer
        ("a", ["a"]),                # Single character
        ("ac", ["a", "c"]),          # Either character is valid
        ("racecar", ["racecar"]),    # Entire string is palindrome
        ("bb", ["bb"]),              # Two same characters
        ("abc", ["a", "b", "c"]),    # No palindrome longer than 1
    ])
    def test_basic_cases(self, input_str, expected):
        result = longest_palindromic_substring(input_str)
        assert result in expected, f"Expected one of {expected}, got '{result}'"
    
    def test_empty_string(self):
        result = longest_palindromic_substring("")
        assert result == "", "Empty string should return empty string"
    
    def test_single_character(self):
        test_cases = ["x", "1", "a", "Z"]
        for char in test_cases:
            result = longest_palindromic_substring(char)
            assert result == char, f"Single character '{char}' should return '{char}'"
    
    def test_all_same_characters(self):
        test_cases = [
            ("aaaa", "aaaa"),
            ("bbbbbb", "bbbbbb"),
            ("111111", "111111"),
        ]
        for input_str, expected in test_cases:
            result = longest_palindromic_substring(input_str)
            assert result == expected, f"All same characters '{input_str}' should return '{expected}'"
    
    def test_even_length_palindromes(self):
        test_cases = [
            ("abccba", "abccba"),
            ("abba", "abba"),
            ("abccbaxyz", "abccba"),
            ("xyzabccba", "abccba"),
        ]
        for input_str, expected in test_cases:
            result = longest_palindromic_substring(input_str)
            assert result == expected, f"Even length palindrome '{input_str}' should return '{expected}'"
    
    def test_odd_length_palindromes(self):
        test_cases = [
            ("abcba", "abcba"),
            ("racecar", "racecar"),
            ("madam", "madam"),
            ("xyzabcba", "abcba"),
        ]
        for input_str, expected in test_cases:
            result = longest_palindromic_substring(input_str)
            assert result == expected, f"Odd length palindrome '{input_str}' should return '{expected}'"
    
    def test_long_string(self):
        # Test with a longer string to ensure performance
        input_str = "a" * 100 + "b" * 100 + "a" * 100
        expected = "a" * 100  # First 100 'a's is a valid longest palindrome
        result = longest_palindromic_substring(input_str)
        assert len(result) >= 100, f"Long string should return palindrome of at least 100 characters"
