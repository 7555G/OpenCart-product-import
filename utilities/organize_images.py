#!/usr/bin/env python

from check_images import *
from os.path import join
from PIL import Image

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
            image = Image.open(associated_image)
            image.load()
            
            # if max(image.height, image.width) > 800:
            factor = float(800 / max(image.width, image.height))
            resized_image = image.resize((int(factor * image.width), int(factor * image.height)), Image.BICUBIC)
            resized_image = resized_image.convert('RGBA')

            background = Image.new("RGBA", resized_image.size, (255, 255, 255))
            background.paste(resized_image, mask=resized_image.split()[3]) # 3 is the alpha channel
            
            image = background.convert('RGB')
            image.save(join(output_path, product_id + ".jpg"), "JPEG", quality=95, optimizer=True)

            # copyfile(associated_image, join(output_path, product_id + ".jpg"), "JPEG", optimizer=True)
        else:
            print(str(product_id) + ": No image found!")
            missing+=1

    print("We are missing: ", missing)

