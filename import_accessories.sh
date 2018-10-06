#!/bin/sh

SPECS_CSV="input/accessories_stock - specs_tsv.tsv"

./accessories.py "$SPECS_CSV" $1
