#!/usr/bin/env python3

import hashlib
import sys

#usage hasher.py <file>
if len(sys.argv) != 2:
    print("Usage: md_hasher.py <file>")
    sys.exit(0)

def md_this():
    pw_file = sys.argv[1]

    with open(pw_file) as f:
        for x in f:
            x = x.rstrip()
            x = bytes(x, 'utf-8')
            y = hashlib.md5(x)
            z = y.hexdigest()
            write_file(z)

def write_file(z):
    with open('md_hashes.txt', 'a') as out:
        out.write(z + '\n')
        out.closed

if __name__ == '__main__':
    md_this()