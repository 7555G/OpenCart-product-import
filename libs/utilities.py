#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distance import levenshtein    

def replace_chars(chars_string, the_string, new_char=""):
    for char in chars_string:
        the_string = the_string.replace(char, new_char)

    return the_string

def closest_match(string, strings_container):
    
    smallest_dist = 100
    closest_match = ""
    for match_candidate in strings_container:
    
        new_dist = levenshtein(replace_chars(" >/-._", string).lower(), \
                               replace_chars(" >/-._", match_candidate).lower())    
        if new_dist < smallest_dist:
            smallest_dist = new_dist
            closest_match = match_candidate

    return closest_match

def rmcomma(instr, word=" and", num_of_commas=1):
    """ Replace last comma with and"""
    k = instr.rfind(",")
    if len(instr.split(",")) - 1 < num_of_commas:
        return instr

    return instr[:k] + word + instr[k+1:]
