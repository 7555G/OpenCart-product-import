#!/usr/bin/env python

COLUMN_TRANSF_RULES = {}    # { 'ΚΑΣΑ': {'S.STEEL':'Ατσαλι'}}

# Now define the transformation dictionaries for each column
# __color0 : θυληκο
# __color1: ουδέτερο
# [eng, gr, lvl]

# -----------------------------------------------------------------------------
# ΡΟΛΟΓΙΑ
watches_kasa = { 
         'STEEL':        ['stainless steel,','ανοξείδωτο ατσάλι,', 0],
         'S.S':          ['stainless steel,','ανοξείδωτο ατσάλι,', 0],
         '__color1 ceramic': ['__color ceramic,', '__color κεραμικό,', 3],
         'ceramic':      ['ceramic,', 'κεραμικό,', 3],
         'IP __color0':  ['IP __color,','με __color επίστρωση,', 1],
         'PVD __color0': ['PVD __color,','με __color επίστρωση,', 2],
         'crystals':     ['with crystals stones,','με κρυστάλλους,', 4],
         'diamonds':     ['with real diamonds,','με διαμάντια,', 5],
         'zirconia':     ['with cubic zirconia stones,','με κυβική ζιρκόνια,', 6],
         'open':         ['open type,', 'ανοιχτού τύπου με κρύσταλλο στην κάτω πλευρά,', 0]
}

watches_waranty = { '2 years':  ['2 years', '2 χρόνια', 0]}

gender = { 'mens':   ['Gents', 'Ανδρικό', 0],
           'womens': ['Ladies', 'Γυναικείο', 0]}

watches_atm = { '3':  ['3atm', '3atm', 0],
                '5':  ['5atm', '5atm', 0],
                '10': ['10atm','10atm', 0]}

watches_mech = {
    '505':   ['Ronda 505', 'Ronda 505', 0],
    '515':   ['Ronda 515', 'Ronda 515', 0],
    '715':   ['Ronda 715', 'Ronda 715', 0],
    '751':   ['Ronda 751', 'Ronda 751', 0],
    '762':   ['Ronda 762', 'Ronda 762', 0],
    '764':   ['Ronda 764', 'Ronda 764', 0],
    '785':   ['Ronda 785', 'Ronda 785', 0],
    '1006':  ['Ronda 1006', 'Ronda 1006', 0],
    '1062':  ['Ronda 1062', 'Ronda 1062', 0],
    '1063':  ['Ronda 1063', 'Ronda 1063', 0],
    '5030':  ['Ronda 5030.D', 'Ronda 5030.D', 0],
    '6003':  ['Ronda 6003.D', 'Ronda 6003.D', 0],
    '6004':  ['Ronda 6004.D', 'Ronda 6004.D', 0],
    '6203':  ['Ronda 6203.D', 'Ronda 6203.D', 0],
    '7750':  ['Valjoux 7750', 'Valjoux 7750', 0],
    'Z60':   ['Ronda Z60', 'Ronda Z60', 0],

    'quartz':    ['Swiss Quartz', 'Swiss Quartz', 1],
    'automatic': ['Swiss automatic', 'Swiss automatic', 1],

    'chronograph': ['chronograph','χρονογράφος', 2]
}

watches_glass = {
    'Sapphire': ['Sapphire','Ζαφείρι',0],
    'mineral' : ['Mineral glass', 'ορυκτό κρύσταλλο',0],
    'faceted':  ['faceted mineral glass', 'πρισματικό ορυκτό κρύσταλλο', 0]
}

watches_functions = {
    'big':       ['Big','Μεγάλη', 1],
    'date':      ['date indication,', 'ένδειξη ημερομηνίας,', 2],
    'daydate':   ['day and date indication,', 'ένδειξη ημερομηνίας και ημέρας,', 2],
    'day':          ['day indication,', 'ένδειξη ημέρας,', 2],
    '24hr':         ['24 hour indication,', 'ένδειξη 24 ωρών,', 4],
    'world time':   ['world time indication,', 'ένδειξη παγκόσμιας ώρας,', 5],
    'chronograph':  ['chronograph,','χρονογράφος,', 6]
}

watches_strap_material = {
    'STEEL':             ['stainless steel,','ανοξείδωτο ατσάλι,', 0],
    'S.S':               ['stainless steel,','ανοξείδωτο ατσάλι,', 0],
    'titanium':          ['titanium', 'τιτάνιο', 0],
    '__color1 Ceramic':  ['__color ceramic,', '__color κεραμικό,', 3],
    'IP __color0':       ['IP __color,','__color επίστρωση,', 1],
    'PVD __color0':      ['PVD __color','__color επίστρωση', 2],
    '__color1 leather':  ['__color genuine leather', '__color δερμάτινο', 4],
    'leather __color1':  ['__color genuine leather', '__color δερμάτινο', 4],
    'leather':           ['Leather', 'δερμάτινο', 4],
    '__color1 rubber':   ['__color rubber', '__color καουτσούκ', 4],
    'rubber __color1':   ['__color rubber', '__color καουτσούκ', 4],
    '__color1 satin':    ['__color satin', '__color σατέν', 4],
    '__color0 silicone': ['__color silicone', '__color σιλικόνη', 4]
}

watches_clasp_type = {
    'normal':    ['Buckle','τοκάς', 0],
    'folding':   ['folding buckle', 'αναδιπλώμενο κούμπωμα', 0],
    'butterfly': ['folding buckle', 'αναδιπλώμενο κούμπωμα', 0]
}

watches_back_type = {
    'open': ['open type', 'ανοιχτού τύπου με κρύσταλλο στην κάτω πλευρά', 0]
}

watches_strap = {
    'strap':     ['leather strap','λουράκι δερμάτινο', 0],
    'bracelet': ['Stainless steel bracelet', 'μπρασελέ από ανοξείδωτο ατσάλι', 0]
}


COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']               = {}
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΚΑΣΑ']       = watches_kasa
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΕΓΓΥΗΣΗ']    = watches_waranty
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΑΔΙΑΒΡΟΧΟ']  = watches_atm
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΣΤΕΦΑΝΗ']    = watches_kasa
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΜΗΧΑΝΙΣΜΟΣ'] = watches_mech
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΦΥΛΟ']       = gender
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΚΡΥΣΤΑΛΛΟ']       = watches_glass
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΛΕΙΤΟΥΡΓΙΕΣ']     = watches_functions
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΥΛΙΚΟ ΔΕΣΙΜΑΤΟΣ'] = watches_strap_material
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΚΟΥΜΠΩΜΑ']        = watches_clasp_type
COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΚΑΠΑΚΙ']          = watches_back_type
# COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΔΕΣΙΜΟ']          = watches_strap
# COLUMN_TRANSF_RULES['ΡΟΛΟΓΙΑ']['ΥΛΙΚΟ ΔΕΣΙΜΑΤΟΣ'] = watch_strap_material

# ΡΟΛΟΓΙΑ                                
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# ΑΝΤΑΛΛΑΚΤΙΚΑ

parts_color = {
    # Dials
    'dial __color1':        ['__color dial', '__color καντράν', 0],
    'numerals __color0':    ['white numerals', '__color αρίθμηση', 0],
    # Hands
    'hand __color1':        ['__color','__color', 0],
    'hand up, __color1':    ['__color','__color', 0],
    'hand down, __color1':  ['__color','__color', 0],
    # Clasp
    'clasp __color1':       ['__color','__color', 0],
    # Pin
    'pin __color1':         ['__color','__color', 0],
    # Clean if nothing
    " ":                    ["__clear", "__clear", 0]
}

parts_material = {
    'STEEL':            ['stainless steel,','ανοξείδωτο ατσάλι,', 0],
    'S.S':              ['stainless steel,','ανοξείδωτο ατσάλι,', 0],
    '__color1 gold':    ['__color gold', '__color χρυσό', 0],
    " ":                ["__clear", "__clear", 0]
}


COLUMN_TRANSF_RULES['ΑΝΤΑΛΛΑΚΤΙΚΑ'] = {}
COLUMN_TRANSF_RULES['ΑΝΤΑΛΛΑΚΤΙΚΑ']['ΧΡΩΜΑ'] = parts_color
COLUMN_TRANSF_RULES['ΑΝΤΑΛΛΑΚΤΙΚΑ']['ΥΛΙΚΟ'] = parts_material

# ΑΝΤΑΛΛΑΚΤΙΚΑ
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# ΛΟΥΡΑΚΙΑ

straps_color = {
    "__color1": ['__color', '__color', 0],
    " ":        ["__clear", "__clear", 0]
}

straps_material = {
    "alligator":    ['Mississippi alligator matte skin', 'δέρμα αλιγάτορα Mississippi ματ', 1],
    "croco":        ['Luisiana crocodile matte skin', 'δέρμα κροκοδείλου Louisiana ματ', 1],
    "croc imit":    ['Louisiana crocodile matte skin impression', 'δέρμα κροκοδείλου Louisiana ματ, σταμπαριστό', 1],
    # " ":            ['__stop', '__stop', 1],
    "lizard":       ['lizard leather', 'δέρμα σαύρας', 1],
    "CAOUTCHOUC":   ['Rubber', 'Καουτσούκ', 1],
    "ostrich":      ['ostrich leather', 'δέρμα στρουθοκάμηλου', 1],
    "toro":         ['toro', 'toro', 1],
    "galant":       ['galant', 'galant', 1],
    "calf":         ['calf', 'calf', 1],
    "nato":         ['nato', 'νατο', 1],
    "ravena":       ['ravena', 'δερμάτινο ραβένα', 1],
    # " ":            ['__stop', '__stop', 3],
    "bracelet":     ['stainless steel','ανοξείδωτο ατσάλι', 1],
    "yellow gold plated steel": ["Yellow gold plated steel", "Ανοξείδωτο ατσάλι με χρυσή επίστρωση", 1],
    'STEEL':        ['stainless steel','ανοξείδωτο ατσάλι', 1],
    'S.S':          ['stainless steel','ανοξείδωτο ατσάλι', 1]
}

COLUMN_TRANSF_RULES['ΛΟΥΡΑΚΙΑ'] = {}
COLUMN_TRANSF_RULES['ΛΟΥΡΑΚΙΑ']['ΧΡΩΜΑ'] = straps_color
COLUMN_TRANSF_RULES['ΛΟΥΡΑΚΙΑ']['ΥΛΙΚΟ'] = straps_material
COLUMN_TRANSF_RULES['ΛΟΥΡΑΚΙΑ']['ΔΙΑΣΤΑΣΕΙΣ'] = {}

# Extra
straps_type = {
    'bracelet':   ['bracelet ', 'μπρασελέ ', 0],
    ' ':          ['strap ','λουράκι από ', 0]
}

straps_clasp_type = {
    'folding':   ['folding buckle', 'αναδιπλώμενο κούμπωμα', 0],
    'butterfly': ['folding buckle', 'αναδιπλώμενο κούμπωμα', 0],
    'buckle':    ['Buckle','τοκά', 0],
}

straps_clasp_material = {
    'yellow gold plated': ['yellow gold plated ', 'επιχρυσομένο ',0],
    "__*":      ["__clear","__clear",0]
}

straps_material_names = {
    "alligator":    ['alligator', 'δέρμα Αλιγάτορα', 1],
    "croco":        ['croco', 'δέρμα Κροκοδείλου', 1],
    "croc imit":    ['croco', 'δέρμα Κροκοδείλου', 1],
    # " ":            ['__stop', '__stop', 1],
    "lizard":       ['lizard', 'δέρμα Σαύρας', 1],
    "CAOUTCHOUC":   ['Rubber', 'Καουτσούκ', 1],
    "ostrich":      ['ostrich', 'δέρμα Στρουθοκάμηλου', 1],
    "toro":         ['toro', 'δέρμα Toro', 1],
    "galant":       ['galant', 'δέρμα Galant', 1],
    "calf":         ['calf', 'δέρμα Calf', 1],
    "nato":         ['nato', 'Νατο', 1],
    "ravena":       ['ravena', 'δερμάτινο Ραβένα', 1],
    # " ":            ['__stop', '__stop', 3],
    'gold plated':  ['gold plated steel', 'επιχρυσωμένο ατσάλι',1],
    'STEEL':        ['steel','ατσάλι', 1],
    'S.S':          ['steel','ατσάλι', 1],
    "bracelet":     ['steel','ατσάλι', 1]
}

COLUMN_TRANSF_RULES['ΛΟΥΡΑΚΙΑ']['strap type'] = straps_type
COLUMN_TRANSF_RULES['ΛΟΥΡΑΚΙΑ']['clasp type'] = straps_clasp_type
COLUMN_TRANSF_RULES['ΛΟΥΡΑΚΙΑ']['clasp material'] = straps_clasp_material
COLUMN_TRANSF_RULES['ΛΟΥΡΑΚΙΑ']['name material'] = straps_material_names

# ΛΟΥΡΑΚΙΑ
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# ΚΟΣΜΗΜΑΤΑ/ΑΞΕΣΟΥΑΡ (JOS VON ARX)

accessorys_color = {
    "__color1": ['__color', '__color', 0],
    " ":        ["__clear", "__clear", 0]
}

accessorys_material = {
    'italian bovine leather':       ['genuine italian bovine leather,', 'αυθεντικό ιταλικό δέρμα,',   0],
    'italian leather':              ['genuine italian leather,',        'αυθεντικό ιταλικό δέρμα,',   0],
    'leather':                      ['leather,',                        'δέρμα,',                     0],
    'solid brass with pvd plating': ['solid brass with pvd plating',    'επιπλατινωμένος ορείχαλκος', 1],
    'solid brass':                  ['solid brass',                     'ορείχαλκος',                 1],
    'steel':                        ['stainless steel',                 'ανοξείδωτο ατσάλι',          1],
    's.s':                          ['stainless steel',                 'ανοξείδωτο ατσάλι',          1],
    'PVD __color0':                 ['PVD __color,',                    'με __color επίστρωση,',      2]
}

accessorys_material_name = {
    'leather':                      ['leather',                      'δερμάτινο',                1],
    'solid brass with pvd plating': ['solid brass with PVD plating', 'επιπλατινωμένο ορείχαλκο', 1]
}

accessorys_warranty = {
    '1':      ['1',     '1',      0],
    '2':      ['2',     '2',      0],
    'year':   ['year',  'χρόνος', 1],
    'years':  ['years', 'χρόνια', 1]
}

accessorys_gift_pack = {
    'yes': ['yes', 'ναι', 0],
    'no':  ['no',  'όχι', 0]    
}

accessorys_gender = {'women': ['Ladies', 'Γυναικείο', 0], # must search for 'women' first
                     'men':   ['Gents',  'Ανδρικό',   0]}

COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']                     = {}
COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']['ΧΡΩΜΑ']            = accessorys_color
COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']['ΥΛΙΚΟ']            = accessorys_material
COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']['name_material']    = accessorys_material_name
COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']['ΕΓΓΥΗΣΗ']          = accessorys_warranty
COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']['ΣΥΣΚΕΥΑΣΙΑ ΔΩΡΟΥ'] = accessorys_gift_pack
COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']['gender']           = accessorys_gender

COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ ΑΝΔΡΙΚΑ ΒΡΑΧΙΟΛΙΑ']          = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']
COLUMN_TRANSF_RULES['ΑΞΕΣΟΥΑΡ ΣΤΥΛΟ ΠΕΝΕΣ']                 = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']
COLUMN_TRANSF_RULES['ΑΞΕΣΟΥΑΡ ΔΕΡΜΑΤΙΝΑ ΠΟΡΤΟΦΟΛΙΑ']        = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']
COLUMN_TRANSF_RULES['ΑΞΕΣΟΥΑΡ ΔΕΡΜΑΤΙΝΕΣ ΘΗΚΕΣ ΓΙΑ ΚΑΡΤΕΣ'] = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']
COLUMN_TRANSF_RULES['ΑΞΕΣΟΥΑΡ ΜΑΝΙΚΕΤΟΚΟΥΜΠΑ']              = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']
COLUMN_TRANSF_RULES['ΑΞΕΣΟΥΑΡ ΣΕΤ ΔΩΡΩΝ']                   = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']
COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ ΑΝΔΡΙΚΑ ΚΟΛΙΕ-ΣΤΑΥΡΟΣ']      = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ']
COLUMN_TRANSF_RULES['ΑΞΕΣΟΥΑΡ ΚΛΕΙΔΟΘΗΚΕΣ']                 = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ'] 
COLUMN_TRANSF_RULES['ΑΞΕΣΟΥΑΡ ΧΡΗΜΑΤΟΠΙΑΣΤΡΕΣ']             = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ'] 
COLUMN_TRANSF_RULES['ΑΞΕΣΟΥΑΡ ΓΡΑΒΑΤΟΠΙΑΣΤΡΕΣ']             = COLUMN_TRANSF_RULES['ΚΟΣΜΗΜΑΤΑ'] 
