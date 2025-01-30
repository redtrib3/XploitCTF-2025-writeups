# Web: X-Marks-The-Flag

**Author**: [4-krishna](https://github.com/4-krishna)
**Points**: 100
**Hint(s)**: `Headers` (0 pts)
**Flag**: `xploit{31337_H34d3r_h4ck3r_0x6fa2}`

**Challenge description:**
```
Sometimes, all it takes to find the answer is ask the right thing.

Challenge Link:
http://xploitctf.live:64301
```

## Solve

Read through the provided flask app source code, you come across an interesting piece of code in routes.py.

```python
@main.route('/', methods=['GET', 'POST'])
def index():
    spec_header = current_app.config['SPEC_HEADER']
    spec_header_val = current_app.config['SPEC_HEADER_VAL']
    flag = current_app.config['FLAG']

    if request.method == "POST":
        if request.headers.get(spec_header) == spec_header_val:
            #return f"{flag}", 200
            return render_template('success.html', flag=flag), 200

    return render_template('index.html')

```

The code reads some env variables 'SPEC_HEADER', 'SPEC_HEADER_VAL', and the flag.
and if it gets a POST request, and the post request has headers that match the spec_header and value as spec_header_val, it will return you the flag.
The values of spec_header and spec_header_val are provided in the .env file, all you have to do is send a request containing the headers and you'll get the flag!


**curl request**
```bash
curl -X POST http://xploitctf.live:64301/ -H 'X-Xploit-Id: 31337' -v
```
