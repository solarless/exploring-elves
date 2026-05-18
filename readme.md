## Exploring ELF format

I was curious about what exactly our executables contain and why it is not just
an executable code itself, but complex, well designed format.

Each python script creates an ELF object byte-by-byte, either executable or
relocatable. To build them all at once you can use `build.sh` script.

It was not intended to be well-written x86 assembly programs, consider
them as inevitable payload so we can see the result, besides looking at
`readelf` and `objdump` output.

## Files

### `exec/tiny.py`

Smallest possible ([excluding ways in which some structures overlap](https://www.muppetlabs.com/~breadbox/software/tiny/teensy.html))
executable that just does exit(0).

### `exec/hello-world.py`

Simple yet complete hello world program.

### `rel/`

Relocatable objects that should be linked together by the linker. Here
`swap-n-print.py` uses functions `swapcase` from `swapcase.py` and `println`
from `println.py`. It prints a string, swaps the letter case in it and prints it
again.

## Useful links

  - System V ABI (common): https://www.sco.com/developers/gabi/latest/contents.html
  - System V ABI (x86-64 specific): https://www.uclibc.org/docs/psABI-x86_64.pdf
