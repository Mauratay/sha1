#!/usr/bin/env python2
import hashlib

raw_password = 'password'
raw_salt = 'salt'

print "-----Hex decoded-----"
print hashlib.sha1( raw_password + raw_salt ).hexdigest().upper().decode("hex").encode("base64")

print "-----Not Hex decoded-----"
print hashlib.sha1( raw_password + raw_salt ).hexdigest().encode("base64")


