import socket
import struct
import time

# CWND Simulation Parameters
cwnd = 10
MIN_CWND = 1
MAX_CWND = 50

def adjust_cwnd(protocol, size):
    global cwnd
    if protocol == 1:  # ICMP
        cwnd = max(MIN_CWND, cwnd - 1)
    elif protocol == 6:  # TCP
        if size > 1000:
            cwnd = min(MAX_CWND, cwnd + 2)
        else:
            cwnd = max(MIN_CWND, cwnd - 1)
    elif protocol == 17:  # UDP
        cwnd = min(MAX_CWND, cwnd + 1)
    else:
        pass  # unknown protocol
    return cwnd

# Create raw socket
try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    print("✅ Raw socket created. Listening...\n")
except socket.error as msg:
    print(f"❌ Failed to create socket: {msg}")
    exit()

# Packet listener loop
packet_count = 0
start_time = time.time()

while True:
    try:
        packet, _ = s.recvfrom(65565)

        # Extract IP header
        ip_header = packet[14:34]
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

        version_ihl = iph[0]
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])

        # Adjust CWND based on packet
        pkt_len = len(packet)
        cwnd = adjust_cwnd(protocol, pkt_len)

        # Print result
        print(f"📦 {s_addr} → {d_addr} | Protocol: {protocol} | Length: {pkt_len} | 🧠 CWND: {cwnd}")

        # Count packet for throughput metric
        packet_count += 1

        # Print stats every 10 seconds
        if time.time() - start_time > 10:
            print(f"\n⏱️ Packets captured in 10s: {packet_count}, Final CWND: {cwnd}\n")
            start_time = time.time()
            packet_count = 0

    except KeyboardInterrupt:
        print("\n🛑 Sniffer + CWND simulation stopped.")
        break
