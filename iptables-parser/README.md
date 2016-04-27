# A simple limited parser for iptables rules
### Written in python3

#### get-rules-by-port.py
This script simply takes a file (set in script) and parses the lines.
It will grab all rules and sort them by protocol and port
It will then run a host command on the system to convert the IP to a FQDN.

If the hostname is in the list of abandoned hosts, it will not print it.


The original purpose of this script was to assist in converting from an iptables firewall to pfsense.
