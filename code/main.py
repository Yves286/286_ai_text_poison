#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from confusables import Confusables
from confuseables_dict import confuseables_dict
import re


c = Confusables('286_ai_text_poison/code/confusables.txt')
string = "BING BONG!! You have been caught by the A.I. police!" # pass a string
output = ""
for c in string: # for each character, find the matching key in confuseables_dict
    if c in confuseables_dict: # IF match - replace with random character in value
        confuseable_chars = confuseables_dict[c]
        print(confuseable_chars) # for each character, find the matching key in confuseables_dict
        rand_int = random.randint(0, len(confuseable_chars)-1)
        print(rand_int)
        output = output + confuseable_chars[rand_int]
    else:
        output = output + c
print(output)