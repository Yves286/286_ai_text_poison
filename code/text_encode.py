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
        