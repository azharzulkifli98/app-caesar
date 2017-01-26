def alphabet_position(letter):
    """
    given letter return numeric value
    """
    thebet2 = "abcdefghijklmnopqrstuvwxyz"
    num = 0
    first_letter = letter.lower()
    for j in range(len(thebet2)):
        if thebet2[j] == first_letter:
            num = num + j
    return num

def rotate_character(char, rot):
    """
    given letter rotate by given number
    """
    thebet = "abcdefghijklmnopqrstuvwxyz"
    caps = False
    if char.isupper():
        caps = True
    oldnum = alphabet_position(char)
    newnum = oldnum + rot
    newnum = newnum % 26
    if caps:
        newchar = thebet[newnum]
        newchar = newchar.upper()
    else:
        newchar = thebet[newnum]
        newchar = newchar.lower()
    return newchar
