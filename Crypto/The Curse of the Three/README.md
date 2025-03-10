# Crypto: The Curse of the Three

**Author**: [redtrib3](https://github.com/redtrib3)<br>
**Points**: 450<br>
**Hint 1 **: How do you find the exponent and modulus from a public key? (30 pts)<br>
**Hint 1 **: https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/rsa.pdf (70 pts)<br>
**Flag**: `xploit{thee_h0lds_th3_key_0xce5}`<br>

**Challenge description:**
```
My Three Best friends Shamir, Ron, and Leonard sent me a message, but it seems to be encrypted in a Random Secure algorithm i have no idea about.

The public key should be helpful, right...?
```

## Solve

The vulnerability in this rsa implementation is low public exponent AKA cube root attack.

#### Why Does the Attack Work?:

in RSA Cipher 'c' is generated by the formula: c = m^e mod n programmatically: c = pow(m, e, n)
since e is a low value such as 3, m^3 will always be lesser than N. this rendered N useless in the formula, cause the main purpose of modulo operation is to reduce the m^e value to the range within N.
so the forumla now is: c = pow(m, e) # n being not relevant cause m^e < N anyway
to get value of 'M', move the e to the LHS, which becomes (cube root of c) = m. this is why this attack is called cube root attack. but e may be any value which is low, and can be lower than N.


### Steps in solving:

1. Extract the N,e values from the public key.

```python
from Cryptodome.PublicKey import RSA

def extract_n_e():
    with open("pubkey.pem", "rb") as f:
        key = RSA.import_key(f.read())
    print("n:", key.n)
    print("e:", key.e)

if __name__ == "__main__":
    extract_n_e()
```


This will generate the n,e values:
```

n: 18328270981827589684453307152926857989515797049095684193665439607837898219431012886597006481425145171775978062527566325266122164712831819030866588242683783910717940135743498400109938324375354875794213228138138808324911660229371871252207414350021598944073279423219569164569563857405002809470309327639439479648351390421862534605072391443328575145532812945187032707895832317557847703228958210837712775945134679201537597202047618965441495904064618196664063870179903937192628427289860593096398468376151694908896600406382492813003109971959766792011027500613617409898976857036143245195799422860920956168269215291406912020681
e: 3

```

From this vulnerability, as odd as it looks, the exponent is low and is thus vulnerable to cube root attack.

### Solve script

```python
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

```

This will get you the flag!
