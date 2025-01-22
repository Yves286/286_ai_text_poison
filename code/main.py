#!/usr/bin/env python
# -*- coding: utf-8 -*-
from confusables import Confusables
import re

"""
Quick demo of Confusables class
"""

c = Confusables('286_ai_text_poison/code/confusables.txt')

string = "Hello"
cpattern = c.confusables_regex(string)
print("Regexp pattern: {}".format(cpattern))
r = re.compile(cpattern)