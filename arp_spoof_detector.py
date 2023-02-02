#!/usr/bin/python3
# coding: utf-8

from scapy.all import sniff


IP_MAC_Map = {}


def process_packet(packet):
    src_IP = packet['ARP'].psrc
    src_MAC = packet['Ether'].src

    if src_MAC in IP_MAC_Map.keys():
        if IP_MAC_Map[src_MAC] != src_IP:
            try:
                old_IP = IP_MAC_Map[src_MAC]
            except:
                old_IP = 'unknown'

            message = (f'\n Possible ARP Spoofing attack detected \n'
                       f'Its possible that the machine with IP \n'
                       f'{str(old_IP)} it pretending to be {src_IP} \n')
            return message
    else:
        IP_MAC_Map[src_MAC] = src_IP


sniff(count=0, filter='arp', store=0, prn=process_packet)

