#!/bin/bash

target_script=$1
target_file=$2

if test -f "$target_file"; then
    while :; do 
        inotifywait -e modify $target_file
        python3 $target_script $target_file
    done
else
    echo "Target file path provided is not valid: ${target_file}"
    exit
fi
