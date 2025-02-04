import random
from confuseables_dict import confuseables_dict
from text_encode import replace_char

if __name__ == "__main__":
    str_user = None
    while (str_user is None) or (len(str_user) == 0):
        str_user = input("Input the text you want encoded: ")
    print("Your encoded text is: " + replace_char(str_user))