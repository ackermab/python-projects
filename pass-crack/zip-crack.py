import zipfile, optparse
from threading import Thread

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print("[+] Password Found: " + password)
	except:
		pass	

def main():
	parser = optparse.OptionParser("usage%prog -f <zipFile> -d <dictionaryFile>")
	parser.add_option('-f', dest='zipFile', type='string', help='specify zip file')
	parser.add_option('-d', dest='dictionaryFile', type='string', help='specify dictionary file')
	(options, args) = parser.parse_args()

	if (options.zipFile == None) | (options.dictionaryFile == None):
		print(parser.usage)
		exit(0)
	else:
		zipFile = options.zipFile
		dictionaryFile = options.dictionaryFile

	zFile = zipfile.ZipFile(zipFile)
	passFile = open(dictionaryFile)

	for line in passFile.readlines():
		password = line.strip("\n")
		t = Thread(target=extractFile, args=(zFile, password.encode('utf-8')))
		t.start()

if __name__ == "__main__":
	main()
