
# Webhooks and API Security Testing

## 1. Webhooks

A Webhook allows an application to notify another application when a specific event occurs.

Instead of repeatedly requesting information from a service, an application can receive an update when new information becomes available.

### 1.1 Webhook vs. API Polling

An API can be used to retrieve updated information by sending repeated requests to a service.

For example, imagine that a product is out of stock in an online store. A user may repeatedly check the store to see whether the product is available again.

With API polling, the client sends repeated requests to the service to check for updates.

With a Webhook, the user can request to be notified when the product becomes available. The service then sends a notification when the relevant event occurs.

The main difference is:

- **API Polling:** The client repeatedly requests updated information.
- **Webhook:** The service sends a notification when a specified event occurs.

## 2. Web API Testing Methodology

Web API testing involves evaluating an API to identify potential security weaknesses.

According to the module, the testing methodology consists of four stages:

1. Target Identification
2. Security Standards Identification
3. Attack Surface Identification
4. Launching Attacks

### 2.1 Target Identification

The first stage involves identifying the target API and examining its communication data.

The following elements should be reviewed:

- HTTP headers.
- HTTP message body.

### 2.2 Security Standards Identification

In this stage, the API is examined to determine whether appropriate security standards are being used.

The module discusses SSL and Transport Layer Security as mechanisms for protecting API communication.

Transport security helps provide:

- **Confidentiality:** Protecting information through encryption.
- **Integrity:** Helping ensure that transmitted information has not been modified.

The module also points out that API messages may contain both sensitive and non-sensitive information, and that some information may remain unencrypted.

### 2.3 Attack Surface Identification

Identifying the attack surface of a web application with a graphical user interface is relatively straightforward because input fields are visible on web pages.

However, identifying the attack surface of an API is different because APIs do not necessarily provide a graphical user interface with visible input fields.

Therefore, testers need to identify the API's available endpoints and the data it accepts.

### 2.4 Launching Attacks

After identifying the target, reviewing security standards, and discovering the attack surface, the next stage is launching security tests against the API.

## 3. REST API Vulnerability Scanning

REST APIs may contain security risks similar to those found in traditional web applications and websites.

These risks may include:

- Theft of sensitive data.
- Manipulation of transmitted data.
- Other vulnerabilities that attackers may exploit.

Performing a comprehensive vulnerability scan of REST APIs can help identify security weaknesses.

### 3.1 REST API Scanning Tools

The module introduces the following tools for REST API vulnerability scanning:

- **W3af**
- **Fuzzaoi** (spelling as shown in the source material)
- **Astra**
- **AppSpider**

These tools can be used to assess REST APIs and identify potential vulnerabilities.

## Related Links

- [Webhooks - GitHub Documentation](https://docs.github.com/en/webhooks/about-webhooks)
- [OWASP API Security Project](https://owasp.org/www-project-api-security/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/)
- [W3af](https://github.com/andresriancho/w3af)
- [Astra Security](https://www.getastra.com/)
- [REST API Security - OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)

## Summary

This file covered Webhooks, Web API testing methodology, and REST API vulnerability scanning.

Webhooks provide event-based notifications instead of requiring repeated API requests.

API security testing involves identifying the target, reviewing security standards, discovering the attack surface, and performing security tests. Vulnerability scanning tools can help identify weaknesses in REST APIs.
