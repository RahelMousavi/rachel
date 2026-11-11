
## LDAP Enumeration

### What Is LDAP?

LDAP (Lightweight Directory Access Protocol) is a protocol used to access and manage distributed directory services, such as Microsoft Active Directory.

It allows users and applications to search for information stored in directory services.

### Information Available Through LDAP

LDAP can provide information such as:

- Usernames
- Email addresses
- Departments
- Server information
- User accounts
- Group information
- Computer information

### LDAP Enumeration

LDAP Enumeration is the process of gathering information from directory services by querying an LDAP server.

Attackers may obtain sensitive information from an LDAP server, sometimes even without authentication, depending on its configuration and access permissions.

This information can later be used in other attacks against the network.

### LDAP Port

LDAP commonly uses:

- **TCP 389:** Standard LDAP port.

### Role of DNS in LDAP

DNS can help locate directory services and domain controllers, making it easier for clients to discover and communicate with them.

LDAP information can also be retrieved using Domain User credentials, including details about users, groups, and computers.

---

## Manual LDAP Enumeration Using Python

LDAP Enumeration can be performed manually using Python and the `ldap3` library.

### Step 1 — Install ldap3

Install the required Python library:

```bash
pip3 install ldap3
```

### Step 2 — Connect to the LDAP Server

The following Python code creates an LDAP server object and establishes a connection.

```python
import ldap3

server = ldap3.Server(
    'Target IP Address',
    get_info=ldap3.ALL,
    port=389
)

connection = ldap3.Connection(server)

connection.bind()
```

### Code Explanation

- `import ldap3`: Imports the LDAP3 library.
- `ldap3.Server()`: Defines the LDAP server.
- `get_info=ldap3.ALL`: Requests all available server information.
- `port=389`: Specifies the standard LDAP port.
- `ldap3.Connection()`: Creates a connection to the LDAP server.
- `connection.bind()`: Attempts to establish an LDAP session.

If the connection is successful, `connection.bind()` returns:

```python
True
```

### Step 3 — Retrieve Server Information

After connecting to the LDAP server, the following command can be used to retrieve server information:

```python
server.info
```

This information may include:

- Domain name
- Naming context
- Server capabilities

### Using Secure LDAP

If the LDAP server uses SSL, enable SSL when defining the server:

```python
server = ldap3.Server(
    'Target IP Address',
    get_info=ldap3.ALL,
    port=636,
    use_ssl=True
)
```

Port `636` is commonly used for LDAPS.

---

## Manual LDAP Enumeration Using Python (Continued)

After obtaining the naming context from the LDAP server, directory objects can be retrieved using an LDAP search.

### Step 1 — Search the LDAP Directory

```python
connection.search(
    search_base='DC=DOMAIN,DC=DOMAIN',
    search_filter='(&(objectClass=*))',
    search_scope='SUBTREE',
    attributes='*'
)
```

### Code Explanation

- **search_base:** Specifies the starting point of the directory search. It is usually the domain's Distinguished Name (DN).
- **search_filter:** Defines which directory objects should be returned.
- **search_scope:** Specifies how far the search should extend.
- **attributes:** Specifies which attributes should be returned. `'*'` requests all user-accessible attributes.

### Search Scope

`SUBTREE` searches the specified directory entry and all its descendants.

### Step 2 — Check the Search Result

If the search is successful, the method returns:

```python
True
```

### Step 3 — Display the Results

To view the retrieved directory entries:

```python
connection.entries
```

The results may contain information about users, groups, computers, and other directory objects, depending on the search permissions.

---

## LDAP Enumeration Tools

Several tools can be used to browse, search, and manage LDAP directories.

### 1. HTML View

A tool for viewing LDAP directory information through an HTML-based interface.

### 2. LDAP Administrator

A graphical LDAP administration tool used to browse and manage directory entries.

### 3. JXplorer

An open-source LDAP browser that allows users to connect to LDAP servers and explore directory structures.

### 4. LDAP Admin Tool

A graphical application for browsing and managing LDAP directory data.

### 5. LDAP Account Manager

A web-based application for managing LDAP directory accounts and entries.

### 6. LEX — The LDAP Explorer

An LDAP directory browsing and exploration tool.

### 7. LDAP Admin

A graphical LDAP directory management tool used to browse and modify directory entries.

### 8. Active Directory Explorer

A tool from Microsoft Sysinternals for viewing and exploring Active Directory databases.

### 9. LDAP Administration Tool

A tool designed to help administrators browse and manage LDAP directories.

### 10. LDAP Search

A utility used to search LDAP directories and retrieve matching entries.

### 11. LDAP Browser/Editor

A graphical tool for browsing, searching, and editing LDAP directory information.

---

## Related Links

- [LDAP — RFC 4511](https://www.rfc-editor.org/rfc/rfc4511)
- [LDAP Data Interchange Format — RFC 2849](https://www.rfc-editor.org/rfc/rfc2849)
- [ldap3 — Official Documentation](https://ldap3.readthedocs.io/)
- [ldap3 — Installation](https://ldap3.readthedocs.io/en/latest/installation.html)
- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/)
- [JXplorer](http://jxplorer.org/)
- [LDAP Account Manager](https://www.ldap-account-manager.org/)
- [Microsoft Sysinternals — Active Directory Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/adexplorer)
