import crypt

# Takes a password and hashes a dictionary to look for match
def crackPass(cryptPass):
	# Selects a salt that is the first to chars of the word
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt','r')
	
	# Reads through the dictionary file
	for word in dictFile.readlines():
		word = word.strip('\n')

		# Encrypt word with salt
		cryptWord = crypt.crypt(word, salt)
		
		print("Checking - " + word + ": " + cryptWord + " == " + cryptPass)
		
		# Checks if pass matches dictionary word
		if (cryptWord == cryptPass):
			print("[+] Found Password: " + word + "\n")
			return

	print("[-] Password Not Found\n")
	return

def main():
	passFile = open('passwords.txt')

	# Read password file
	for line in passFile.readlines():

		# Split user:pass and crack each password
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print("[*] Cracking Password For: " + user)
			crackPass(cryptPass)

if __name__ == "__main__":
	main()
