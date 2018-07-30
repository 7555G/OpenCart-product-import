# OpenCart-product-import
Scripts for multiple product importing through OpenCart xlsx files.


## Main scripts
* `get_stock.py [xlsx_file] [data_file] [specs_format_file]`: collects specs with defined format from an xlsx file of stock.

* `import_product.py [data_file] [xlsx_file]`: generates product entries
with given data from file.


## Utilities
* `image_checker.py [xlsx_file] [photos_dir]`: searches for photos of
products from a stock.xlsx file and returns their location if successful.
    for passwords from the xslx

* `image_organizer [xlsx_file] [search_dir] [output_dir]`: searches a
specified directory for images of products from a stock.xlsx (using
`image_checker.py`) and if successful it converts them to JPEG (TODO),
scales them down if necessary (TODO) and moves them to output directory.

* `create_categories_dict.py [xlsx_file]`: creates a dictionary that
maps the categories' names to their IDs from the specified xlsx file.

* `create_attributes_dict.py [xlsx_file]`: creates a dictionary that
maps *categories* to *attribute groups*, and a second that maps *attributes* to
*attribute groups*
