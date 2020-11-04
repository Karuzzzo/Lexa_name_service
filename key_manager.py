from ecdsa import SigningKey, SECP256k1
import hashlib, random, binascii, argparse

def generate_pair():
    sk = SigningKey.generate(curve=SECP256k1)
    pk = sk.get_verifying_key()

    print("your pub key is :", pk.to_string().hex(), "\nyour secret key is :", sk.to_string().hex(),
    "\nWrite that data, or later you will not able to this pair!")

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--mode', '-m', default='gen')
    parser.add_argument ('--string_tosig', '-s', default='')
    parser.add_argument ('--secret_key', '-sk', default='')

    return parser

def sig_string(input, sec_key):
    input_b = bytes(input, 'utf-8')
    private_key = binascii.unhexlify(sec_key)
    priv = SigningKey.from_string(private_key, curve=SECP256k1)
    signature = priv.sign(input_b)
    print('Your signature is: ', signature.hex())

parser = createParser()
namespace = parser.parse_args()
 
if namespace.mode == 'gen':
    generate_pair()
elif namespace.mode == 'sign':
    sig_string(namespace.string_tosig, namespace.secret_key)  
else:
    print("wrong input")