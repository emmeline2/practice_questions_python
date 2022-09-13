class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) is None or len(s) == 1: 
            return s
        
        start = 0
        end = len(s) - 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(s)
        while start < end:
            # start and end are both vowels -> swap
            if s[start] in vowels and s[end] in vowels:
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start += 1
                end -= 1
            # start char is a vowel
            elif s[start] in vowels:
                end -= 1
            # end char is a vowel
            elif s[end] in vowels:
                start += 1
            # no vowels present
            else:
                start += 1
                end -= 1
        
        return ''.join(s)
        
