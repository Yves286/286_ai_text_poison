import random
from confuseables_dict import confuseables_dict

def replace_char(str_input):
    output = ""
    for c in str_input: # for each character, find the matching key in confuseables_dict
        if c in confuseables_dict: # IF match - replace with random character in value
            confuseable_chars = confuseables_dict[c]# for each character, find the matching key in confuseables_dict
            rand_int = random.randint(0, len(confuseable_chars)-1)
            output = output + confuseable_chars[rand_int]
        else:
            output = output + c
    return output
        

if __name__ == "__main__":
    str_user = None
    print(type(str_user))
    while (str_user is None) or (len(str_user) == 0):
        str_user = input("Input the text you want encoded: ")
    print("Your encoded text is: " + replace_char(str_user))