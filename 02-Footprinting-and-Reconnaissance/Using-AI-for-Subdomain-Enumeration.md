
# Using AI for Subdomain Enumeration

AI tools can help security researchers create scripts for automating subdomain discovery.

One common technique is **Brute-force Subdomain Discovery**, which uses a wordlist of common subdomain names and DNS queries to identify valid subdomains.

## How It Works

1. Select a target domain.
2. Prepare a wordlist containing common subdomain names.
3. Combine each wordlist entry with the target domain.
4. Use `dig` or DNS lookup commands to check whether each subdomain resolves.
5. Save discovered subdomains and their IP addresses to an output file.

## 1. Bash Script (Linux / macOS)

The following script uses `dig` to perform DNS lookups for potential subdomains.

```bash
#!/bin/bash

DOMAIN="example.com"
WORDLIST="/path/to/subdomains.txt"
OUTPUT="found_subdomains.txt"

# Clear previous results
> "$OUTPUT"

echo "[*] Starting subdomain enumeration for $DOMAIN..."

while read -r SUB; do
    FULL="$SUB.$DOMAIN"
    RESULT=$(dig +short "$FULL")

    if [[ -n "$RESULT" ]]; then
        echo "$FULL -> $RESULT" | tee -a "$OUTPUT"
    fi

done < "$WORDLIST"

echo "[*] Enumeration complete. Results saved in $OUTPUT"
```

### Important Commands

- `dig`: Queries DNS records and retrieves DNS information.
- `dig +short`: Displays concise DNS query results.
- `while read -r`: Reads each line from the wordlist.
- `tee -a`: Displays results in the terminal and appends them to a file.
- `-n`: Checks whether a string is non-empty when used with `[[ ... ]]`.

## 2. PowerShell Script (Windows)

On Windows, PowerShell provides the `Resolve-DnsName` command for performing DNS queries.

```powershell
$domain = "example.com"
$wordlist = "C:\wordlists\subdomains.txt"
$output = "found_subdomains.txt"

Write-Output "[*] Starting subdomain enumeration for $domain..."

Remove-Item $output -ErrorAction SilentlyContinue

Get-Content $wordlist | ForEach-Object {
    $sub = "$_.$domain"

    $result = Resolve-DnsName -Name $sub -Type A `
        -ErrorAction SilentlyContinue |
        Where-Object { $_.IPAddress }

    if ($result) {
        Write-Output "$sub -> $($result.IPAddress)"
        Add-Content -Path $output -Value $sub
    }
}

Write-Output "[*] Enumeration complete. Results saved in $output"
```

### Important Commands

- `Get-Content`: Reads the contents of a wordlist file.
- `ForEach-Object`: Processes each wordlist entry.
- `Resolve-DnsName`: Performs DNS resolution.
- `-Type A`: Requests IPv4 address records.
- `Add-Content`: Appends discovered subdomains to an output file.

## 3. Wordlists

A wordlist contains common subdomain names that are tested against the target domain.

Examples:

```text
www
mail
ftp
admin
dev
test
vpn
api
blog
support
```

A popular collection of wordlists is **SecLists**.

GitHub Repository:
https://github.com/danielmiessler/SecLists

Example wordlist:

```text
Discovery/DNS/subdomains-top1million-110000.txt
```

## Role of AI in Subdomain Enumeration

AI can assist security researchers by:

- Generating Bash and PowerShell enumeration scripts.
- Modifying scripts for different operating systems.
- Explaining command syntax and troubleshooting errors.
- Improving output formatting and result processing.
- Helping automate repetitive reconnaissance tasks.

## Limitations

- Results depend on the quality and size of the wordlist.
- DNS resolution does not guarantee that a discovered subdomain hosts an active website.
- Some subdomains may not be discovered because they are not included in the wordlist.
- DNS wildcard records may produce false positives.
- Rate limits and DNS filtering may affect results.

**Important:** Run enumeration scripts only against domains you own or are explicitly authorized to assess.
