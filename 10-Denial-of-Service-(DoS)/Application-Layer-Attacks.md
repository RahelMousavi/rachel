
# Application Layer Attacks

## Introduction

**Application Layer attacks** target the resources of an application or service.

Their objective is to consume the resources required to process application requests, making the application unavailable to legitimate users.

These attacks are measured in:

- **RPS (Requests Per Second):** The number of requests sent per second.

## 1. HTTP GET/POST Attacks

HTTP clients, such as web browsers, communicate with web servers using the HTTP protocol.

Two common HTTP request methods are:

- **GET:** Used to request information from a server.
- **POST:** Used to send data to a server.

The course describes two forms of HTTP-based attacks:

### HTTP GET Attack

In the HTTP GET attack described in the course, a time delay is introduced in the HTTP header to keep HTTP connections open.

Keeping these connections active consumes web server resources and may reduce the resources available for legitimate users.

### HTTP POST Attack

In an HTTP POST attack, the attacker sends HTTP requests with complete headers but incomplete message bodies.

The server waits for the remaining part of the message, keeping the connection open and consuming server resources.

## 2. Slowloris Attack

**Slowloris** is a tool used to perform Layer 7 DDoS attacks.

One characteristic that distinguishes Slowloris from other attack tools is that it uses legitimate and valid-looking HTTP traffic to disrupt a web server.

### How It Works

1. The attacker sends incomplete HTTP requests to the target server.
2. The server assumes that the requests are still being transmitted.
3. The server keeps the connections open while waiting for the remaining request data.
4. The requests are never completed.
5. The server's maximum capacity for simultaneous connections becomes occupied.
6. New legitimate connections may be rejected.

The attack attempts to exhaust the server's available connection capacity without relying on large volumes of traffic.

## 3. UDP Application Layer Flood

A **UDP Application Layer Flood** uses application-layer protocols that operate over UDP.

The course lists the following examples:

- CharGEN
- SNMPv2
- QOTD
- RPC
- SSDP
- CLDAP
- TFTP
- NetBIOS
- NTP
- Quake Network Protocol
- Steam Protocol
- VoIP

These protocols can be involved in UDP-based application-layer flooding.

## Summary

- **HTTP GET/POST Attacks:** Keep server connections occupied by delaying or incompletely transmitting HTTP requests.
- **Slowloris:** Sends incomplete HTTP requests and keeps connections open, exhausting the server's simultaneous connection capacity.
- **UDP Application Layer Flood:** Uses UDP-based application protocols to generate traffic toward a target.

## Related Links

- [Cloudflare — HTTP Flood Attack](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/)
- [Cloudflare — What Is Slowloris?](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/)
- [Cloudflare — Application Layer DDoS Attacks](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/)
- [IANA — Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
