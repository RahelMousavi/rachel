
# TCP Flags

TCP Flags are control bits in the TCP header that determine how a TCP connection is established, managed, and terminated.

Each flag has a specific purpose in controlling communication between network hosts.

## Types of TCP Flags

### 1. URG (Urgent)

Indicates that the Urgent Pointer field is significant and urgent data should be processed accordingly.

### 2. ACK (Acknowledgment)

Indicates that the Acknowledgment Number field is valid and acknowledges received data.

### 3. PSH (Push)

Requests that buffered data be delivered to the receiving application without unnecessary delay.

### 4. RST (Reset)

Resets or immediately terminates a TCP connection.

### 5. SYN (Synchronize)

Initiates a TCP connection and synchronizes sequence numbers between communicating hosts.

### 6. FIN (Finish)

Indicates that the sender has finished transmitting data and wants to close its sending direction of the TCP connection.

## TCP Header Structure

The TCP header contains several fields used to manage communication between hosts:

- **Source Port:** Identifies the sending application's port.
- **Destination Port:** Identifies the receiving application's port.
- **Sequence Number:** Identifies the position of data in the TCP stream.
- **Acknowledgment Number:** Specifies the next sequence number expected from the other host.
- **Data Offset:** Specifies the length of the TCP header.
- **Reserved:** Contains bits reserved for future use.
- **TCP Flags:** Control connection establishment, communication, and termination.
- **Window:** Specifies the amount of data the receiver is willing to accept.
- **TCP Checksum:** Helps detect errors in the TCP header and data.
- **Urgent Pointer:** Indicates the end of urgent data when the URG flag is set.
- **Options:** Contains optional TCP parameters.

# TCP/IP Communication

TCP (Transmission Control Protocol) is a connection-oriented transport layer protocol.

Before transmitting data, TCP establishes a connection between the client and server. When communication is finished, the connection is normally terminated through an exchange of control packets.

TCP communication involves two important processes:

1. TCP Session Establishment (Three-Way Handshake).
2. TCP Session Termination.

## 1. TCP Three-Way Handshake

The Three-Way Handshake is the process used to establish a TCP connection between a client and a server.

It consists of three steps:

### Step 1: SYN

The client sends a TCP packet with the SYN flag set to request a connection with the server.

### Step 2: SYN-ACK

The server responds with a packet containing both SYN and ACK flags to acknowledge the client's request and synchronize its own sequence number.

### Step 3: ACK

The client sends an ACK packet to acknowledge the server's response.

After these three steps, the TCP connection is established and data transmission can begin.

## 2. TCP Session Termination

TCP connection termination normally uses a four-step process involving FIN and ACK flags.

### Step 1: FIN

The client sends a FIN packet to indicate that it has finished transmitting data.

### Step 2: ACK

The server acknowledges the client's termination request by sending an ACK packet.

### Step 3: FIN

The server sends its own FIN packet when it has finished transmitting data.

### Step 4: ACK

The client acknowledges the server's FIN packet, completing the normal connection termination process.

## Summary

TCP Flags control different aspects of TCP communication.

The six main flags covered in this section are:

- **URG:** Indicates urgent data.
- **ACK:** Acknowledges received data.
- **PSH:** Requests immediate delivery of buffered data to the application.
- **RST:** Resets a connection.
- **SYN:** Establishes and synchronizes a connection.
- **FIN:** Indicates that the sender has finished transmitting data.

TCP uses the Three-Way Handshake to establish connections and normally uses a four-step FIN/ACK exchange to terminate them.

## Related Links

- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html) — Official TCP specification, including TCP header fields, flags, connection establishment, and termination.
- [Wireshark — TCP Three-Way Handshake](https://wiki.wireshark.org/TCP_3_way_handshaking) — Explains the TCP connection establishment process with packet examples.
- [Wireshark](https://www.wireshark.org/) — Network protocol analyzer useful for examining TCP packets, flags, sequence numbers, and acknowledgments.
- [IANA — TCP Parameters](https://www.iana.org/assignments/tcp-parameters/tcp-parameters.xhtml) — Official registry of TCP header parameters and flags.

