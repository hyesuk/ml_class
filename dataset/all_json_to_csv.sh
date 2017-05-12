#!/bin/bash
for json in `ls *.json`
do
    python ../json_to_csv_converter.py $json
done