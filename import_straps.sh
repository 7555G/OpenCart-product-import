#!/bin/sh

SPECS_CSV="input/straps_stock - specs_tsv.tsv"

./straps.py "$SPECS_CSV" $1
