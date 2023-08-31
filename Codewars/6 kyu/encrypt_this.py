# 6 kyu
# Encrypt this!
# 
# Description:
# Encrypt this!
# 
# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
# 1. Your message is a string containing space separated words.
# 2. You need to encrypt each word in the message using the following rules:
#    - The first letter must be converted to its ASCII code.
#    - The second letter must be switched with the last letter
# 3. Keepin' it simple: There are no special characters in the input.
# 
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
    tmp = []
    for i in text.split():
        if len(i) > 2:
            tmp.append(f'{ord(i[0])}{i[-1]}{i[2:-1]}{i[1]}')
        elif len(i) == 2:
            tmp.append(f'{ord(i[0])}{i[1]}')
        else:
            tmp.append(f'{ord(i[0])}')
    return ' '.join(tmp)



# Best Practices

def encrypt_this(text):
    result = []
    for word in text.split():
        word = list(word)
        word[0] = str(ord(word[0]))
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        result.append(''.join(word))
    return ' '.join(result)