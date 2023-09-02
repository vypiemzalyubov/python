# 5 kyu
# Rot13
# 
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. 
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.

def rot13(message):
    tmp = []
    for c in message:
        if c.isalpha() and not c.isupper():
            tmp.append(chr((ord(c) - 97 + 13) % 26 + 97))
        elif c.isalpha() and c.isupper():
            tmp.append(chr((ord(c.lower()) - 97 + 13) % 26 + 97).upper())            
        else:
            tmp.append(c)
    return ''.join(tmp)



# Best Practices

def rot13(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputMessage = ""
    for letter in message:
        if letter in alpha.lower():
            outputMessage += alpha[(alpha.lower().index(letter) +13) % 26].lower()
        elif letter in alpha:
            outputMessage += alpha[(alpha.index(letter) +13) % 26]
        else:
            outputMessage += letter
    return outputMessage