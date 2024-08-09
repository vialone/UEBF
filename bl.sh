#!/bin/bash

# This is a wrapper to run the bootloader for Unified Extensible Binary Format (UEBF) images.
# It is intended to be used as alternative to the ELF format.

python3 /usr/lib/uebf/bl.py $@
