# Network-Scanner
Investigative and categorize what devices are running on a network.

### ARP = ADDRESS RESOLUTION PROTOCOL 

ARP does IP <> MAC address pairing. <br />
Computers need to know both the IP address and the MAC address of a destination before 
they can start network communication. <br />
This mapping procedure is important because the lengths of the IP and MAC addresses 
differ, and a translation is needed so that the systems can recognize one another.  <br />
The ARP cache keeps a list of each IP address and its matching MAC address.  <br />
The ARP cache is dynamic, but users on a network can also configure a static. <br />

* On Kali Linux, there is pre-installed network scanner = netdiscover
* Example to scan own network: netdiscover -r 10.0.2.1/24 
It shows the IP, MAC address together.  <br />
This python file is going to do similar. <br />

#### STEPS
1. ARP Request >> To learn about: scapy.ls(scapy.ARP())
2. Broadcast >>  To learn about: scapy.ls(scapy.Ether())
3. ARP Response

To send an receive packets (sr) : This function is sending packets and receiving answers.  <br />
sr1() is a variant that only returns one packet that answered the packet sent.  <br />
srp() do the same for layer 2 packets.  <br />
timeout= don't wait to get an answer until it comes <br />

 [More about ARP](https://www.fortinet.com/resources/cyberglossary/what-is-arp) <br />
 [More about Scapy](https://scapy.net/) <br />
 [More about Scapy](https://docs.python.org/3/library/optparse.html) <br />

# Usage
Run in terminal: <br />
`python networkscanner.py -i networkaddress` <br />
Example:`python networkscanner.py -i 10.0.2.1/24` <br />
