def caesarCipher(s, k):
    # Write your code here
    newString = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    limit = len(alphabet)
    
    for letter in s:
        if letter.lower() in alphabet:
            index = alphabet.index(letter.lower())
            movedIndex = (index + k) % limit
            if letter.isupper():
                newString += (alphabet[movedIndex].upper())
            else:
                newString += alphabet[movedIndex]
        else:
            newString += letter
    
    return newString
            
    
