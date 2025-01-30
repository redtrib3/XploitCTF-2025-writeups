# Misc: Hidden Meme

**Author**: [redtrib3](https://github.com/redtrib3)
**Points**: 100
**Hint(s)**: None
**Flag**: `xploit{1n_pl41n_s1ght_0x6d7}`

**Challenge description:**
```
My friend sent me this weird meme, hmm...
```

## Solve

This is an easy steganography challenge, the title points to that.
use steghide to extract files with a blank password. (no password)

`steghide extract -sf meme.jpg`

This extracts a zip file named flag.zip with the flag.txt file.
the flag.txt contains 100s of lines of text with the flag hidden within, use `cat flag.txt | grep xploit{` to find the flag!

