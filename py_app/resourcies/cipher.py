def ciph(message):

    """function that takes a string as input and converts it into a ciphered string"""
    # message = input('please enter your message \n')

    glyph = ''

    for i in message:

        glyph += chr(ord(i) + 3)

    # print(glyph.__hash__())       
    return glyph    

    