#!/usr/bin/env bash
set -e

mkdir -p bin

python3 exec/hello-world.py
python3 exec/tiny.py

python3 rel/println.py
python3 rel/swap-n-print.py
python3 rel/swapcase.py

chmod +x bin/exec-hello-world
chmod +x bin/exec-tiny
ld -o bin/exec-swap-n-print \
    bin/rel-swap-n-print.o bin/rel-println.o bin/rel-swapcase.o
