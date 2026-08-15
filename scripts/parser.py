import pyshark

def load_packets(pcap_file):
        
        print(f"Loading packets from {pcap_file}...")

        capture = pyshark.FileCapture(pcap_file)

        packets = []

        for pkt in capture:         # It can also be written as
            packets.append(pkt)     # packets = [pkt for pkt in capture]

        capture.close()

        print(f"Total packets loaded: {len(packets)}")
        
        return packets