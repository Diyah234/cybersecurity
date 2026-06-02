

from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

# Suspicious ports to flag
SUSPICIOUS_PORTS = [4444, 8080, 23, 1337, 9001]

log_file = open("capture_log.txt", "a")

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    log_file.write(line + "\n")

def analyze_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

        if ICMP in packet:
            log(f"ICMP | {src} --> {dst}")

        elif TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            flag = " ⚠️  SUSPICIOUS PORT!" if dport in SUSPICIOUS_PORTS else ""
            log(f"TCP  | {src}:{sport} --> {dst}:{dport}{flag}")

        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            log(f"UDP  | {src}:{sport} --> {dst}:{dport}")

log("=== Sniffer Started ===")
print("Sniffing traffic... Press Ctrl+C to stop\n")

try:
    sniff(prn=analyze_packet, store=False)
except KeyboardInterrupt:
    log("=== Sniffer Stopped ===")
    log_file.close()
    print("\nLog saved to capture_log.txt")
