# Forensics: The portable documents

**Author**: [greed](https://github.com/greedoftheendless)<br>
**Points**: 120<br>
**Hint(s)**: None<br>
**Flag**: `xploit{cr4ck3d_ez}`<br>

**Challenge description:**
```
Did you know? PDFs were originally called “Camelot” before being renamed to PDF in 1993! I just made that up.

Now help me read this pdf.
```

## Solve

Provided a PDF document with a password, use tools like pdfcrack or pdf2john to find the password.

```bash

└──╼ $pdf2john The_Hidden_Path_to_Discovery.pdf > hash
└──╼ $john hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PDF [MD5 SHA2 RC4/AES 32/64])
Cost 1 (revision) is 4 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
rugrat           (The_Hidden_Path_to_Discovery.pdf)
1g 0:00:00:00 DONE (2025-01-31 19:12) 1.724g/s 14344p/s 14344c/s 14344C/s total90..THOMAS
Use the "--show --format=PDF" options to display all of the cracked passwords reliably
Session completed.

```

Open the pdf file, and find the flag from the paragraphs using find and replace - 'xploit{'.

