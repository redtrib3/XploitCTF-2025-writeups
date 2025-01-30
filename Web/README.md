# Web challenges summary

## X-Marks-The-Flag (100)
Analyse the given source code to find a custom header named X-Xploit-Id being defined. Flag is returned when we send the custom header with the value 31337.

## NoteWorthy 
IDOR vulnerability in notes app, lets you read others' notes. read through the numbers to get the flag from note 0.

## xploitdb
Union based SQL injection. The website provides its source code. inject union queries to enumerate and dump values from other table containing the flag.

## The cook 
(This challenge initially involved exploiting a Flask console by finding a PIN to achieve RCE, but due to unexpected server-side restrictions at the last moment, it had to be limited to file traversal and PIN generation.)
Flask debug pin console hacking, use the flask pin generation algorithm to generate the debug pin, which is the flag.
To get the values required by the pin generation algorithm, exploit a file traversal vulnerability in the job listing page.


