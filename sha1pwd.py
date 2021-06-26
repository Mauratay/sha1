#!/usr/bin/env python3
import codecs
import hashlib, uuid
import base64

def hashing(word):
    digest = hashlib.sha1(word.encode('utf-8')).digest()
    return base64.b64encode(digest)

raw_salt='salt'
password=hashing('password'+raw_salt)
salt=base64.b64encode(bytes(raw_salt, 'utf-8'))

print(f"Salt: {salt} \nPassword: {password}")


def hashalone(word):
    digest = hashlib.sha1(word.encode('utf-8')).hexdigest() # <- hexdigest is the culprit 
    return digest

def hashafterb654(hash_):
    encoded=base64.b64encode(bytes(hash_, 'utf-8'))
    return encoded

hashalone = hashalone('passwordsalt')
encoded_hash = hashafterb654(hashalone)
hash_caps = hashafterb654(hashalone.upper())

print(f"Hash alone: {hashalone} \nHash not hex encoded before base64 encoding: {encoded_hash} \nHash not hex encoded before base64 all caps: {hash_caps}")


decode_hex = codecs.getdecoder("hex_codec")
test1= decode_hex(hashalone)[0]
test1 = base64.b64encode(test1)
print(f"This is the hash hex decoded: {test1}")

