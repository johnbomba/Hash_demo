#!/usr/bin/env python3

import hashlib
import sys

#usage hasher.py <string> <string>
if len(sys.argv) != 3:
    print("Usage: hash_this.py <string> <string>")
    sys.exit(0)

def hash_this():
    pw  = sys.argv[1]
    pw2 = sys.argv[2]
    print(pw)
    print(pw2)
    convert_to_bytes(pw,pw2)

def convert_to_bytes(pw,pw2):
    pw = pw.rstrip()
    pw = bytes(pw, 'utf-8')
    pw2 = pw2.rstrip()
    pw2 = bytes(pw2, 'utf-8')
    md_hash(pw,pw2)
    sha_hash(pw,pw2)
    sha3_hash(pw,pw2)
    blake_hash(pw,pw2)

def md_hash(pw,pw2):
    pw_md = hashlib.md5(pw)
    pw_md = pw_md.hexdigest()
    print(f'sha 1: {pw_md}')
    print(sys.getsizeof(pw_md)) #sys.getsizeof(object[, default]) Return the size of an object in bytes.
    pw2_md = hashlib.md5(pw2)
    pw2_md = pw2_md.hexdigest()
    print(f'sha 1: {pw2_md}')
    print(sys.getsizeof(pw2_md)) #sys.getsizeof(object[, default]) Return the size of an object in bytes.

def sha_hash(pw,pw2):
    pw_sha1 = hashlib.sha1(pw)
    pw_sha1 = pw_sha1.hexdigest()
    print(f'md5: {pw_sha1}')
    print(sys.getsizeof(pw_sha1))
    pw2_sha1 = hashlib.sha1(pw2)
    pw2_sha1 = pw2_sha1.hexdigest()
    print(f'md5: {pw2_sha1}')
    print(sys.getsizeof(pw2_sha1))

def sha3_hash(pw,pw2):
    pw_sha3 = hashlib.sha3_512(pw)
    pw_sha3 = pw_sha3.hexdigest()
    print(f'sha3-512: {pw_sha3}')
    print(sys.getsizeof(pw_sha3))
    pw2_sha3 = hashlib.sha3_512(pw2)
    pw2_sha3 = pw2_sha3.hexdigest()
    print(f'sha3-512: {pw2_sha3}')
    print(sys.getsizeof(pw2_sha3))

def blake_hash(pw,pw2):
    pw_blake2b = hashlib.blake2b(pw)
    pw_blake2b = pw_blake2b.hexdigest()
    print(f'blake2b: {pw_blake2b}')
    print(sys.getsizeof(pw_blake2b))
    pw2_blake2b = hashlib.blake2b(pw2)
    pw2_blake2b = pw2_blake2b.hexdigest()
    print(f'blake2b: {pw2_blake2b}')
    print(sys.getsizeof(pw2_blake2b))


if __name__ == '__main__':
    hash_this()


#sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s(). md5()
