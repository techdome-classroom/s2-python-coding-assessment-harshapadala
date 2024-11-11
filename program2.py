class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        for char in s:
            curr_value = roman_to_int[char]
            
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value
            else:
                result += curr_value
            
            prev_value = curr_value
        
        return result
