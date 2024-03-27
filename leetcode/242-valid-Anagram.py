class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        
        holds = list(s)
        holdt = list(t)
        
        holds.sort
        holdt.sort
    
        if holds == holdt:
           return True
            
        return False
    
        