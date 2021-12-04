# -*- coding: utf-8 -*-

import tokenize

def translate_code(readline, translations):
    for type, name, _,_,_ in tokenize.generate_tokens(readline):
        # print(type, name, tokenize.NAME)
        if type == tokenize.NAME and name in translations:
            yield tokenize.NAME, translations[name]
        elif name == '💩' or name == '♦' or name == '🍜':
            yield tokenize.NAME, translations[name]
        else:
            yield type, name
            
