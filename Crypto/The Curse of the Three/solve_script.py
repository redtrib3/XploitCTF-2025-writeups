
from Crypto.Util.number import *
from Cryptodome.PublicKey import RSA
from gmpy2 import iroot

# from messages.txt
c = 161666437813793094113083864185510766762740926307980632461163761499821980453651667616604128704191791653304282794400203496612622477141951882347291838529153608524353442605661638797425571472693723556951238883375678057677926552782529637


def extract_n_e():
    with open("attachments/pubkey.pem", "rb") as f:
        key = RSA.import_key(f.read())
    print("n:", key.n)
    print("e:", key.e)


m, is_match = iroot(c, 3)
if is_match:
    print("[=] Successfully found Secret Message M.")
    print("[=] Message:", long_to_bytes(int(m)).decode())
