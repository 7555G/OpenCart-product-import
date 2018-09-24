#!/bin/sh

# arg1: output.xlsx | arg2: initial.xlsx
clean_file="xlsx_files/clean.xlsx"
if [ $# -eq 1 ]
then
    clean_file = $2
fi

excel_file="xlsx_files/products.xlsx"
if [ $# -eq 2 ] 
then
    excel_file=$1
fi


files=$(ls import*.sh)

# Clean up the excel file
echo "Cleaning up the excel: $excel_file"
rm "$excel_file"
cp "$clean_file" "$excel_file"

# Run each import script
for i in $files; do
    echo ""
    echo "Running $i"
    ./$i "$excel_file"
done
