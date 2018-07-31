#!/usr/bin/env python

COLUMN_TRANSF_RULES = {}    # { 'ΚΑΣΑ': {'S.STEEL':'Ατσαλι'}}

# Now define the transformation dictionaries for each column

# ΡΟΛΟΓΙΑ
watches_kasa = { 
         'STEEL':       ['stainless steel','ανοξείδωτο ατσάλι', 0],
         'S.S':         ['stainless steel','ανοξείδωτο ατσάλι', 0],
         'Ceramic':     ['ceramic', 'κεραμικό', 1],
         'IP Rose Gold':['IP rose gold','με ρωζ χρυσή επίστρωση', 2],
         'IP Pink Gold':['IP pink gold','με ρωζ χρυσή επίστρωση', 2],
         'IP silver':   ['IP yellow','με ασημένια επίστρωση', 2],
         'IP Gold':     ['IP gold','με χρυσή επίστρωση', 2],
         'IP Red':      ['IP red','με κόκκινη επίστρωση', 2],
         'IP Green':    ['IP green','με πράσινη επίστρωση', 2],
         'IP black':    ['IP black','με μαύρη επίστρωση', 2],
         'IP yellow':   ['IP yellow','με κίτρινη επίστρωση', 2],
         'IP purple':   ['IP yellow','με μωβ επίστρωση', 2],
         'IP orange':   ['IP yellow','με πορτοκαλί επίστρωση', 2],
         'IP light blue':   ['IP yellow','με γαλάζια επίστρωση', 2],
         'IP cyan':   ['IP yellow','με γαλάζια επίστρωση', 2],
         'IP brown':   ['IP yellow','με καφέ επίστρωση', 2],
         }

watches_waranty = { '2 years':  ['2 years', '2 χρόνια', 0]}

gender ={ 'mens':   ['Gents', 'Ανδρικό'],
          'womens': ['Ladies', 'Γυναικείο']}

watches_atm = { '3':    ['3atm', '3atm'],
                '5':    ['5atm', '5atm'],
                '10':   ['10atm','10atm']}
watches_mech = {}

watches_bezel = { 
         'STEEL':       ['stainless steel','ανοξείδωτο ατσάλι', 1],
         'S.S':         ['stainless steel','ανοξείδωτο ατσάλι', 1],
         'Ceramic':     ['ceramic', 'κεραμικό', 0],
         'IP Rose Gold':['IP rose gold','με ρωζ χρυσή επίστρωση', 2],
         'IP Pink Gold':['IP pink gold','με ρωζ χρυσή επίστρωση', 2],
         'IP silver':   ['IP yellow','με ασημένια επίστρωση', 2],
         'IP Gold':     ['IP gold','με χρυσή επίστρωση', 2],
         'IP Red':      ['IP red','με κόκκινη επίστρωση', 2],
         'IP Green':    ['IP green','με πράσινη επίστρωση', 2],
         'IP black':    ['IP black','με μαύρη επίστρωση', 2],
         'IP yellow':   ['IP yellow','με κίτρινη επίστρωση', 2],
         'IP purple':   ['IP yellow','με μωβ επίστρωση', 2],
         'IP orange':   ['IP yellow','με πορτοκαλί επίστρωση', 2],
         'IP light blue':   ['IP yellow','με γαλάζια επίστρωση', 2],
         'IP cyan':   ['IP yellow','με γαλάζια επίστρωση', 2],
         'IP brown':   ['IP yellow','με καφέ επίστρωση', 2],
         }


watches_glass = {
    'Sapphire': ['Sapphire','Ζαφείρι'],
    'Glass' :   ['Mineral glass', 'Κρύσταλλο']
}

watches_strap_material = {}

COLUMN_TRANSF_RULES = {'ΡΟΛΟΓΙΑ':{ 'ΚΑΣΑ':watches_kasa,
                                    'ΕΓΓΥΗΣΗ':watches_waranty,
                                    'ΑΔΙΑΒΡΟΧΟ':watches_atm,
                                    'ΣΤΕΦΑΝΗ':bezel,
                                    'ΜΗΧΑΝΙΣΜΟΣ':watches_mech,
                                    'ΦΥΛΟ':gender
                                    'ΚΡΥΤΑΛΛΟ':watches_glass,
                                    'ΥΛΙΚΟ ΔΕΣΙΜΑΤΟΣ':watch_strap_material
                                  }
                      }