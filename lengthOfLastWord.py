class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if len(words) == 0:
            return 0
        end_element = len(words) - 1
        return len(words[end_element])
