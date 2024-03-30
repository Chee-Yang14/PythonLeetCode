class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        holder = []
        
        for i, char in enumerate(s): 
                        
           if len(holder) == 0:
               holder.append(char) 
               continue
           
           match char:
                case '(':
                   holder.append('(')
                case '[':
                   holder.append('[')
                case '{':
                   holder.append('{')
                case ')':
                    if holder.pop('(') == '(':
                        return False
                case ']':
                    if holder.pop('[') == '[':
                        return False
                case '}':
                    if holder.pop('{') == '{':
                        return False
        
        return True