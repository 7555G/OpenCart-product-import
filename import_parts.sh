#!/bin/sh

SPECS_CSV="input/parts_stock - specs_tsv.tsv"

./parts.py "$SPECS_CSV" $1
