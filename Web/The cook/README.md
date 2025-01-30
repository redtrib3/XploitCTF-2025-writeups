# Web: X-Marks-The-Flag

**Author**: redtrib3 (https://github.com/redtrib3)
**Points**: 500
**Hint(s)**: `Headers` (0 pts)
**Flag**: `xploit{582-036-628}`

**Challenge description:**
```
I made a paste app, BugBin, where you can store your bugs.

However, recent pentests revealed that I may have left a web console open somewhere. Thankfully, the issue has been fixed, and the console has been deleted. Conduct a pentest and trace the attacker's path to find the console key.

**Flag Format:**<br>
`xploit{XXX-XXX-XXX}` , where XXX is a 3 digit number.

**Challenge Link:**
http://xploitctf.live:64297
```

## Solve

The challenge which is directly provided in the description is to find a 'pin' for the console.
The application provided is a paste service type of app where you can create public and private pastes. The paste service itself does not seem to be vulnerable.

The application does not have many endpoints, except `/about`, where many important information is provided. This includes a 'admin' email address, which we take note of for now.
We are provided the `/jobs` endpoint, where there are job listings. if you notice the initial loading and run the request using a proxy interceptor like burpsuite, (or just check the Inspect source) you will find the javascript making request to an API endpoint.

-> `/api/fetch-data` with a post parameter `file=jobs.dat`, try removing the file name, or change it something else, This will eventually result in all types of errors and tracebacks. This is a Flask traceback on a debug server!
and Flask have a locked debug console with a PIN. The description must make sense now.

Our task is to generate the flask debug pin following the debug pin generation algorithm here:
https://hacktricks.boitatech.com.br/pentesting/pentesting-web/werkzeug#15bad021803443318e30d3fdc4d0f312



## Generating the console pin

To generate the console pin, we need the following information.
```python

probably_public_bits = [
    '<username>',  # username, # get from error
    'flask.app',  # modname, # most of the time right
    'Flask',  # getattr(app, '__name__', getattr(app.__class__, '__name__'))
    '/usr/local/lib/python3.5/dist-packages/flask/app.py',
]

private_bits = [
    '2485377892354', # str(uuid.getnode()),  # get network interface from /proc/net/arp, /sys/class/net/<interface>/address
    '8d00bb9313094a9b87c9f1943025b7d3docker-b75193191750d197e1d72e4cd74336af9c6be74930a15c21c28ccfc6ee82e81b.scope', # get_machine_id(), /etc/machine-id + last slash after /proc/self/cgroup
]

```


### Getting probably public bits

**username**: We know that the username is probably usultheadmin, since its has already been provided. This can be confirmed by reading the `/etc/passwd` file using the file traversal.
**modname** : This is `flask.app` most  of the time.
**server**  : This is for the Server class, it can either be `Flask` for flask development servers, or `wsgi_app` for wsgi run applications, since its in production environment, lets assume the organizers wont run a unscalable dev server ;)
**Filepath** : This is the file path of the native flask code, this can be extracted from the traceback.

### Getting probably Private bits

**The first bit**: Get the network interface by checking `/proc/net/arp` and we see its `eth0`. lets get the mac address from `/sys/class/net/eth0/address` - 02:42:ac:11:00:05, convert into a integer using python or any tool - `int(0x0242ac110005) = 2485377892357`
**The second bit**: we need to concatenate two different information here. /etc/machine-id (which is a unique id for every machine generated at boot) + last slash after /proc/self/cgroup.


If you get all the values plug it into the exploit, and generate the pin, thats the flag!



