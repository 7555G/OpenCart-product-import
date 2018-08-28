#!/bin/sh

# If argument is given then use that excel
excel_file="xlsx_files/products.xlsx"
if [ $# -eq 1 ] 
then
    excel_file=$1
fi

files=$(ls import*.sh)

# Clean up the excel file
echo "Cleaning up the excel: $excel_file"
rm "$excel_file"
cp xlsx_files/clean.xlsx "$excel_file"

# Run each import script
for i in $files; do
    echo ""
    echo "Running $i"
    ./$i "$excel_file"
done
