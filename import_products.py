#!/usr/bin/env python

from sys import argv
from pprint import pprint
from openpyxl import Workbook, load_workbook

# Global Data
products_xlsx = ''
categories_dict = {}

MODEL_INDX  = 0
MANUF_INDX  = 1
CATEG_INDX  = 2
COLLEC_INDX = 3
FAMILY_INDX = 4
GENDER_INDX = 5
PRICE_INDX  = 6
ATTRIBUTE_GROUP = 'ΡΟΛΟΓΙΑ'
MANUFACTURER = ['Chronoswiss',
                'Fortis',
                'Jos Von Arx',
                'Jowissa',
                'Manfred Cracco',
                'Rodania',
                'Victorinox']
ATTRIBUTE = ['ΦΥΛΟ',
             'ΣΥΛΛΟΓΗ',
             'ΜΗΧΑΝΙΣΜΟΣ',
             'ΛΕΙΤΟΥΡΓΙΕΣ',
             'ΚΑΣΑ',
             'ΔΙΑΜΜΕΤΡΟΣ ΚΑΣΑΣ',
             'ΠΑΧΟΣ ΚΑΣΑΣ',
             'ΚΡΥΣΤΑΛΛΟ',
             'ΚΑΠΑΚΙ',
             'ΣΤΕΦΑΝΗ',
             'ΥΛΙΚΟ ΔΕΣΙΜΑΤΟΣ',
             'ΚΟΥΜΠΩΜΑ',
             'ΑΔΙΑΒΡΟΧΟ',
             'ΕΓΓΥΗΣΗ']
DEFAULT_ATTR = ['n',
                'o',
                't',
                'h',
                'i',
                'n',
                'g',
                ' ',
                't',
                'o',
                ' ',
                's',
                'e',
                'e']


def open_new_products(input_file):
    new_products = open(input_file)
    new_products = [line.replace('\n','') for line in new_products]

    # Remove commas and trim spaces
    new_products = [line.split(',') for line in new_products]

    for product in range(len(new_products)):
        for entry in range(len(new_products[product])):
            new_products[product][entry] = \
                                        new_products[product][entry].strip()

    # Format data
    for product in range(len(new_products)):
        # Manufacturer
        new_products[product][MANUF_INDX] = \
                                   new_products[product][MANUF_INDX].title()
        # Category
        new_products[product][CATEG_INDX] = \
                          new_products[product][CATEG_INDX].replace(' ', '')
        new_products[product][CATEG_INDX] = \
                                   new_products[product][CATEG_INDX].upper()
        # Gender
        new_products[product][GENDER_INDX] = \
                                  new_products[product][GENDER_INDX].lower()
        # Price
        new_products[product][PRICE_INDX] = \
                                      int(new_products[product][PRICE_INDX])
    
    return new_products

def load_categories():
    import pickle

    with open('categories.pkl', 'rb') as f:
        return pickle.load(f)

# XLSX modifier funcions
def add_empty_product(wb):
    products_sheet = wb["Products"]
    products_sheet.append(['' for i in range(products_sheet.max_column)])
    row_num = products_sheet.max_row
   
    # Write the new product code
    last_product_id = products_sheet['A' + str(row_num - 1)].value
    curr_product_id = last_product_id + 1
    products_sheet['A' + str(row_num)] = curr_product_id

    print('Insert new product with ID ' + str(curr_product_id) \
          + ' in row ' + str(row_num) + '.')


def add_product_name(product_info, wb):
    products_sheet = wb["Products"]
    row_num = products_sheet.max_row

    # Create product name
    product_name = product_info[MANUF_INDX]  + ' ' \
                 + product_info[COLLEC_INDX]
    if product_info[FAMILY_INDX] != '':
        product_name += product_info[FAMILY_INDX] + ' '
    product_name += product_info[MODEL_INDX]

    # Write product name
    products_sheet['B' + str(row_num)] = product_name
    products_sheet['C' + str(row_num)] = product_name

def add_description(product_info, wb):
    products_sheet = wb["Products"]
    row_num = products_sheet.max_row

    # Define gender
    if product_info[GENDER_INDX] == 'mens':
        gender_en = 'mens'
        gender_el = 'ανδρικό'
    elif product_info[GENDER_INDX] == 'womens':
        gender_en = 'womens'
        gender_el = 'γυναικείο'

    # Greek
    descr_el = 'Κομψό ' + gender_el + ' ρολόι από την εταιρία ' \
             + product_info[MANUF_INDX] \
             + ', Ελβετικής κασκευής, από τη συλλογή ' \
             + product_info[COLLEC_INDX] 
    if product_info[FAMILY_INDX] != '':
        # Family could be empty
        descr_el += ' ' + product_info[FAMILY_INDX]
    descr_el += ', με κωδικό ' + product_info[MODEL_INDX] + '.'

    # English
    descr_en = 'An elegant ' + gender_en + ' watch by ' \
             + product_info[MANUF_INDX] \
             + ', Swiss made, from the collection ' \
             + product_info[COLLEC_INDX] 
    if product_info[FAMILY_INDX] != '':
        # Family could be empty
        descr_en += ' ' + product_info[FAMILY_INDX]
    descr_en += ', with reference ' + product_info[MODEL_INDX] + '.'

    # Write description
    products_sheet['AE' + str(row_num)] = '<p>' + descr_el + '</p>'
    products_sheet['AF' + str(row_num)] = '<p>' + descr_en + '</p>'

    # Write meta description
    products_sheet['AI' + str(row_num)] = descr_el
    products_sheet['AJ' + str(row_num)] = descr_en


def add_SEO(product_info, wb):
    products_sheet = wb["Products"]
    row_num = products_sheet.max_row

    # Create SEO
    SEO = product_info[MANUF_INDX].replace(' ', '_') + '-' \
        + product_info[COLLEC_INDX].replace(' ', '_') + '-'
    if product_info[FAMILY_INDX] != '':
        SEO += product_info[FAMILY_INDX].replace(' ', '_') + '-'
    SEO += product_info[MODEL_INDX].replace(' ', '_')

    # Write SEO
    products_sheet['AD' + str(row_num)] = SEO


def add_model(product_info, wb):
    products_sheet = wb["Products"]
    row_num = products_sheet.max_row

    # Get model
    model = product_info[MODEL_INDX]

    # Write model
    products_sheet['M' + str(row_num)] = model


def add_meta_title(product_info, wb):
    products_sheet = wb["Products"]
    row_num = products_sheet.max_row

    # Define gender
    if product_info[GENDER_INDX] == 'mens':
        gender_en = 'Mens'
        gender_el = 'Ανδρικό'
    elif product_info[GENDER_INDX] == 'womens':
        gender_en = 'Womens'
        gender_el = 'Γυναικείο'

    # Greek
    if product_info[FAMILY_INDX] != '':
        meta_title_el_m = gender_el + ' Ελβετικό ρολόι - ' \
                        + product_info[MANUF_INDX]  + ' ' \
                        + product_info[FAMILY_INDX] + ' ' \
                        + product_info[MODEL_INDX]  + ' | Eurotimer'
        meta_title_el_l = gender_el + ' Ελβετικό ρολόι - ' \
                        + product_info[MANUF_INDX]  + ' ' \
                        + product_info[COLLEC_INDX] + ' ' \
                        + product_info[FAMILY_INDX] + ' ' \
                        + product_info[MODEL_INDX]  + ' | Eurotimer'
    else:
        meta_title_el_m = gender_el + ' Ελβετικό ρολόι - ' \
                        + product_info[MANUF_INDX]  + ' ' \
                        + product_info[COLLEC_INDX] + ' ' \
                        + product_info[MODEL_INDX]  + ' | Eurotimer'
        meta_title_el_l = meta_title_el_m
    meta_title_el_s = gender_el + ' Ελβετικό ρολόι - ' \
                    + product_info[MANUF_INDX] + ' ' \
                    + product_info[MODEL_INDX] + ' | Eurotimer'
    
    # English
    if product_info[FAMILY_INDX] != '':
        meta_title_en_m = gender_en + ' Watches - Swiss Made ' \
                        + product_info[MANUF_INDX]  + ' ' \
                        + product_info[FAMILY_INDX] + ' ' \
                        + product_info[MODEL_INDX]  + ' | Eurotimer'
        meta_title_en_l = gender_en + ' Watches - Swiss Made ' \
                        + product_info[MANUF_INDX]  + ' ' \
                        + product_info[COLLEC_INDX] + ' ' \
                        + product_info[FAMILY_INDX] + ' ' \
                        + product_info[MODEL_INDX]  + ' | Eurotimer'
    else:
        meta_title_en_m = gender_en + ' Watches - Swiss Made ' \
                        + product_info[MANUF_INDX]  + ' ' \
                        + product_info[COLLEC_INDX] + ' ' \
                        + product_info[MODEL_INDX]  + ' | Eurotimer'
        meta_title_en_l = meta_title_en_m
    meta_title_en_s = gender_en + ' Watches - Swiss Made ' \
                    + product_info[MANUF_INDX] + ' ' \
                    + product_info[MODEL_INDX] + ' | Eurotimer'

    # Select meta title with appropriate length
    if len(meta_title_el_l) <= 60:
        meta_title_el = meta_title_el_l
    elif len(meta_title_el_m) <= 60:
        meta_title_el = meta_title_el_m
    elif len(meta_title_el_s) <= 60:
        meta_title_el = meta_title_el_s
    else:
        print("Warning: Greek meta title is longer than 60 characters!")
        meta_title_el = ''

    if len(meta_title_en_l) <= 60:
        meta_title_en = meta_title_en_l
    elif len(meta_title_en_m) <= 60:
        meta_title_en = meta_title_en_m
    elif len(meta_title_en_s) <= 60:
        meta_title_en = meta_title_en_s
    else:
        print("Warning: English meta title is longer than 60 characters!")
        meta_title_en = ''

    # Wrte meta titles
    products_sheet['AG' + str(row_num)] = meta_title_el
    products_sheet['AH' + str(row_num)] = meta_title_en


def add_price(product_info, wb):
    products_sheet = wb["Products"]
    row_num = products_sheet.max_row

    # Get price
    price = product_info[PRICE_INDX]

    # Write price
    products_sheet['Q' + str(row_num)] = price


def add_manufacturer(product_info, wb):
    products_sheet = wb["Products"]
    row_num = products_sheet.max_row

    # Check manufacturer
    manuf = ''
    for correct_manuf in MANUFACTURER:
        if product_info[MANUF_INDX]== correct_manuf:
            manuf = product_info[MANUF_INDX]
    if manuf == '':
        print("Warning: invalid manufacturer name!")

    # Write manufacturer
    products_sheet['N' + str(row_num)] = manuf


def add_category(product_info, wb):
    products_sheet = wb["Products"]
    row_num = products_sheet.max_row

    # Find category number from dictionary
    categ = categories_dict[product_info[CATEG_INDX]]
    if categ == '':
        print("Warning: invalid category!")

    # Write category number
    products_sheet['D' + str(row_num)] = categ


def add_attributes(product_info, wb):
    products_sheet = wb[""]
    row_num = products_sheet.max_row



if __name__ == '__main__':

    if len(argv) != 3:
        print('arg1: input_file, arg2: products.xlsx')
        exit(1)

    input_file = argv[1]
    products_xlsx = argv[2]

    wb = load_workbook(products_xlsx)
    new_products = open_new_products(input_file)
    categories_dict = load_categories()
    pprint(new_products)

    # Iterate the inputs
    for product in new_products:
        add_empty_product(wb)
        add_product_name(product, wb)
        add_description(product, wb)
        add_SEO(product, wb)
        add_model(product, wb)
        add_meta_title(product, wb)
        add_price(product, wb)
        add_manufacturer(product, wb)
        add_category(product, wb)

    # Save to file
    wb.save(products_xlsx)
