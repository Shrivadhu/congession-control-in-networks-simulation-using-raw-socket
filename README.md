🌐 CWND Simulation and Packet Sniffer
Packet Sniffer Setup:

Uses raw sockets to listen to incoming network packets, capturing IP headers and their protocols (ICMP, TCP, UDP).

Congestion Window (CWND) Simulation:

Dynamically adjusts the CWND based on the protocol and packet size:

ICMP: Reduces CWND.

TCP: Increases CWND for larger packets, decreases for smaller ones.

UDP: Gradual increase of CWND.

Protocol Handling:

Identifies and processes different protocols:

ICMP: Used for ping-like communications.

TCP: For reliable transport layer, adjusts CWND based on size.

UDP: For faster, connectionless communication, adjusting CWND more conservatively.

Real-Time CWND Adjustment:

Adjusts and prints the current CWND value dynamically for each captured packet in real-time.

Throughput Metric:

Counts and displays the number of packets captured every 10 seconds, providing a throughput metric.

Customizable Simulation Parameters:

Adjustable MIN_CWND and MAX_CWND values for different network conditions.





![WhatsApp Image 2025-04-21 at 23 39 51_b5c38985](https://github.com/user-attachments/assets/aeadab7a-7bb5-4c4b-bf8f-19b21603e00a)



![image](https://github.com/user-attachments/assets/c1d7fc0c-3e58-4e8c-8719-675e5995ec8a)



