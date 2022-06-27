#!/usr/bin/env bash

fallback_budget="500 EUR"
declare budget
if [[ -z $@ ]]; then
    echo -e "WARNING:\tusing fallback budget of ${fallback_budget}"
    budget=$fallback_budget
else
    budget=$1
fi


d=$(date +%Y-%m-01)
month_name=$(date +%B)
# open budget account
ast=$(echo '*')
accounts_string="${d} *Opening Budget account ${month_name} \n\tAssets:Budget:${month_name}\t${budget}\n\tEquity:Budget"

echo -e $accounts_string >> "/home/velo/Documents/Me/Finance/my.ledger"
