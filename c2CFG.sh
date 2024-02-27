#!/bin/bash

cd "$1" || exit

mkdir -p llvm-ir
mkdir -p output

for var in *.c; do
    clang -S -emit-llvm "$var" -o llvm-ir/"${var: : -2}.ll" -w
    cd llvm-ir
    opt -dot-cfg -disable-output "${var: : -2}.ll"
    
    
    dot -Tpng -o ../output/"${var: : -2}.png" ".main.dot"
    dot -Tpdf -o ../output/"${var: : -2}.pdf" ".main.dot"
    pwd
    
    rm .*.dot
    cd ..
done
