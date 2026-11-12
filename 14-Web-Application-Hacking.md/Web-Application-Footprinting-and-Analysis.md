
# Web Application Footprinting and Analysis

## 1. Introduction to Web Application Hacking Methodology

Web Application Hacking Methodology describes the steps used to identify and assess weaknesses in web applications.

The first stage is gathering information about the web infrastructure and understanding how the application operates.

This process includes identifying servers, services, technologies, hidden content, and potential vulnerabilities.

## 2. Footprinting Web Infrastructure

Footprinting Web Infrastructure is the initial information-gathering stage of web application testing.

According to the module, this process consists of five stages:

### 2.1 Server Discovery

Server Discovery involves collecting information about the target domain and hosting environment.

Activities include:

- Gathering domain and hosting information using WHOIS services.
- Identifying open ports on the target server.

**Tool:**
- Nmap

### 2.2 Service Discovery

After identifying open ports, the next step is determining which services are running on those ports.

This helps identify the services exposed by the target infrastructure.

**Tool:**
- Nmap

### 2.3 Server Identification

Server Identification involves collecting information about the web server by examining its banners.

Banner information may reveal details about the server and its running software.

The module introduces the following tools:

- **Netcraft:** Used to gather information about websites and their infrastructure.
- **Netcat:** Can be used to establish network connections and interact with services.
- **Telnet:** Can be used to connect to network services.
- **ID Serve:** Used for identifying web servers.
- **Wafw00f:** Used to identify Web Application Firewalls (WAFs).

### 2.4 Hidden Content Discovery

Hidden Content Discovery involves identifying hidden sections and resources within a web application.

These resources may not be directly accessible through the application's visible navigation.

**Tool:**
- Burp Suite

### 2.5 Load Balancer Detection

Load Balancer Detection involves identifying load balancers and their associated IP addresses.

The module mentions the following tools:

- `dig`
- `lbd`
- `halberd`

## 3. Analyzing Web Applications

After gathering information about the infrastructure, the next step is analyzing the web application itself.

This stage focuses on identifying application components, technologies, input points, and potential vulnerabilities.

### 3.1 Identifying User Input Points

User input points are locations where the application receives data from users.

HTTP headers are also examined during this process.

**Tools:**
- Burp Suite
- OWASP ZAP

### 3.2 Identifying Server-Side Technologies

This stage involves identifying technologies used by the web server and application.

The analysis may include:

- HTML source code.
- URLs.
- Error pages.
- Session information.

**Tools:**
- Nmap
- httprint

### 3.3 Identifying Website Files and Directories

This stage involves discovering files and directories available on the web server.

The analysis includes checking:

- Directory listing functionality.
- Sensitive directories.
- Available files and resources.

**Tools:**
- dirb
- Nmap
- Gobuster

### 3.4 Identifying Web Vulnerabilities

The final part of application analysis involves identifying known vulnerabilities in the web application.

**Tools:**
- Acunetix
- Nessus
- Vega

## 4. Bypassing Client-Side Controls

Web applications use client-side controls to manage user input and interactions.

Developers may assume that these controls cannot be bypassed. However, client-side controls can be inspected and manipulated before data reaches the server.

The module describes several approaches:

### 4.1 Attacking Hidden Form Fields

Hidden form fields are elements that are not normally visible to users but are included in web forms.

An attacker may identify and modify these fields before submitting the form to the server.

### 4.2 Inspecting and Modifying Requests

Requests sent from the browser to the server can be intercepted and modified.

Tools such as Burp Suite allow testers to inspect HTTP requests and change their contents before forwarding them.

### 4.3 Reviewing Source Code

Reviewing application source code can help identify:

- User input points.
- Encoding and encryption methods.
- Modifiable application components.
- Hidden form fields.

### 4.4 Bypassing XSS Filters

The module mentions several techniques for attempting to bypass XSS filters:

- Encoding.
- Tag manipulation.
- Using whitespace in script code.

These techniques are related to weaknesses in how applications filter or process potentially malicious input.

## Related Links

- [WHOIS Lookup](https://lookup.icann.org/)
- [Nmap Documentation](https://nmap.org/book/man.html)
- [Netcraft](https://www.netcraft.com/)
- [Wafw00f](https://github.com/EnableSecurity/wafw00f)
- [Burp Suite Documentation](https://portswigger.net/burp/documentation)
- [OWASP ZAP](https://www.zaproxy.org/)
- [Gobuster](https://github.com/OJ/gobuster)
- [Nessus](https://www.tenable.com/products/nessus)

## Summary

This file covered the initial stages of web application hacking methodology.

The process begins with footprinting the web infrastructure, including server discovery, service discovery, server identification, hidden content discovery, and load balancer detection.

It then moves to application analysis and the inspection of client-side controls, where tools such as Nmap, Burp Suite, ZAP, and Gobuster can assist security testers.
