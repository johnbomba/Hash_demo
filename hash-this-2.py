#!/usr/bin/env python3
import hashlib
import sys
def hash_this():
    pw  = sys.argv[1]
    print(pw)
    pw = pw.rstrip()
    pw = bytes(pw, 'utf-8')
    md_hash(pw)
    sha_hash(pw)
    sha3_hash(pw)
    blake(pw)
def md_hash(pw):
    pw_md = hashlib.md5(pw)
    pw_md = pw_md.hexdigest()
    print(f'md5: {pw_md}\n')
    # print(sys.getsizeof(pw_md)) #sys.getsizeof(object[, default]) Return the size of an object in bytes.
def sha_hash(pw):
    pw_sha1 = hashlib.sha1(pw)
    pw_sha1 = pw_sha1.hexdigest()
    print(f'sha1: {pw_sha1}\n')
    # print(sys.getsizeof(pw_sha1))
def sha3_hash(pw):
    pw_sha3 = hashlib.sha3_512(pw)
    pw_sha3 = pw_sha3.hexdigest()
    print(f'sha3-512: {pw_sha3}\n')
    # print(sys.getsizeof(pw_sha3))
def blake(pw):
    pw_blake2b = hashlib.blake2b(pw)
    pw_blake2b = pw_blake2b.hexdigest()
    print(f'blake2b: {pw_blake2b}\n')
    # print(sys.getsizeof(pw_blake2b))
if __name__ == '__main__':
    #usage hasher.py <string>
    if len(sys.argv) != 2:
      print("Usage: hash_this.py <string>")
      sys.exit(0)
    else:
      hash_this()
#sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s(). md5() (edited) 
