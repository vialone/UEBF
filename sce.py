#!/usr/bin/env python3
# simple compiler example
# compiles a simple language to UEBF ELF wrapper

import sys

with open(sys.argv[1], 'rb') as f:
    code = f.read()

with open(sys.argv[2], 'wb') as f:
    f.write(b'#!/usr/lib/uebf/bl.sh\n')
    f.write(b'FMT/EBF\n')
    f.write(b'TYPE/ELFW\n')
    f.write(b'BL/ELF\n')
    f.write(b'---\n')
    f.write(code)
