
# Email Header Analysis

An email header contains technical information about an email message and its transmission between mail servers.

Analyzing email headers is an important Footprinting technique because it can reveal information about the sender, mail servers, message routing, and email authentication mechanisms.

## Information Found in Email Headers

### 1. Received From

Shows the address or mail server from which the message was received.

### 2. Received Date and Time

Indicates when the message was received by a mail server.

### 3. Sender's IP Address

May reveal the IP address of a system involved in sending the email.

**Note:** The visible IP address may belong to a mail server or intermediary rather than the sender's personal device.

### 4. Return-Path

Specifies the address used for handling bounced or undeliverable messages.

### 5. Mail Server

Identifies the mail server involved in processing or delivering the message.

### 6. Authentication Results

Contains the results of email authentication checks, such as SPF, DKIM, and DMARC.

### 7. Sender's Name

The `From` field may contain the sender's display name and email address.

### 8. Date

The `Date` field indicates when the sender's email client created or sent the message.

### 9. Message-ID

A unique identifier assigned to an email message, usually by the sending mail system.

### 10. Subject

Contains the subject line of the email.

### 11. To

Specifies the intended recipient's email address.

## Email Authentication Mechanisms

### SPF (Sender Policy Framework)

SPF allows domain owners to specify which mail servers are authorized to send emails on behalf of their domain.

### DKIM (DomainKeys Identified Mail)

DKIM uses a digital signature to help verify that an email was authorized by the sending domain and that signed content has not been modified.

### DMARC (Domain-based Message Authentication, Reporting, and Conformance)

DMARC defines how receiving mail servers should handle messages that fail SPF and DKIM checks and provides reporting capabilities.

## Role in Footprinting

Email Header Analysis can help security researchers:

- Identify mail servers used by an organization.
- Examine email routing information.
- Identify IP addresses associated with mail infrastructure.
- Analyze email authentication configurations.
- Investigate suspicious or potentially spoofed emails.

## Summary

Email Header Analysis involves examining the technical metadata of an email to understand its origin, routing, and authentication.

It can reveal information such as sender addresses, mail servers, IP addresses, timestamps, and authentication results.

**Important:** Email headers can contain misleading or forged information. Header fields should be interpreted carefully, and trusted server-added fields should be distinguished from sender-controlled fields.
