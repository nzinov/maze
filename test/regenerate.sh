#!/bin/sh
cd test/
run=0
for file in *.test
do
    echo "Processing $file"
    let "run += 1"
    if python3 regenerate_test.py $file
    then
        mv $file.new $file
    fi
done
echo "Processed $run"
