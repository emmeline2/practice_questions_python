class Solution(object):
    letters = {"a": ".-", "b": "-...", "c": "-.-.",
               "d":"-..", "e": ".","f": "..-.",
               "g":"--.", "h":"....", "i":"..",
               "j":".---", "k":"-.-", "l":".-..",
               "m":"--", "n":"-.", "o":"---",
               "p":".--.", "q":"--.-", "r":".-.",
               "s":"...", "t":"-", "u":"..-",
               "v":"...-", "w":".--", "x":"-..-",
               "y":"-.--", "z":"--.."}
    
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = set()
        
        # translate each word given to morse code
        for word in words: 
            codes.add(self.translate_word(word))
        
        # sets don't allow duplicates so return
        # length of set for unique words
        return len(codes)
    
    def translate_word(self, word):
        morse_code = ""
        
        # Translate each letter and append
        for i in word:
            morse_code += self.letters[str(i)]
        
        return morse_code
            
            
        
