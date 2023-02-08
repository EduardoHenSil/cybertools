from scapy.all import sniff


def process_packet(packet):
    flags = packet['TCP'].flags
    if flags == 'FPU':  # FIN PSH and URG, this is xmas scan
        layer3 = packet['IP']
        print(f'POSSIBLE XMAS SCAN DETECTED from {layer3.src} to {layer3.dst} !!!!!')


if __name__ == '__main__':
    sniff(count=0, filter='tcp', store=0, prn=process_packet)
