# Forensics: Investigation

**Author**: [redtrib3](https://github.com/redtrib3)<br>
**Points**: 450<br>
**Hint(s)**: Trace the path of the attacker, and reach the last step. You might find what you are looking for but in a different form. (50 pts)<br>
**Flag**: `xploit{1ncid3nt_r3sp0nse_101}`<br>

**Challenge description:**
```
Things are not going well at Microhard Corp. They are under constant attack. There are doubts as to whether the attackers have already broken in. The company is deeply impressed by your previous work and wishes for you to conduct an investigation.
```

## Solve

You are provided with the log and capture file(s) of various services. have a look through them, or use grep recursively to search for flag in the log files.
we do not find a flag, which points us to look in the wireshark capture file.

Use wireshark to analyse the capture file, if you walk through the incident, you'll find that the attacker has tried to bruteforce successfully into FTP, uploading a README.md file.
Followed by that, the attacker conducts a directory bruteforce of the HTTP website, to find some useful endpoints.

The attacker finds a command injection in the /boardDataWW.php endpoint, and manages to drop a shell.
Follow the tcp stream of the attacker's shell connection to find plaintext commands, in one of the commands the attacker echoes a base64.

```bash
www-data@98cd4575df25:/$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@98cd4575df25:/$ echo -n 'eHBsb2l0ezFuY2lkM250X3Izc3AwbnNlXzEwMX0= |becho -n 'eHBsb2l0ezFuY2lkM250X3Izc3AwbnNlXzEwMX0= |
www-data@98cd4575df25:/$ cd /mnt
```

decode the base64 to get the flag!
