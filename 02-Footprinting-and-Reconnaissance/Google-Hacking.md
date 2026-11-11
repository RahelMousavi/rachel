## Google Hacking (Google Dorking)

Google Hacking, also known as Google Dorking, is an information-gathering technique that uses advanced Google search operators to find specific information indexed by Google.
Instead of performing ordinary searches, these operators allow users to narrow search results based on specific conditions, such as website domains, file formats, page titles, and URLs.
In ethical hacking, Google Hacking is used during the Footprinting phase to discover publicly available information, identify exposed resources, and understand the target's online presence.

### Google Hacking Operators

#### 1. cache:

Historically, this operator displayed Google's cached version of a web page, allowing users to view an older copy of the page.

**Example:**
`cache:example.com`

**Note:** Google discontinued this operator in September 2024.

#### 2. link:

Historically, this operator was used to find web pages linking to a specific URL.

**Example:**
`link:example.com`

**Note:** This operator is no longer reliably supported by Google.

#### 3. filetype:

Searches for files with a specific format, such as PDF, DOCX, XLSX, or PPT.
It is useful for finding publicly indexed documents related to a target.

**Example:**
`site:example.com filetype:pdf`

#### 4. site:

Restricts search results to a specific website or domain.
It helps discover indexed pages and publicly accessible content associated with a target.

**Example:**
`site:example.com`

#### 5. intitle:

Searches for web pages containing a specific word or phrase in their page titles.
It can help identify pages related to specific services, login portals, or administrative interfaces.

**Example:**
`intitle:"login page"`

#### 6. inurl:

Searches for web pages containing a specific word or phrase in their URLs.
It can help discover pages with particular URL patterns, such as login pages or administrative sections.

**Example:**
`inurl:admin`

### Summary

Google Hacking uses advanced search operators to narrow search results and discover publicly indexed information.

- `cache:` - Historically displayed Google's cached version of a web page.
- `link:` - Historically searched for pages linking to a specified URL.
- `filetype:` - Searches for files with a specific format.
- `site:` - Restricts results to a specific website or domain.
- `intitle:` - Searches for words in page titles.
- `inurl:` - Searches for words in URLs.

**Note:** Search results depend on Google's indexing and retrieval limits. These techniques should only be used for authorized security research.
