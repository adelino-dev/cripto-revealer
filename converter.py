def text_to_dec(text):
    converted = ''
    for letter in text:
        decimal =  str(ord(letter))
        converted += decimal+ " "
    return converted

def text_to_bin(text):
    converted = ''
    for letter in text:
        binary =  bin(ord(letter))[2:]
        length = len(binary)
        if  length < 8:
            binary = '0'*(8-length)+binary

        converted += binary+" "    
    return converted