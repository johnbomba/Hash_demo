#!/usr/bin/env python3

import hashlib
import sys

#usage hasher.py <string>
if len(sys.argv) != 2:
    print("Usage: hash_this.py <string>")
    sys.exit(0)

def hash_this():
    pw  = sys.argv[1]
    print(pw)
    pw = pw.rstrip()
    pw = bytes(pw, 'utf-8')

    pw_md = hashlib.md5(pw)
    pw_md = pw_md.hexdigest()
    print(f'sha 1: {pw_md}')
    print(sys.getsizeof(pw_md)) #sys.getsizeof(object[, default]) Return the size of an object in bytes.

    pw_sha1 = hashlib.sha1(pw)
    pw_sha1 = pw_sha1.hexdigest()
    print(f'md5: {pw_sha1}')
    print(sys.getsizeof(pw_sha1))

    pw_sha3 = hashlib.sha3_512(pw)
    pw_sha3 = pw_sha3.hexdigest()
    print(f'sha3-512: {pw_sha3}')
    print(sys.getsizeof(pw_sha3))

    pw_blake2b = hashlib.blake2b(pw)
    pw_blake2b = pw_blake2b.hexdigest()
    print(f'blake2b: {pw_blake2b}')
    print(sys.getsizeof(pw_blake2b))


if __name__ == '__main__':
    hash_this()


#sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s(). md5()