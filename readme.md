## Exploring ELF format

I was curious about what exactly our executables contain and why it is not just
an executable code itself, but a bit complex, well designed format.

I think explaining every single line in my code with comments would be rather
distracting than useful. You can just look at raw bytes and not to dive into
details, but if you want to, you can always read the specification.

Each python script creates an ELF object byte-by-byte, either executable or
relocatable. To build relocatable objects at once you can use `build-rel.sh`
script.

It was not intended to be well-written x86 assembly programs, consider
it as necessary payload so we can see the result, besides looking at `readelf`
and `objdump` outputs.

## Files

### `exec-tiny.py`

Smallest possible ([excluding ways in which internal structures overlap](https://www.muppetlabs.com/~breadbox/software/tiny/teensy.html))
executable that just does exit(0).

### `exec-hello-world.py`

Simple yet complete hello world program.

### `rel-*.py`

Relocatable objects that should be linked together by the linker. Here
`rel-swap-n-print` uses functions `swapcase` from `rel-swapcase` and `println`
from `rel-println`. It prints a string, swaps the letter case in it and prints it
again.

## Useful links

  - System V ABI (common): https://www.sco.com/developers/gabi/latest/contents.html
  - System V ABI (x86-64 specific): https://www.uclibc.org/docs/psABI-x86_64.pdf
