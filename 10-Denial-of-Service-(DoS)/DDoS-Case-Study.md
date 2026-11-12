
# DDoS Case Study

## Introduction

Studying real-world DDoS attacks helps us understand how these attacks affect large-scale services and how organizations respond to them.

This section examines two major DDoS incidents involving Google and GitHub.

## 1. DDoS Attack Against Google (2023)

In September 2023, Google reported that it had successfully mitigated a massive DDoS attack that reached **398 million requests per second (RPS)**.

The attack used a technique known as **HTTP/2 Rapid Reset**, which targeted websites, Internet services, and infrastructure.

### Attack Technique: HTTP/2 Rapid Reset

The attack exploited the stream multiplexing feature of the HTTP/2 protocol.

HTTP/2 allows multiple independent streams to be managed over a single TCP connection.

The attack took advantage of this capability by repeatedly sending requests and immediately resetting them.

This caused servers and other infrastructure components to process a large number of requests, even though the requests were quickly canceled.

### Google's Response

After analyzing the attack, Google took several defensive measures:

- Updated its defense systems and proxies.
- Worked closely with other cloud service providers and maintainers of HTTP/2-based software.
- Shared threat intelligence in real time.
- Published mitigation solutions to help other providers.
- Developed security patches and new mitigation methods for proxies, application servers, and load balancers.

### Vulnerability Identification

The vulnerability associated with HTTP/2 Rapid Reset was registered as:

- **CVE:** CVE-2023-44487
- **CVSS Score:** 7.5 out of 10
- **Severity:** High

## 2. DDoS Attack Against GitHub (2018)

In February 2018, GitHub experienced one of the largest DDoS attacks recorded at that time.

The attack disrupted access to GitHub services for several minutes.

### Attack Timeline

The attack occurred on Wednesday, February 28, 2018.

According to the course material:

- GitHub.com was unavailable from 17:21 to 17:26 UTC.
- The service experienced intermittent availability from 17:26 to 17:30 UTC.
- The first wave reached approximately 1.35 Tbps and 126.9 million packets per second.
- A second wave reached approximately 400 Gbps after 18:00 UTC.

### Attack Sources

The attack originated from:

- More than 1,000 independent Autonomous System Numbers (ASNs).
- Tens of thousands of unique endpoints.

This demonstrates how a distributed attack can generate enormous amounts of traffic from many different networks and devices.

### Impact

The attack temporarily disrupted access to GitHub.com.

Users were unable to reliably access the service during the incident.

The incident demonstrated the importance of having sufficient network capacity, traffic monitoring, and DDoS mitigation infrastructure.

## 3. Lessons Learned

These two incidents demonstrate several important points:

- **Large-scale attacks:** DDoS attacks can generate hundreds of millions of requests per second or traffic volumes measured in terabits per second.
- **Protocol weaknesses:** Features designed to improve protocol efficiency can sometimes be exploited to disrupt services.
- **Distributed attack sources:** Attack traffic can originate from thousands of independent networks and many endpoints.
- **Continuous monitoring:** Detecting unusual traffic patterns is important for identifying attacks.
- **Coordinated response:** Sharing threat intelligence and working with other service providers can improve mitigation efforts.
- **Infrastructure protection:** Proxies, load balancers, and DDoS protection systems play an important role in maintaining service availability.

## Summary

This case study examined two major DDoS incidents:

- **Google (2023):** An HTTP/2 Rapid Reset attack that reached 398 million requests per second and was mitigated through Google's defense infrastructure and coordinated security improvements.
- **GitHub (2018):** A large-scale volumetric DDoS attack that reached approximately 1.35 Tbps and temporarily disrupted GitHub's availability.

Both incidents demonstrate the scale and complexity of modern DDoS attacks and the importance of effective detection, mitigation, and incident response.

## Related Links

- [Google Cloud — Google Mitigated the Largest DDoS Attack to Date](https://cloud.google.com/blog/products/identity-security/google-cloud-mitigated-largest-ddos-attack-peaking-above-398-million-rps)
- [Google Cloud — How HTTP/2 Rapid Reset Works](https://cloud.google.com/blog/products/identity-security/how-it-works-the-novel-http2-rapid-reset-ddos-attack)
- [GitHub — February 28th DDoS Incident Report](https://github.blog/news-insights/company-news/ddos-incident-report/)
- [NIST — National Vulnerability Database: CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487)
