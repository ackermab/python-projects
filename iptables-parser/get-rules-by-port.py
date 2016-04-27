import os
import re
from itertools import izip, tee

abandonedhosts = set()
abandonedhosts = {"some-host"}

file = open("firewall-rules-forward")

def pairwise(iterable):
	"s - > (s0,s1), (s2,s3), (s4,s5), ..."
	a = iter(iterable)
	return izip(a, a)

tcpports = set()
udpports = set()
icmpips = set()

tcphosts = set()
udphosts = set()
icmphosts = set()

testports = set()
text = []
for line in file:
	text.append(line)
	array = line.split()
	args = {}

	# Parse line into flag-argument pairs
	for k,v in pairwise(array):
		args[k] = v
	
	# Check if line has destination ports
	if '--dports' in args.keys():
		# If multiple ports, iterate through and add them
		dports = args['--dports'].split(',')
		for dport in dports:
			if 'tcp' in args['-p']:
				tcpports.add(int(dport))
			elif 'udp' in args['-p']:
				udpports.add(int(dport))
	
	# Check if there is only one destination port
	if '--dport' in args.keys():
		# Add single port to tcp or udp ports
		if '--dport' in args.keys():
			if 'tcp' in args['-p']:
				tcpports.add(args['--dport'])
			elif 'udp' in args['-p']:
				udpports.add(args['--dport'])	


	# If the port is icmp, add to list
	if '-p' in args.keys():
		if 'icmp' in args['-p']:
			if '-d' in args.keys():
				icmphosts.add(args['-d'].strip("/32"))

# print("TCP")
# for port in sorted(tcpports):
# 	print(port)
# print("UDP")
# for port in sorted(udpports):
# 	print(port)
# print("ICMP")
# for host in sorted(icmphosts):
# 	print(host)

# Iterate through possible ports and add all hosts
for intport in sorted(tcpports):
	port = str(intport)
	ips = set()
	
	# Iterate each line from the text of the file
	for line in text:

		# If it contains the specific port in its port list add the ip
		regexp = re.compile(r'[,| ]' + port + "[,| ]")
		if regexp.search(line) is not None:
			array = line.split()
			args = {}
	
			for k, v in pairwise(array):
				args[k] = v
			
			if '-d' in args.keys():
				ips.add(args['-d'].strip("/32"))
				
				if ".32" in args['-d']:
					print(">>>>" + args['-d'])

	# Iterate through ips and get host name with system host command
	hosts = {}
	for ip in ips:
		os.system('host %(ip)s | grep -o "[a-z0-9-]*.cs.byu.edu" > host.txt' % locals())
		#os.system('host %(ip)s' % locals())
	
		# Read from file the host command redirected the input to
		file = open("host.txt")
		host = file.readline().strip()

		host2 = file.readline().strip()
	
		# Fix issues with pathgen hosts with multiple ips
		if "pathgen" in host:
			hosts[host2] = ip
		elif host != "":
			hosts[host] = ip

	print("\nHosts with open TCP port " + port)
	print("==================================")
	if len(hosts.keys()) is 0:
		print ("")
	for host, ip in hosts.iteritems():
		parts = host.split(".")
		if parts[0] not in abandonedhosts:
			print(host)

for intport in sorted(udpports):
	port = str(intport)
	ips = set()
       
	# Iterate each line from the text of the file
	for line in text:

		# If it contains the specific port in its port list add the ip
		regexp = re.compile(r'[,| ]' + port + "[,| ]")
		if regexp.search(line) is not None:
			array = line.split()
			args = {}

			for k, v in pairwise(array):
				args[k] = v

			if '-d' in args.keys():
				ips.add(args['-d'].strip("/32"))
        
				if ".32" in args['-d']:
					print("=====" + args['-d'])

	# Iterate through ips and get host name with system host command
	hosts = {}
	for ip in ips:
		os.system('host %(ip)s | grep -o "[a-z0-9-]*.cs.byu.edu" > host.txt' % locals())
		#os.system('host %(ip)s' % locals())

		# Read from file the host command redirected the input to
		file = open("host.txt")
		host = file.readline().strip()

		host2 = file.readline().strip()

		# Fix issues with pathgen hosts with multiple ips
		if "pathgen" in host:
			hosts[host2] = ip
		elif host != "":
			hosts[host] = ip

	print("\nHosts with open UDP port " + port)
	print("==================================")
	if len(hosts.keys()) is 0:
		print ("")
	for host, ip in hosts.iteritems():
		parts = host.split(".")
		if parts[0] not in abandonedhosts:
			print(host)

print("\nHosts with open ICMP port")
print("==================================")
hosts = {}
for ip in icmphosts:
	os.system('host %(ip)s | grep -o "[a-z0-9-]*.cs.byu.edu" > host.txt' % locals())
	#os.system('host %(ip)s' % locals())

	# Read from file the host command redirected the input to
	file = open("host.txt")
	host = file.readline().strip()
	host2 = file.readline().strip()

	if "." in host:
		parts = host.split(".")
		if parts[0] not in abandonedhosts:
			print(host)
	# # Fix issues with pathgen hosts with multiple ips
	# if "pathgen" in host:
	# 	hosts[host2] = ip
	# elif host != "":
	# 	hosts[host] = ip

	# if len(hosts.keys()) is 0:
	# 	print ("NONE")
	# else:
	# 	print(host)
