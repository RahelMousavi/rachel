
# 02 — Application-Level Session Hijacking

## 1. Introduction

**Application-Level Session Hijacking** occurs when an attacker steals or predicts a valid session token to gain unauthorized access to a web server or create an unauthorized session.

This type of attack mainly targets HTTP sessions.

The attacker attempts to compromise a user's **Session ID**, which is used by the web application to identify an authenticated session.

## 2. Session ID Stealing, Guessing, and Brute Forcing

There are three methods introduced in the course for compromising Session IDs.

### 2.1 Session ID Stealing

In this method, the attacker obtains a valid Session ID using different techniques, such as:

- Gaining physical access to files containing Session IDs.
- Extracting information from server or client memory.
- Sniffing network traffic to capture Session IDs.

Once obtained, the attacker may use the stolen identifier to impersonate the legitimate user.

### 2.2 Session ID Guessing

In this method, the attacker observes session patterns and attempts to predict a valid Session ID.

This attack may succeed when:

- Session IDs are short.
- Session IDs follow predictable patterns.
- Weak algorithms are used to generate identifiers.

### 2.3 Session ID Brute Forcing

In a **Brute Force** attack, the attacker attempts different possible combinations of Session IDs until a valid one is found.

This method is more feasible when session identifiers have a small number of possible combinations.

## 3. Obtaining Session IDs Using Sniffing

**Sniffing** is a technique used to capture and inspect network packets.

In Session Hijacking, an attacker may monitor communication between a legitimate client and a web server to obtain a Session ID.

If the session identifier is transmitted without adequate encryption, it may be exposed to attackers monitoring the network.

After obtaining a valid Session ID, the attacker may attempt to use it to access the victim's session.

## 4. Predictable Session IDs

Some web servers use custom algorithms or predictable patterns to generate session identifiers.

If these identifiers are not sufficiently random, an attacker may analyze previously observed Session IDs and attempt to predict future ones.

For example, a Session ID generated using predictable values such as dates, timestamps, or sequential numbers may be easier to guess.

A secure session management system should use sufficiently long and unpredictable session identifiers.

## 5. Man-in-the-Browser Attacks

**Man-in-the-Browser (MitB)** is an attack that uses a Trojan to intercept and manipulate communication between a web browser and its security mechanisms or libraries.

In this attack:

1. A Trojan is installed on the victim's system.
2. The Trojan operates between the browser and its security mechanisms.
3. It can modify web pages and transaction content.
4. It may insert additional transactions without the user's knowledge.

The Trojan's activities may remain invisible to both the user and the web application.

The primary objective described in the course is financial theft through the manipulation of transactions performed using Internet banking systems.

## 6. Client-Side Attacks

**Client-Side Attacks** target vulnerabilities in applications running on the user's system.

Depending on the vulnerabilities, an attacker may use a malicious email link or trick a user into visiting a malicious website.

The course identifies the following vulnerable components:

- Unprotected websites
- Java Runtime Environment (JRE)
- Web browsers

Browsers are considered the primary target among these components.

Three techniques mentioned in the course are:

### 6.1 Cross-Site Scripting (XSS)

**Cross-Site Scripting (XSS)** is a vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users.

Depending on the vulnerability, these scripts may be used to access sensitive information or compromise session data.

### 6.2 Malicious JavaScript (Mal-JS)

**Mal-JS** refers to malicious JavaScript code used to perform unwanted actions in a victim's browser.

It may be delivered through malicious websites or compromised web content.

### 6.3 Trojan

A **Trojan** is malicious software that disguises itself as legitimate software.

In client-side attacks, a Trojan may compromise the user's system or browser and provide an attacker with access to sensitive information.

## 7. Session Fixation

**Session Fixation** is an attack in which an attacker causes a victim to use a session identifier that is already known to the attacker.

The course diagram illustrates the following process:

1. The attacker sends the victim a link containing a predefined Session ID.
2. The victim clicks the link and logs in to a vulnerable web server.
3. The attacker attempts to log in using the same Session ID.
4. Because the session identifier is shared, the attacker may gain access to the victim's authenticated session.

The main weakness is that the application does not generate a new session identifier after successful authentication.

**Important:** Regenerating the Session ID after login is an essential defense against Session Fixation.

## 8. Session Hijacking Using CRIME Attack

### 8.1 What Is CRIME?

**CRIME** stands for **Compression Ratio Info-leak Made Easy**.

It is a client-side attack that exploits vulnerabilities in data compression mechanisms used with protocols such as SPDY and SSL/TLS.

According to the course, the attack takes advantage of the compression of data before encryption.

### 8.2 How CRIME Works

The course describes the following process:

1. A user establishes an HTTPS connection with a web server, creating a TLS session.
2. Websites commonly use cookies for user authentication.
3. Before encryption, cookies may be compressed using lossless compression algorithms such as DEFLATE.
4. The attacker tricks the victim into clicking a malicious link or visiting a malicious website.
5. Malicious code is used to generate requests and observe differences in their compressed sizes.
6. The attacker attempts to infer cookie information from these differences.

The course also mentions techniques such as **ARP Spoofing** for intercepting network traffic when the victim already has an HTTPS connection established.

### 8.3 Main Objective

The main objective of CRIME is to extract sensitive information, particularly authentication cookies, by exploiting information leaked through compression behavior.

**Note:** CRIME is a historical attack associated with TLS/SPDY compression. The course describes its attack model; modern TLS configurations and browser implementations have changed significantly since its discovery.

## Summary

Application-Level Session Hijacking targets web sessions, particularly HTTP sessions, by compromising session identifiers or manipulating browser activity.

The main techniques covered in this section are:

- **Session ID Stealing:** Obtaining an existing session identifier.
- **Session ID Guessing:** Predicting a valid identifier based on observable patterns.
- **Brute Forcing:** Trying possible Session ID combinations.
- **Sniffing:** Capturing session information from network traffic.
- **Predictable Session IDs:** Exploiting weak session identifier generation.
- **Man-in-the-Browser:** Using a Trojan to intercept and manipulate browser activity.
- **Client-Side Attacks:** Exploiting browser and client application vulnerabilities.
- **Session Fixation:** Forcing a victim to use an attacker-known Session ID.
- **CRIME:** Exploiting compression-related information leakage.

## Related Links

- [OWASP — Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [OWASP — Session Fixation](https://owasp.org/www-community/attacks/Session_fixation)
- [OWASP — Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)
- [RFC 7457 — Summarizing Known Attacks on TLS and DTLS](https://www.rfc-editor.org/rfc/rfc7457)
- [MITRE ATT&CK — Man-in-the-Browser](https://attack.mitre.org/techniques/T1185/)
