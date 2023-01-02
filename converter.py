def text_to_dec(text):
    converted = ''
    for letter in text:
        decimal =  str(ord(letter))
        converted += decimal+ " "
    return converted