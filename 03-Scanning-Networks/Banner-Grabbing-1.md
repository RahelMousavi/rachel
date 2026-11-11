
# Banner Grabbing

Banner Grabbing is a technique used to collect information about services running on a target system.

When a client connects to a network service, the service may return information such as:

- Service name.
- Software name.
- Software version.
- Operating system information.
- Server type.

This information can help security professionals identify running services, understand the target environment, and discover potentially outdated software.

## 1. Types of Banner Grabbing

Banner Grabbing is divided into two main categories:

- Passive Banner Grabbing
- Active Banner Grabbing

### Passive Banner Grabbing

Passive Banner Grabbing collects service information without directly sending specially crafted probes to the target service.

The slide introduces the following methods:

#### 1. Banner Grabbing from Error Messages

Some applications and services reveal information about their software when generating error messages.

For example, an error response may disclose:

- Web server software.
- Application framework.
- Software version.
- Server configuration details.

#### 2. Sniffing Network Traffic

Network sniffing involves capturing and analyzing network packets exchanged between systems.

Some protocols and services transmit information that can reveal service banners or software details.

Tools such as Wireshark and NetworkMiner can help analyze captured network traffic.

#### 3. Banner Grabbing from Web Pages

Web servers may expose information through HTTP response headers or page content.

For example, an HTTP response may contain:

```http
HTTP/1.1 200 OK
Server: Apache/2.4.XX
Content-Type: text/html
```

The `Server` header may reveal the web server software and version.

However, administrators can hide or modify this information.

#### 4. Banner Grabbing with Netcraft

Netcraft provides information about websites and their hosting infrastructure.

Depending on the available data, it may provide information about:

- Web server technologies.
- Hosting providers.
- Operating systems.
- Website infrastructure.

Website: https://www.netcraft.com/

### Active Banner Grabbing

Active Banner Grabbing involves directly interacting with a target service by sending requests or specially crafted packets.

The slide introduces the following methods:

#### 1. Specially Crafted Packets

A scanner sends customized packets to a target service and analyzes its responses.

The responses may reveal information about the running service or the target's network stack.

Tools such as hping3 can be used to create customized network packets.

#### 2. Banner Grabbing with Telnet

Telnet can establish a connection to a TCP service and allow a user to send application-level requests manually.

For example, an HTTP request can be sent to a web server:

```bash
telnet 10.10.10.10 80
```

After connecting, enter:

```http
GET / HTTP/1.0
Host: 10.10.10.10
```

Press Enter twice to complete the request.

The server may return an HTTP response containing headers and server information.

#### 3. Banner Grabbing with Ping (TTL)

The slide introduces TTL (Time To Live) values as a possible way to estimate the operating system of a target.

Typical initial TTL values often associated with operating systems are:

- Linux: 64
- Microsoft Windows: 128
- Cisco devices: 255

For example, if a target responds with a TTL value of 63, it may have started with an initial TTL of 64 and the packet may have passed through one router.

**Important:** TTL values are only clues, not definitive operating system identifiers. Different systems can use different initial values, and network routing changes the observed TTL.

---

## 2. Banner Grabbing Tools

Page 37 introduces several tools used for banner grabbing and network service identification.

### 1. ID Serve

ID Serve is a tool designed to identify web servers and retrieve information from HTTP services.

It can query a web server and examine its responses to identify server software.

The slide's screenshot shows an example in which the server is identified as Microsoft IIS.

### 2. PRADS

PRADS stands for Passive Real-time Asset Detection System.

It is a passive network traffic analysis tool that observes network traffic and attempts to identify active systems and services.

It can help with:

- Network asset discovery.
- Service identification.
- Passive operating system fingerprinting.
- Network monitoring.

Project: https://github.com/gamelinux/prads

### 3. P0f Banner Grabbing Tool

P0f is a passive operating system fingerprinting tool.

It analyzes network traffic without actively probing the target.

It can help identify:

- Operating system characteristics.
- Network stack fingerprints.
- Client and server information.

Project: https://lcamtuf.coredump.cx/p0f3/

### 4. SINFP

SINFP is a network fingerprinting tool designed to identify operating systems through TCP/IP stack behavior.

It uses network response characteristics to help determine the operating system of a remote host.

### 5. NetworkMiner

NetworkMiner is a Network Forensic Analysis Tool (NFAT).

It analyzes captured network traffic and extracts information such as:

- Hosts.
- Operating systems.
- Network services.
- Files transferred over the network.
- Credentials and other protocol information, when present in captured traffic.

Website: https://www.netresec.com/?page=NetworkMiner

### 6. Xprobe

Xprobe is an operating system fingerprinting tool.

It uses network probes and analyzes responses to estimate the operating system of a remote host.

It is an older tool and is not commonly used in modern assessments.

### 7. Satori

Satori is a passive operating system fingerprinting tool.

It analyzes network traffic to identify operating systems and devices based on their network behavior.

### 8. THC AMAP

AMAP (Application Mapper) is a tool designed to identify applications and services running on network ports.

Unlike simply assuming a service based on its port number, AMAP attempts to identify the actual application through service responses.

It can be useful when services run on non-standard ports.

Project: https://github.com/vanhauser-thc/thc-hydra

**Note:** The link above is for THC Hydra, not AMAP. AMAP was historically distributed as part of the THC tool collection; availability of its original standalone project may vary.

---

## 3. Practical Banner Grabbing with Netcat

Page 38 demonstrates banner grabbing using Netcat.

Netcat (`nc`) is a command-line networking utility that can establish TCP or UDP connections and send or receive data.

### Step 1: Connect to the Target

```bash
nc -vv www.example.com 80
```

Command breakdown:

- `nc`: Runs Netcat.
- `-v`: Enables verbose output.
- `-vv`: Enables additional connection details.
- `www.example.com`: Specifies the target hostname.
- `80`: Specifies the destination port.

### Step 2: Send an HTTP Request

After establishing the connection, enter:

```http
GET / HTTP/1.0
```

Press Enter twice.

The server may return an HTTP response containing information about the web server.

### Example Response

```http
HTTP/1.1 200 OK
Date: Tue, 11 Nov 2026 08:00:00 GMT
Server: Microsoft-IIS/6.0
Content-Type: text/html
Connection: close
```

In this example:

```http
Server: Microsoft-IIS/6.0
```

reveals that the web server identifies itself as Microsoft IIS 6.0.

**Note:** This is an illustrative response based on the type of output shown in the slide, not a live server response.

---

## 4. Practical Banner Grabbing with Telnet

Telnet can also be used to connect to a TCP service and manually send an HTTP request.

### Step 1: Connect to the Web Server

```bash
telnet www.example.com 80
```

### Step 2: Send an HTTP Request

```http
GET / HTTP/1.0
Host: www.example.com
```

Press Enter twice.

### Step 3: Analyze the Response

The server may return HTTP headers containing information such as:

```http
HTTP/1.1 200 OK
Server: Microsoft-IIS/6.0
Content-Type: text/html
```

The `Server` header can help identify the web server software.

**Security Note:** Telnet does not encrypt its connection. Use it only in controlled environments or when connecting to services where plaintext communication is appropriate. Netcat or modern alternatives can be used for other testing scenarios.

---

## 5. Passive vs. Active Banner Grabbing

### Passive Banner Grabbing

- Observes existing network traffic or information already exposed by applications.
- Does not need to initiate a direct service probe.
- Examples: traffic sniffing, analyzing error messages, and examining web pages.
- Tools: Wireshark, NetworkMiner, PRADS, and P0f.

### Active Banner Grabbing

- Directly interacts with the target service.
- Sends requests or probes and analyzes the responses.
- Examples: connecting with Telnet or Netcat and sending HTTP requests.
- Tools: Netcat, Telnet, and hping3.

## Summary

Banner Grabbing is used to collect information about services and applications running on a target system.

The two main approaches are:

- **Passive Banner Grabbing:** Collects information from existing traffic or exposed information without directly probing the service.
- **Active Banner Grabbing:** Sends requests or probes to the target and analyzes its responses.

Common tools introduced in these pages include:

- ID Serve
- PRADS
- P0f
- SINFP
- NetworkMiner
- Xprobe
- Satori
- THC AMAP
- Netcat
- Telnet

Banner information can help identify outdated services and potential vulnerabilities. However, banners can be hidden, modified, or misleading, so they should not be treated as definitive proof of a software version.

---

## Related Links

### Banner Grabbing and HTTP

- [Netcat Manual](https://man.openbsd.org/nc.1) — Documentation for Netcat and its connection options.
- [curl Documentation](https://curl.se/docs/) — HTTP requests and response-header inspection.
- [HTTP Semantics — RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) — HTTP protocol semantics and header fields.
- [Netcraft](https://www.netcraft.com/) — Website and hosting infrastructure information.

### Banner Grabbing and Network Analysis Tools

- [Wireshark](https://www.wireshark.org/) — Network traffic capture and analysis.
- [NetworkMiner](https://www.netresec.com/?page=NetworkMiner) — Network forensic analysis tool.
- [PRADS](https://github.com/gamelinux/prads) — Passive real-time asset detection system.
- [P0f](https://lcamtuf.coredump.cx/p0f3/) — Passive operating system fingerprinting.
- [Nmap Service and Version Detection](https://nmap.org/book/man-version-detection.html) — Active service identification and version detection.
- [hping3](https://www.hping.org/) — TCP/IP packet crafting and network testing.

### Related Protocol References

- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — HTTP headers and response semantics.
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — TCP protocol specification.
- [RFC 791 — Internet Protocol](https://www.rfc-editor.org/rfc/rfc791.html) — IPv4 and TTL field specification.
