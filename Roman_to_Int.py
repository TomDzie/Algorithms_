class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        last_value = 0
        Roman_to_Digits = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for letter in s[::-1]:
            digit_value = Roman_to_Digits[letter]
            if digit_value >= last_value:
                value += digit_value
                last_value = digit_value
            else:
                value -= digit_value
        return value


A = Solution()
print(A.romanToInt("MLVIII"))