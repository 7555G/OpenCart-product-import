#!/usr/bin/env python

COLUMN_TRANSF_RULES = {}    # { 'ΚΑΣΑ': {'S.STEEL':'Ατσαλι'}}

# Now define the transformation dictionaries for each column

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
                                
                      
