import sys
from scapy.all import sr1, IP, ICMP, TCP


def icmp_probe(ip):
    icmp_packet = IP(dst=ip)/ICMP()
    resp_packet = sr1(icmp_packet)
    return resp_packet is not None


def syn_scan(ip, port, verbose=False):
    syn_packet = IP(dst=ip)/TCP(dport=port, flags='S')
    resp_packet = sr1(syn_packet)
    if verbose:
        print(resp_packet.show())
    return resp_packet['TCP'].flags == 'SA'  # == 0x12 (0x02 == SYN + 0x10 == ACK)


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    if icmp_probe(ip):
        if syn_scan(ip, port):
            print(f'{port} => open')
    else:
        print(f'PING Failed!')
