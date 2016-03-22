#!/usr/bin/python3
import sys, re

def main(argv):

	if (len(sys.argv) != 2):
		print("Invalid command line arguments")
		print("Try: regex-personal-info.py <filename>")
	else:
		inputfile = argv[0]
	
		phoneRegex = re.compile(r'(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}')
		emailRegex = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b')

		ifile = open(inputfile)
		content = ifile.read()
		ifile.close()

		matchPhone = re.search(phoneRegex, content)
		matchEmail = re.search(emailRegex, content)

		
		print(inputfile)

if __name__ == "__main__":
	main(sys.argv[1:])
