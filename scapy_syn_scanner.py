import sys
from scapy.all import sr1, IP, ICMP, TCP


def icmp_probe(ip):
    icmp_packet = IP(dst=ip)/ICMP()
    resp_packet = sr1(icmp_packet)
    return resp_packet is not None


def syn_scan(ip, port):
    syn_packet = IP(dst=ip)/TCP(dport=port, flags='S')
    resp_packet = sr1(syn_packet)
    print(resp_packet.show())
    print('CHECK: ', resp_packet['TCP'].flags == 'SA')


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    if icmp_probe(ip):
        syn_scan(ip, port)
    else:
        print(f'PING Failed!')
