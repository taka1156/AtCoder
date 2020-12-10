#!/bin/sh

if [ "$1" = "abs" -a "$2" != "" ];
then 
    cp ./template/template.py ./ABS/ABS_"$2".py
elif [ "$1" = "apg4b" -a "$2" != "" ];
then 
    cp ./template/template.py ./APG4b/APG4b_EX"$2".py
else
    echo "例: [make.sh ABS|APG4b 086A]のように入力してください。"
fi
