class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        for i in range(len(s) - 1):
            if roman_values[s[i]] < roman_values[s[i + 1]]:
                number -= roman_values[s[i]]
            else:
                number += roman_values[s[i]]
        number += roman_values[s[-1]]
        return number
