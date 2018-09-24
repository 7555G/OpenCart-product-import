#!/usr/bin/env python

COLORS = {
    'red':      ['κόκκινη', 'κόκκινο'],
    'dark blue':['σκούρο μπλε', 'σκούρο μπλε'], 
    'blue':     ['μπλε', 'μπλε'], 
    'navy blue':['Navy μπλε', 'Navy μπλε'],
    'rose':     ['ρωζ', 'ρωζ'],
    'gold':     ['χρυσή', 'χρυσό'],
    'silver':   ['ασημένια', 'ασημένιο'],
    'rose gold':['ρωζ χρυσή', 'ρωζ χρυσό'],
    'pink gold':['ρωζ χρυσή', 'ρωζ χρυσό'],
    'pink':     ['ρωζ', 'ρωζ'],
    'brown':    ['καφέ', 'καφέ'],
    'black':    ['μαύρη', 'μαύρο'],
    'white':    ['λευκή', 'λευκό'],
    'yellow':   ['κίτρινη', 'κίτρινο'],
    'green':    ['πράσινη', 'πράσινο'],
    'purple':   ['μωβ','μωβ'],
    'orange':   ['πορτοκαλί', 'πορτοκαλί'],
    'grey':     ['γκρι', 'γκρι'],
    'duco grey':['γκρι', 'γκρι'],
    'cyan':     ['γαλάζια', 'γαλάζιο'],
    'light blue':['γαλάζια', 'γαλάζιο'],
    'golden':    ['χρυσαφένια','χρυσαφί'],
    'dark brown':['σκούρα καφέ', 'σκούρο καφέ'],
    'light brown':['ανοιχτή καφέ', 'ανοιχτό καφέ'],
    'beige':    ['μπεζ','μπεζ'],
    'bordeaux': ['μπορντό', 'μπορντό'],
    'burgundy': ['burgundy', 'burgundy'],
    'burgund': ['burgundy', 'burgundy'],
    'cognac':   ['καφέ', 'καφέ'],
    'chestnut': ['ανοιχτή καφέ', 'ανοιχτό καφέ']
    }

# __color0, __color1
def get_color(pattern, string):

    color = "__color0"
    color_ind = 0
    if "__color1" in pattern:
        color = "__color1"
        color_ind = 1

    pattern_blocks = pattern.split()
    color_pos = pattern_blocks.index(color)
    colorless_pattern = pattern.replace(color, "").strip()

    # if we pattern = '__color' match with the first color you find
    if pattern == "__color1" or pattern == "__color0":
        # print("seaching color in: "+string)
        curr = ""
        prev_pos = 100000000
        for col in COLORS:
            if string.find(col.lower()) != -1 and string.find(col.lower()) < prev_pos:
                curr = col
                prev_pos = string.find(col)

        if curr:
            return [curr, COLORS[curr][color_ind]]
        else:
            return []


    # If the pattern without the color is not present, return
    if colorless_pattern not in string:
        return []

    key_word_pos = string.index(colorless_pattern)

    if color_pos == 0:
        # If the color was first check the words previous from the colorless pattern
        string_to_check = string[:key_word_pos]
        string_words = list(reversed(string_to_check.split()))
        inversed = True
    else:
        string_to_check = string[key_word_pos:]
        string_words = string_to_check.split()
        inversed = False

    # We match the colors with most words first
    for i in range(len(string_words)):
        word = string_words[i].lower()
        if i == len(string_words) -1:
            # Last word
            if word in COLORS:
                return [word, COLORS[word][color_ind]]
        else:
            next_word = string_words[i+1].lower()

            if (next_word + ' ' + word) in COLORS and inversed:
                color_key = next_word + ' ' + word 
                return [color_key, COLORS[color_key][color_ind]]
            
            if (word + ' ' + next_word) in COLORS and not inversed:
                color_key = word + ' ' + next_word
                return [color_key, COLORS[color_key][color_ind]]
            
            if word in COLORS:
                return [word, COLORS[word][color_ind]]

    return []


def replace_colors(string, color):
    return string.replace("__color", color)