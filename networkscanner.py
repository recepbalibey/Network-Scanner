import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address",help="Provide the network address! (Example: python networkscanner.py -i 10.0.2.1/24)")
    (user_input, arguments) = parse_object.parse_args()

    if not user_input.ip_address:
    	print("You need to provide the network address. (Example 10.0.2.1/24")
    return user_input	

def scanner(ip):
	arp_request_packet = scapy.ARP(pdst=ip)
	arp_broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

	arp_combined_packet = arp_broadcast_packet/arp_request_packet

	(answered_list, unanswered_list) = scapy.srp(arp_combined_packet, timeout=1)
	answered_list.summary()

user_ip_address= get_user_input()
scanner(user_ip_address.ip_address)




