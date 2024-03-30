class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        holder = []
        
        for char in s: 
                        
            if len(holder) == 0:
               holder.append(char) 
               continue
           
            if char == '(':
                holder.append('(')
                continue
            elif char == '[':
                holder.append('[')
                continue
            elif char == '{':
                holder.append('{')
                continue

            charHolder = holder.pop()
            
            if char == ')' and charHolder != '(':
                print(char, charHolder)
                return False
            if char == ']' and charHolder != '[':
                print(char, charHolder)
                return False
            if char == '}' and charHolder != '{':
                print(char, charHolder)
                return False
        
        return len(holder) == 0