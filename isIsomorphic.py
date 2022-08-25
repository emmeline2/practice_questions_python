class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # occurances of letters
        s_map = {}
        for letter in s:
            if letter not in s_map:
                s_map[letter] = 1
            else: 
                s_map[letter] += 1
        
        t_map = {}
        for letter in t:
            if letter not in t_map:
                t_map[letter] = 1
            else: 
                t_map[letter] += 1
        
        # check if number of letters matches
        if len(t_map) != len(s_map):
            return False
        
        
        # check if values of letter frequency matches
        s_values = list(s_map.values())
        t_values = list(t_map.values())
        for value in s_values: 
            if value in t_values:
                t_values.remove(value)
            else:
                return False
                
        return True
