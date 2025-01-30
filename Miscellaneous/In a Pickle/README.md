# Misc: In a pickle

**Author**: [redtrib3](https://github.com/redtrib3)
**Points**: 300
**Hint 1**: pickletools will help identifying whats wrong. (0 pts)
**Hint 2**: Override the annoying function, the right way. (25 pts)
**Flag**: `xploit{a_sn4ke_1n_a_p1ckle_4nd_a_10ng_f1ag_t0_mak3_1t_h4rd_4u}`

**Challenge description:**
```
"All you have to do is execute the pickle", they said in unison.
```

## Solve

Execute the pickled hexadecimal in python, you'll notice that you exit the console/program without any output.
```python

>>> data = "80049545010000000000008c03737973948c04657869749493944d390585945294284b348c0174944b268c0166944b0b8c0134944b0568054b228c0130944b328c015f944b1a68094b008c0178944b108c016e944b368c0168944b3b68074b098c0173944b2c68084b0d8c0165944b0a680b4b0e68094b1168094b218c0131944b19680e4b078c0161944b15680f4b3768074b298c0167944b3568094b1e68094b2b68054b018c0170944b2068094b0868094b2468114b0c8c016b944b27680f4b1c680b4b1268104b2868104b1f68104b048c0169944b2f68104b1b68074b388c0172944b038c016f944b1d8c0164944b188c016c944b2a68094b2568094b318c0133944b3d8c017d944b0268184b068c017b944b0f680f4b23680b4b3068134b3c8c0175944b3968174b2e8c016d944b168c0163944b1368094b1768134b2d68094b33680f4b3a68094b146812752e"
>>> import pickle
>>> pickle.loads(bytes.fromhex(data))
<exits>
```

Now the right thing to do is analyse the pickle and find why its exiting, use pickletools!

```

>>> pickletools.dis(bytes.fromhex(data))
    0: \x80 PROTO      4
    2: \x95 FRAME      325
   11: \x8c SHORT_BINUNICODE 'sys'
   16: \x94 MEMOIZE    (as 0)
   17: \x8c SHORT_BINUNICODE 'exit'
   23: \x94 MEMOIZE    (as 1)
   24: \x93 STACK_GLOBAL
   25: \x94 MEMOIZE    (as 2)
   26: M    BININT2    1337
   29: \x85 TUPLE1
   30: \x94 MEMOIZE    (as 3)
   31: R    REDUCE
   32: \x94 MEMOIZE    (as 4)
   33: (    MARK
   34: K        BININT1    52
   36: \x8c     SHORT_BINUNICODE 't'
   39: \x94     MEMOIZE    (as 5)
   40: K        BININT1    38
   42: \x8c     SHORT_BINUNICODE 'f'
   45: \x94     MEMOIZE    (as 6)
   46: K        BININT1    11
   48: \x8c     SHORT_BINUNICODE '4'
   51: \x94     MEMOIZE    (as 7)
   52: K        BININT1    5
   <-- SNIPPED --> <-- SNIPPED -->

  326: K        BININT1    58
  328: h        BINGET     9
  330: K        BININT1    20
  332: h        BINGET     18
  334: u        SETITEMS   (MARK at 33)
  335: .    STOP
highest protocol among opcodes = 4
```

From this disassembly, we see the `sys.exit()` call at the start and a bunch of text jumbled and stored as stacks which seems to be the flag.
the best way to get the flag is to skip over the sys.exit() call, we can do this by overriding the function, since we control it.

## Script:
```python3

import pickle
import sys

# overwrite sys.exit so that module doesnt get called
sys.exit = lambda _: [_ for _ in range(100)] 

output = pickle.loads(bytes.fromhex(out))
print('\n',''.join([i for i in output if isinstance(i, str)]))
```
