# Web: NoteWorthy

**Author**: [redtrib3](https://github.com/redtrib3)<br>
**Points**: 150<br>
**Hint(s)**: None<br>
**Flag**: `xploit{auth3nticate_auth0rize_aud1t}`<br>

**Challenge description:**
```
Introducing NoteWorthy! ✨

It’s not your regular boring notes app—it’s a whole new take on privacy. Your secrets are all yours, miltary grade secured!

Challenge Link:
http://xploitctf.live:64299/
```

## Solve

We are given a note taking application. Go ahead and signup for an account, and login, in the dashboard, we can create a note,
view the created note, delete a note.

On viewing a note, notice the URL `/notes/<note_id>`, which is a numerical number, on creating a new note, its the previous note id + 1.
Try to access previous notes, and you can access other's notes!

decreasing note number one by one, you reach note id 0 which has the flag.

