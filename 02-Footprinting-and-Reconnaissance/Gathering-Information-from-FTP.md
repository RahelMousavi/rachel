
# Gathering Information from FTP

FTP (File Transfer Protocol) is a network protocol used to transfer files between a client and a server over a network.
SFTP (SSH File Transfer Protocol) is a separate file transfer protocol that uses SSH to provide secure file transfers.
During the Footprinting phase, penetration testers collect information about FTP servers, their configurations, directories, and publicly exposed resources.
The main goal is to identify FTP-related information that may reveal security weaknesses or misconfigurations in the target infrastructure.

## Objectives of FTP Information Gathering

- **Discovering FTP Servers:** Identifying FTP servers associated with the target organization.
- **Finding Exposed Directories:** Discovering publicly accessible FTP directories and files.
- **Identifying Configuration Files:** Finding information about FTP server configurations.
- **Discovering Server Information:** Identifying server types, software, and related technologies.
- **Detecting Information Disclosure:** Finding sensitive information that may have been unintentionally exposed.
- **Identifying Security Weaknesses:** Discovering misconfigurations and potential security risks.

## FTP Information Gathering Techniques

### 1. Finding FTP/SFTP Configuration Information

Search engines can help discover publicly indexed configuration files, source code, and repository content related to FTP and SFTP servers.
These files may reveal server settings, software information, and configuration details.

### 2. Discovering Sensitive FTP Directories

Google search operators can help identify publicly indexed FTP directories and directory listings.
Exposed directories may contain documents, backups, or other resources that should not be publicly accessible.

### 3. Finding FTP Server Configuration Files

Searching for configuration file names, such as `pure-ftpd.conf`, may reveal publicly indexed information about FTP server configurations.
These files may contain details about server settings, access permissions, and authentication methods.

### 4. Identifying Exposed FTP/SFTP Configuration Files

Search engines may index files related to FTP/SFTP configurations, including files used by development tools.
If these files are publicly accessible, they may reveal technical details about the environment.

### 5. Discovering Public FTP Servers

Search queries can help identify websites that expose FTP directory listings or publicly accessible FTP resources.
These listings may reveal file names, directory structures, and available resources.

### 6. Identifying FTP Servers by IP Address

Search engines may index FTP-related pages and files associated with specific IP addresses.
This information can help researchers identify exposed servers and understand the target's external infrastructure.

## Google Dorks for FTP Footprinting

Google Dorks are advanced search queries that use Google search operators to find specific information indexed by the search engine.
The following examples demonstrate how these operators can be used for FTP-related information gathering.

### 1. FTP Configuration References

```text
inurl:github.com intext:ftpconfig -issues
```

Searches GitHub-indexed pages for references to FTP configuration information.

### 2. FTP-Related PDF and PostScript Files

```text
site:mil inurl:ftp (filetype:pdf OR filetype:ps)
```

Searches indexed FTP-related PDF and PostScript files on .mil domains.

### 3. Pure-FTPd Configuration References

```text
intext:pure-ftpd.conf intitle:index.of
```

Searches for indexed directory listings containing references to Pure-FTPd configuration files.

### 4. SFTP Configuration References

```text
intitle:"Index Of" intext:sftp-config.json
```

Searches for indexed directory listings containing references to SFTP configuration files.

### 5. Public FTP Directory Listings

```text
inurl:"ftp://www." "Index of /"
```

Searches for indexed pages referencing FTP directories and directory listings.

**Note:** Google Dorks only return information indexed by Google. A search result does not necessarily mean that a server is currently accessible or vulnerable.

## Security Risks of Exposed FTP Information

Exposing FTP-related information may introduce several security risks:

### 1. Credential Exposure
Unintentionally published configuration files or source code may reveal usernames, passwords, or other authentication information.

### 2. Directory Exposure
Publicly accessible FTP directories may expose confidential documents, backups, or internal resources.

### 3. Information Disclosure
Configuration files and server banners may reveal software versions, server settings, and technical details.

### 4. Unauthorized Access
Weak authentication, excessive permissions, or improperly configured anonymous FTP access may allow unauthorized users to access server resources.

### 5. Data Interception
Traditional FTP does not encrypt credentials or file transfers by default, which can expose information to interception during transmission.
SFTP provides encrypted communication through SSH and is a more secure alternative for file transfers.

## Summary

Gathering Information from FTP is a footprinting technique used to discover information about FTP servers, configurations, directories, and publicly exposed resources.
Google Dorking can help identify:

- FTP-related configuration files.
- Publicly accessible directories.
- Exposed server information.
- FTP/SFTP-related documents.
- Potential security misconfigurations.

This information helps penetration testers understand the target's external infrastructure, identify potential security weaknesses, and prepare for further security assessments.

**Important:** FTP reconnaissance and security testing must only be performed within an authorized scope. Discovered credentials and private files must never be accessed or used without permission.
