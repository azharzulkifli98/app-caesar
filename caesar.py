from helpers import alphabet_position, rotate_character
from sys import argv, exit

def user_input_is_valid(list_argv):
    user_input_is_valid = True
    if len(list_argv) != 2:
        user_input_is_valid = False
    elif not list_argv[1].isdigit():
        user_input_is_valid = False
    return user_input_is_valid

def encrypted(text):
    """
    take text and rotate letters across alphabet_position
    """
    secret = ""
    for i in range(len(text)):
        if text[i].isalpha():
            secret = secret + rotate_character(text[i], 13)
        else:
            secret = secret + text[i]
    return secret

def main():
    u_valid = user_input_is_valid(argv)

    if not u_valid:
        print("usage: python3 caesar.py n")
    else:
        print("Type a message:")
        tex = input()
        num = argv[1]
        num = int(num)
        print(encrypt(tex, num))

if __name__ == '__main__':
    main()
