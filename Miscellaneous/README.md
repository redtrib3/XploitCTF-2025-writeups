# Misc challenges summary

## Hidden meme (120)
use steghide to extract a zip file from the image containing the flag hidden among multiple words.

## The Bridge (150)
OSINT challenge to find the location of the bridge, use reverse image search to match the location of a popular tower and then use google maps to find the name of the bridge, find the year using wikipedia.

## We are hiring (200)
Given a google forms link, requiring the flag to submit the form, find the flag from the page source.

## In a Pickle (300)
Execute the pickle and you exit cause there is a sys.exit call at the start, which you can know using pickletools, override the sys.exit in a proper way and deserialize the payload to get the flag.

## Flag Checker v2 (500)
RET2WIN vulnerability, pwn the challenge by exploiting a buffer overflow calling the getflag() function.
