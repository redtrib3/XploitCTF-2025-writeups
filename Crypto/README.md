# Crypto challenges summary

## Collision Among us (120)
Find the unique file from many using md5sum, fails cause it has hashcollision. use sha1sum to find the different file.

## Brick by Brick (150)
Provided a text which is encoded using multiple levels of different encoding, identify and decode each level to get the flag.

## RSA1000 (250)
Factorise a 1000 bit modulus N, to generate the decryption key (d) and thus find the flag.

## The Curse of the Three (450)
Exploit a low public exponent vulnerability in implementation of RSA, find the n,e from a pubkey file, and do the cube root attack to get the flag.
