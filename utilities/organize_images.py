#!/usr/bin/env python

from image_checker import *
from os.path import join

if __name__ == "__main__":
    from shutil import copyfile

    if len(argv) < 3:
        print("Need 3 args. 1: xlsx file 2: photos search dir 3: output dir")
        exit()

    xlsx_file = argv[1]
    search_path = argv[2]
    output_path = argv[3]

    missing=0
    for product_id in get_ids(xlsx_file):
        associated_image = check_image_exists(product_id, search_path)
        if associated_image:
            print("Copied: " + associated_image)
            copyfile(associated_image, join(output_path, product_id + "." + associated_image.split(".")[-1]))
        else:
            print(str(product_id) + ": No image found!")
            missing+=1

    print("We are missing: ", missing)

