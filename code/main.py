#!/usr/bin/env python
# -*- coding: utf-8 -*-
from confusables import Confusables
from confuseables_dict import confuseables_dict
import re


c = Confusables('286_ai_text_poison/code/confusables.txt')
string = "."
cpattern = c.confusables_regex(string)
print(cpattern)
#split_string = cpattern.split("][")
#print(split_string)
#clean_string = re.sub('[[\], ]','',split_string[-1])