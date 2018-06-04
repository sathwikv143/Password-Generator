#!/usr/bin/env python3

import pyAesCrypt as aes
import argparse, time, os, getpass
import string as st
import random as rd

# To check given file already exists
def file_exists(file):
	if os.path.exists(file):
		return True		
	else:
		return False

# Function to Encrypt or Decrypt
def AesEncDec(e):
	ops = ["encrypt","decrypt"]
	OrigFile = "data.txt"
	EncFile = "data.aes"
	bufferSize = 64 * 1024
	if str(e) in ops:
		pas = getpass.getpass("Enter password to encrypt/dycrypt the file(remember): ")
		if str(e) == ops[0]:
			if file_exists(OrigFile):
				print("File {} is not encrypted !!".format(OrigFile))
				aes.encryptFile(OrigFile,EncFile,pas,bufferSize)
				print("File {0} is encrypted as {1} and deleted !!!".format(OrigFile,EncFile))
				os.remove(OrigFile)
				print("Do not delete or rename the encrypted file {}".format(EncFile))
				exit()
			else:
				print("Original File {} does not exist !!".format(OrigFile))
				exit()
		elif str(e) == ops[1]:
			if file_exists(EncFile):
				print("Encrypted file {} exists !!".format(EncFile))
				aes.decryptFile(EncFile,OrigFile,pas,bufferSize)
				print("File {1} is decrypted as {0} and deleted !!!".format(OrigFile,EncFile))
				os.remove(EncFile)
				print("Do not delete or rename the decrypted file {}".format(OrigFile))
				exit()
			else:
				print("Encrypted File {} does not exist !!".format(EncFile))
				exit()
	else:
		exit("\nUse --help/-h option to view the usage of script\n")


# Function to generate random password
def generatePwd(u,l,c,s):
	timecreated = time.asctime( time.localtime(time.time()) )
	f = open("data.txt","a+")
	pwd = ''
	if u != None and s != None:
		if l != None:
			l = int(l)
			if l > len(u):
				pwd = pwd.join(rd.choice(c) for x in range(l))
				f.write("username= "+u+" password= "+pwd+" length= "+str(l)+" site= "+s+" createdOn= "+timecreated+"\n")
				return pwd
			else:
				pwd = pwd.join(rd.choice(c) for x in u)
				f.write("username= "+u+" password= "+pwd+" length= "+str(len(u))+" site= "+s+" createdOn= "+timecreated+"\n")
				return pwd
		else:
			pwd = pwd.join(rd.choice(c) for x in u)
			f.write("username= "+u+" password= "+pwd+" length= "+str(len(u))+" site= "+s+" createdOn= "+timecreated+"\n")
			return pwd
	elif l != None and s == None:
		l = int(l)
		if u == None:
			pwd = pwd.join(rd.choice(c) for x in range(l))
			return pwd
		else:
			if l > len(u):
				pwd = pwd.join(rd.choice(c) for x in range(l))
				f.write("username= "+u+" password= "+pwd+" length= "+str(l)+" createdOn= "+timecreated+"\n")
				return pwd
			else:
				pwd = pwd.join(rd.choice(c) for x in u)
				f.write("username= "+u+" password= "+pwd+" length= "+str(len(u))+" createdOn= "+timecreated+"\n")
				return pwd
	else:
		return "\nUse --help/-h option to view the usage of script\n"
		exit()
	f.close()

def main():
	if crypt != None:
		AesEncDec(crypt)
	if mode in modes:
		if mode == "strong":
			chrr = st.ascii_letters + st.digits + st.punctuation
			print(generatePwd(username,length,chrr,site))
		if mode == "weak":
			chrr = st.ascii_letters
			print(generatePwd(username,length,chrr,site))
		if mode == "medium":
			chrr = st.ascii_letters + st.digits
			print(generatePwd(username,length,chrr,site))


if __name__ == '__main__':
	modes = ["strong","weak","medium"]
	m = "|".join(modes)
	parser = argparse.ArgumentParser(description="Random Password Generator", usage = "\t\npython pass.py -m <mode> -u <username> -s <website>\t\npython pass.py -m <mode> -u <username> -s <website> -l <length>\t\npython pass.py -m <mode> -l <length>\t\npython pass.py -c <encrypt/decrypt>")
	parser.add_argument('-m','--mode',help='Modes:%s' % (m))
	parser.add_argument('-u','--username', help='Specify Username')
	parser.add_argument('-s','--site', help='Specify Web Site')
	parser.add_argument('-l','--length',help='Specify Length of Password')
	parser.add_argument('-c','--crypt',help='Encrypt/Dycrypt file: {0}|{1}'.format("encrypt","decrypt"))
	args = parser.parse_args()
	username = args.username
	length = args.length
	site = args.site
	crypt = args.crypt
	mode = args.mode
	main()
