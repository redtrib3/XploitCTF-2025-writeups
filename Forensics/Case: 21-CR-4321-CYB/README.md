# Forensics: Case: 21-CR-4321-CYB

**Author**: [redtrib3](https://github.com/redtrib3)<br>
**Points**: 300<br>
**Hint(s)**: None<br>
**Flag**: `xploit{but_m0st_of_4ll_samy_1smy_h3ro}`<br>

**Challenge description:**
```
Check Detective's note for more info.
```

## Solve

Read through detective RC's note which says that we are provided with a zip file containing the convict's unix home directory.
unzip the zip file, and we get "samy's home" directory containing many folders.

Look through the home directory and you see the hidden  .mozilla directory.
.mozilla is a configuration folder for firefox, there are plenty of tools in github to decrypt this and find saved login passwords.

```bash

└──╼ $python3 ~/Documents/firefox_decrypt/firefox_decrypt.py .mozilla/firefox/
Select the Mozilla profile you wish to decrypt
1 -> r79xlqea.Samyk
2 -> xwh2xjlu.default

```

we get two different firefox profile, including one named 'samyk', press 1 to get a list of saved passwords.

### Saved Passwords:

```

Website:   https://amazon.in
Username: 'samy_h3cker'
Password: 'OlInTaricKYR!'

Website:   https://distrotest.net
Username: 'KineticSamy'
Password: 'SPOnEsnuCulayouwontrememberthis'

Website:   https://www.utorrent.com
Username: 'sammmmypirates'
Password: 'SamyKxoxo!@#!@$#!!!'

Website:   http://holyflags.fr
Username: 'FlaggedByS4mypart2'
Password: 'but_m0st_of_4ll_samy_1s'

Website:   https://instagram.com
Username: 'samyyyyy.k__'
Password: 'tomcatbob!!!1997'

```


One of the password from `http://holyflags.fr` looks interesting and like a flag, the username hints that there a multiple parts of this flag scattered, and this is the second part.
```
part 2 -> but_m0st_of_4ll_samy_1s
```

Where else would sensitive data be stored?

## Cookies:

Cookies in firefox is stored in a sqlite3 database name cookies.sqlite, go ahead and dump the only table named 'moz_cookies'
One of the cookie is present in the same website we found password on - holyflags.fr.

```

8||THE_HOLY_COOKIE|bXlfaDNyb30=|.holyflags.fr|/login|195672271|119641754|945064534|1|1|0|2|1|0|0

```
Decode the cookie value, we get the third part of the flag: `my_h3ro}`

Where would the final part of the flag be?

### History

A quick google search says that firfox saves user history in a file called `places.sqlite` in the table `moz_places`.
Dump that table, and look through it. You can also use grep for 'xploit{' if your eyes dont work like mine or you are too lazy.

### The flag

Now we found the flag from three different parts:

```
xploit{but_m0st_ = History
of_4ll_samy_1s   = Saved encrypted credential
my_h3ro}         = cookies base64 encoded
```

