## Google Hacking Database (GHDB)

Google Hacking Database (GHDB) is a categorized collection of advanced search queries, known as **Google Dorks**, used to discover publicly indexed information that may be sensitive or unintentionally exposed on the internet.

GHDB was originally created by **Johnny Long** around 2000 and is currently maintained by **OffSec** as part of the Exploit Database project.

### Purpose of GHDB

GHDB helps penetration testers and security researchers find information that may not be easily discovered through ordinary search queries.

It can be used to identify:

- **Exposed Files:** Publicly accessible documents and files that may contain sensitive information.
- **Sensitive Directories:** Directories that are unintentionally accessible to the public.
- **Login Portals:** Publicly indexed login pages and authentication interfaces.
- **Vulnerable Files:** Files that may reveal security weaknesses or misconfigurations.
- **Error Messages:** Error pages that expose technical details about servers and applications.
- **Information Disclosure:** Publicly exposed usernames, configuration details, and other sensitive information.
- **Network Information:** Indexed information about network devices and infrastructure.

### How GHDB Works

GHDB provides ready-made search queries that use advanced search operators such as `site:`, `inurl:`, `intitle:`, and `filetype:`.
Users can search the database, select a relevant Google Dork, and use it in a search engine to find matching indexed information.

### How to Use GHDB

1. Visit the Google Hacking Database website.
2. Search for a specific keyword or select a category.
3. Review the available Google Dorks.
4. Select a query relevant to the information you are looking for.
5. Use the query in Google Search.
6. Analyze the results to identify publicly exposed information.

**Note:** GHDB is a collection of search queries, not a vulnerability scanner or exploitation tool. Finding a result does not automatically mean that the target is vulnerable.

### Official Website

Google Hacking Database is available through Exploit Database:

https://www.exploit-db.com/google-hacking-database
