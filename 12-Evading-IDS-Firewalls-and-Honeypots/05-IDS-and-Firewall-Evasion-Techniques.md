
# IDS and Firewall Evasion Techniques

IDS and Firewall Evasion Techniques refer to methods used by attackers to modify the way an attack is performed so that security systems cannot detect it.

IDSs and firewalls rely on predefined rules to identify and block suspicious traffic. Attackers may attempt to bypass these rules by manipulating network traffic, hiding their activities, or exploiting weaknesses in security systems.

## 1. Bypassing Blocked Sites Using an IP Address

In this method, instead of entering the domain name of a blocked website, the attacker enters its IP address directly into the browser.

For example, instead of entering:

```text
www.example.com
```

The user enters the website's IP address.

Services such as Host2IP can help identify the IP address associated with a domain.

**Limitation:** This method works only when the filtering software blocks the domain name but does not also block the corresponding IP address.

## 2. Bypassing Blocked Sites Using Anonymous Website Surfing

Online anonymous browsing services and proxy websites can be used to access blocked websites.

These services may:

- Encrypt the requested URL to make it harder for filtering systems to identify.
- Hide the user's real IP address.
- Display the proxy server's IP address instead of the user's original IP.

This can allow users to access websites that are otherwise blocked by filtering systems.

## 3. Bypassing Firewalls through SSH Tunneling

SSH Tunneling allows network traffic to pass through an encrypted SSH connection.

For example, imagine that FTP traffic is blocked by a firewall or IDS. Since FTP is not encrypted by default, its traffic may be restricted.

SSH tunneling can carry this otherwise unencrypted traffic through an encrypted SSH connection.

This technique can make it harder for security systems to inspect the original traffic.

## 4. Bypassing Firewalls through DNS Tunneling

DNS Tunneling is a technique that uses DNS traffic to carry data between systems.

According to the course material:

- DNS commonly uses UDP.
- The course describes a 255-byte limit for outgoing DNS queries.
- Data can be embedded within DNS packets and transferred through DNS requests.

This technique can be abused for data exfiltration and for maintaining communication between an infected system and a Command and Control (C&C) server.

Even DNSSEC cannot identify every anomaly associated with DNS tunneling.

**Examples of DNS tunneling tools:**

- `iodine`
- `dnscat2`

These tools can tunnel traffic through DNS, commonly using port `53`.

## 5. Bypassing IDS/WAF Using an XSS Attack

Cross-Site Scripting (XSS) exploits vulnerabilities that occur when web applications process user input and server responses.

Attackers may use different representations or encodings of malicious HTML and JavaScript payloads to evade security filters.

The course demonstrates examples involving:

- Standard JavaScript payloads.
- `String.fromCharCode()` encoding.
- URL encoding.
- HTML entity encoding.
- Alternative HTML elements and event handlers.

These variations may help an attacker bypass poorly configured IDS or Web Application Firewall (WAF) rules.

## 6. Insertion

Insertion is a technique that attempts to confuse an IDS.

An IDS uses Pattern Matching algorithms to identify specific patterns in network packets.

In an insertion attack, an attacker manipulates packet data in a way that causes the IDS to interpret the traffic differently from the destination system.

This difference in interpretation may allow malicious traffic to evade detection.

## 7. DoS Against IDS

Many IDS implementations use a central server to store security alerts and event logs.

If an attacker discovers the IP address of this central server, they may attempt to launch a Denial-of-Service (DoS) attack or cause the server to crash.

Possible consequences include:

- The IDS may become unable to record new attack events.
- The attacker’s activities may not be logged.
- Event storage may become full.
- Investigators may have difficulty reconstructing the attack.

## 8. Obfuscation

Obfuscation involves modifying or disguising an attack payload to make it harder for an IDS to recognize.

The destination system may still be able to interpret the packet even when the IDS cannot properly read or recognize it.

Examples mentioned in the course include:

- Using Unicode patterns to bypass IDS filters.
- Using HTTPS to make traffic inspection more difficult.
- Using Steganography to conceal information within other data.

The target application or server must still be capable of interpreting the modified data.

## 9. False Positive Generation

In this technique, an attacker deliberately generates malicious-looking packets to trigger numerous false alerts in an IDS.

The large number of alerts can overwhelm security monitoring and distract security personnel.

While the IDS is busy processing these false alerts, the attacker may attempt to hide the actual attack among the generated warnings.

## 10. Fragmentation

Fragmentation involves splitting network packets into smaller pieces before sending them to the target.

The destination system reassembles these fragments after receiving them.

A potential weakness occurs when the IDS and the destination system handle packet reassembly differently or use different reassembly timeouts.

This difference may cause the IDS to interpret the traffic differently from the target system, potentially allowing malicious traffic to evade detection.

## Related Links

- [RFC 4251 - The Secure Shell (SSH) Protocol Architecture](https://www.rfc-editor.org/rfc/rfc4251)
- [RFC 1035 - Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035)
- [OWASP Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)
- [OWASP Web Application Firewall](https://owasp.org/www-project-modsecurity-core-rule-set/)
- [Snort Documentation](https://docs.snort.org/)

## Summary

IDS and firewall evasion techniques attempt to avoid detection by modifying, disguising, or redirecting network traffic.

| Technique | Main Idea |
|---|---|
| IP Address Bypass | Accessing a blocked website through its IP address |
| Anonymous Website Surfing | Using proxy services to hide the original IP address |
| SSH Tunneling | Carrying traffic through an encrypted SSH connection |
| DNS Tunneling | Transferring data through DNS queries |
| XSS-based Evasion | Using different payload representations to bypass IDS/WAF filters |
| Insertion | Confusing IDS pattern-matching mechanisms |
| DoS Against IDS | Disrupting the IDS or its central logging server |
| Obfuscation | Disguising malicious payloads |
| False Positive Generation | Overwhelming the IDS with misleading alerts |
| Fragmentation | Splitting packets to exploit differences in reassembly |
