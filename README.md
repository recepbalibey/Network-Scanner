# Network-Scanner
Investigative and categorize what devices are running on a network.

# ARP = ADDRESS RESOLUTION PROTOCOL 

ARP does IP <> MAC address pairing.
computers need to know both the IP address and the MAC address of a destination before 
they can start network communication.
This mapping procedure is important because the lengths of the IP and MAC addresses 
differ, and a translation is needed so that the systems can recognize one another. 
The ARP cache keeps a list of each IP address and its matching MAC address. 
The ARP cache is dynamic, but users on a network can also configure a static.

On Kali Linux, there is pre-installed network scanner = netdiscover
Example to scan own network: netdiscover -r 10.0.2.1/24 
It shows the IP, MAC address together. 
This python file is going to do similar.

STEPS
1. ARP Request >> To learn about: scapy.ls(scapy.ARP())
2. Broadcast >>  To learn about: scapy.ls(scapy.Ether())
3. ARP Response

To send an receive packets (sr) : This function is sending packets and receiving answers.
sr1() is a variant that only returns one packet that answered the packet sent. 
srp() do the same for layer 2 packets. 
timeout= don't wait to get an answer until it comes
