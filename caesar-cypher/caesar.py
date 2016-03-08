#!/usr/bin/python3

import sys, getopt, string

def main(argv):
	inputfile = ''
	cycles = ''
	try:
		opts, args = getopt.getopt(argv,"hi:c:",["ifile=","cycle-count"])
	except getopt.GetoptError:
		print('caesar.py -i <inputfile> -c <cycle-count>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('caeser.py -i <inputfile> -c <cycle-count>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-c", "--cycle-count"):
			cycles = int(arg)

	ifile = open(inputfile)
	print('Reading file:', inputfile)
	content = ifile.read()
	# Remove EOF from file content string
	content = content[:-1]
	print('Content     :', content)
	ifile.close()

	alpha = string.ascii_uppercase
	cypher = ''
	for c in content:
		if (c.isalpha()):
			c = c.upper()
			index = alpha.index(c)
			index = (index - cycles) % len(alpha)
			cypher = cypher + alpha[index]
		else:
			cypher = cypher + c
	print('Cypher      :', cypher)

if __name__ == "__main__":
	main(sys.argv[1:])
