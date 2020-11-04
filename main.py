#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ecdsa import VerifyingKey, SECP256k1
import hashlib, random, binascii, argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--request', '-r',default='error')
    parser.add_argument ('--UID', '-u',default='error')
    parser.add_argument ('--IPFS', '-i',default='error')
    parser.add_argument ('--sign', '-s',default='error')

    return parser
 

def set_mode(U_ID, _IPFS, _sign):
    (name, pub_key) = U_ID.split(":")

    pk = VerifyingKey.from_string(bytes.fromhex(pub_key), curve=SECP256k1)
    sign = binascii.unhexlify(_sign)
    IPFS = bytes(_IPFS, 'utf-8')
    if pk.verify(sign, IPFS):
        write_verified(name, pub_key, _IPFS)
    else:
        print('Wrong signature or public key!')

def write_verified(name, pk, link):
    storage = open("storage.md", "w")
    storage.write(name + ":" + pk + ":" + link)
    storage.close()

def get_mode(U_ID):
    storage = open("storage.md", "r")
    print(*storage)
    storage.close()

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
 
    #print (namespace)
 
    if namespace.request == 'get':
        get_mode(namespace.UID)
    elif namespace.request == 'set':
        set_mode(namespace.UID, namespace.IPFS, namespace.sign)    
    else:
        print("wrong input")

