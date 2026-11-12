
# DoS/DDoS Attack Tools

## Introduction

DoS/DDoS tools are software applications designed to generate network traffic or requests for evaluating, testing, or disrupting the availability of systems and services.

The course introduces the following tools:

1. UltraDDOS-v2
2. High Orbit Ion Cannon (HOIC)
3. Low Orbit Ion Cannon (LOIC)
4. HULK (HTTP Unbearable Load King)
5. Slowloris
6. UFONet
7. Packet Flooder Tool

## 1. UltraDDOS-v2

**UltraDDOS-v2** is a Windows-based utility presented in the course as a DoS/DDoS tool.

It is associated with generating network traffic against a target. The course lists the tool but does not explain its internal mechanisms.

## 2. High Orbit Ion Cannon (HOIC)

**HOIC** stands for **High Orbit Ion Cannon**.

It is an HTTP-based traffic generation tool associated with DDoS attacks.

Its general characteristics include:

- Generating large numbers of HTTP requests.
- Supporting HTTP GET and POST requests.
- Using configurable boosters to modify request characteristics.

## 3. Low Orbit Ion Cannon (LOIC)

**LOIC** stands for **Low Orbit Ion Cannon**.

It is an open-source network stress-testing tool that can generate different types of network traffic.

Its commonly documented traffic modes include:

- TCP
- UDP
- HTTP

LOIC has also been associated with coordinated DDoS campaigns.

## 4. HULK (HTTP Unbearable Load King)

**HULK** stands for **HTTP Unbearable Load King**.

It is an HTTP-based DoS tool designed to generate large numbers of requests against web servers.

Unlike ordinary repeated requests, HULK generates varied HTTP requests to increase the processing workload on the target web server.

## 5. Slowloris

**Slowloris** is an application-layer DoS tool that targets web servers by keeping multiple HTTP connections open.

Its general characteristics include:

- Sending incomplete HTTP requests.
- Keeping connections active for extended periods.
- Consuming the server's available connection capacity.
- Requiring relatively little traffic compared with volumetric attacks.

Slowloris is particularly associated with HTTP connection exhaustion.

## 6. UFONet

**UFONet** is a framework associated with application-layer DDoS attacks.

It uses HTTP-based techniques and provides functionality for coordinating traffic sources.

It is designed to target web applications and services rather than simply generating large volumes of arbitrary network packets.

## 7. Packet Flooder Tool

A **Packet Flooder Tool** is a general category of software used to generate large numbers of network packets.

The course displays a packet-generation interface with support for different protocols, including:

- TCP
- UDP
- ICMP

Such tools can be used in authorized network testing to evaluate how systems and network devices handle high packet volumes.

## Summary

| Tool | General Purpose |
|---|---|
| UltraDDOS-v2 | DoS/DDoS traffic generation |
| HOIC | HTTP-based traffic generation |
| LOIC | TCP, UDP, and HTTP traffic generation |
| HULK | HTTP request flooding |
| Slowloris | HTTP connection exhaustion |
| UFONet | Application-layer DDoS framework |
| Packet Flooder Tool | Network packet generation |

**Security Note:** These tools can disrupt services and affect network availability. Any testing must be restricted to systems you own or have explicit authorization to test, preferably within an isolated lab environment. Avoid downloading old or unofficial executables from untrusted sources.

## Related Links

- [DFN-CERT — Details of Selected DDoS Attacks](https://www.dfn-cert.de/documents/83/details_of_selectes_DDos.pdf)
- [Cloudflare — DDoS Attack Tools](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/)
- [GitHub — Slowloris Project](https://github.com/gkbrk/slowloris)
- [GitHub — UFONet Project](https://github.com/epsylon/ufonet)
- [BlackArch — DoS Tools](https://blackarch.org/dos.html)
