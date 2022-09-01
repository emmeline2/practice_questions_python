class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_letters = {}
        
        if len(words) < 1 or len(words) is None:
            return []

        # set up first hash map
        for letter in words[0]:
            if letter not in common_letters:
                common_letters[letter] = 1
            else:
                common_letters[letter] += 1
        
        
        # compare with other words in set
        for i in range(1,len(words)):
            temp_letters = {}
            for letter in words[i]:
                if letter not in temp_letters:
                    temp_letters[letter] = 1
                else:
                    temp_letters[letter] += 1
            
            for key,value in common_letters.items():
                if key not in temp_letters:
                    del common_letters[key]
                else:
                    if value > temp_letters[key]:
                        # reset value for duplicates
                        common_letters[key] = temp_letters[key]
                    if value < temp_letters[key]: 
                        pass
                    else: 
                        pass
        
        # create output string
        ret_string = []
        for key,value in common_letters.items():
            temp_str = []
            for i in range(0, value):
                temp_str.append(key)
            ret_string += temp_str
        
        return ret_string
                        
