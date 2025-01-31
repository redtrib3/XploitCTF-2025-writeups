# Crypto: Brick By Brick

**Author**: [UjjwalBeast](https://github.com/Ujjwalbeast)<br>
**Points**: 150<br>
**Hint(s)**: None<br>
**Flag**: `xploit{mult1_l3v3l_br1cks}`<br>

**Challenge description:**
```
I built this :
5a57526a5a324e685a6d4a6c59574a685a5452695832566b596d466959474a675a57466a5a3252685a6c396b5a324a685a6d646c4e47566a5a54566b5a575a695a476469595751795a6d4a6b6147526d5a574e6961413d3d

```

## Solve

This challenge involves identifying a multiple levels of encodings and decoding it. You can use tools such as cyberchef for this.

### Decoding pattern:
```
Hex --> Base64 --> Rot47 --> Hex --> Base64 --> plaintext
```

### Cyberchef decode link:
https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')From_Base64('A-Za-z0-9%2B/%3D',true,false)ROT47(47)From_Hex('Auto')From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=NWE1NzUyNmE1YTMyNGU2ODVhNmQ0YTZjNTk1NzRhNjg1YTU0NTI2OTU4MzI1NjZiNTk2ZDQ2Njk1OTQ3NGE2NzVhNTc0NjZhNWEzMjUyNjg1YTZjMzk2YjVhMzI0YTY4NWE2ZDY0NmM0ZTQ3NTY2YTVhNTQ1NjZiNWE1NzVhNjk1YTQ3NjQ2OTU5NTc1MTc5NWE2ZDRhNmI2MTQ3NTI2ZDVhNTc0ZTY5NjE0MTNkM2Q
