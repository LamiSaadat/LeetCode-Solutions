class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}

        result = 0
        prev_val = 0

        for c in s:
            curr_val = numeral_map[c]
            result += curr_val
            if curr_val > prev_val:
                result -= 2 * prev_val
            prev_val = curr_val
        return result
