class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_lower = s.lower()
        filtered_str = ''.join(char for char in str_lower if char.isalnum() or char.isalpha())
    
        if len(filtered_str) <= 1:  # Corrected condition
            return True
        
        start_pointer = 0
        end_pointer = len(filtered_str) - 1
        
        while start_pointer <= end_pointer:
            start_char = filtered_str[start_pointer]
            end_char = filtered_str[end_pointer]
            
            if start_char != end_char:
                return False
            
            start_pointer += 1
            end_pointer -= 1
            
        return True