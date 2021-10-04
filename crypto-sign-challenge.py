import sys
import os
import platform
import base64
import json
from OpenSSL import crypto

#---------------------- Initialising Global Variables------------------------#
message = "" #initialising empty message
count = 0    #initialising empty count for number of characters in the message
Type_Key = crypto.TYPE_RSA #initialising key type to RSA, modify to TYPE_DSA for DSA
bits = 2048 #initialising 
private_key = "" #initialising empty private key
public_key = "" #initialising empty public key
pkey = "" #initialising empty pkey object
signature = "" #initialising empty MAC
resultJSON = {} #initialising empty JSON response
flag = False #set global flag as false
numberOfArguments = len(sys.argv) #total arguments passed to the script


#---------------------- Funtion parses arguments, checks min and max character limits and forms message------------------------#
def CheckInputAndConsolidateMessage(): 
    global numberOfArguments, message, count 

    for i in range(1, numberOfArguments): #Forming message from the argument
        message = message + sys.argv[i] + " "

    for i in message: #counting number of characters in the message
        count = count + 1
    count = count - 1 #removing the count for the space character at the end of the message

    if(count<=1): #giving alert if number of characters are insufficient or more than required.
        print("The message must be more than 1 character and less than 250 characters.")
        return False 
    elif(count>250):
        print("The message must be 250 characters or less.")
        return False
    else: 
        return True

#---------------------- Funtion generates Private and Public key pairs------------------------#        
def CreateKeyPair():
    global Type_Key, bits, private_key, public_key, pkey
    pkey = crypto.PKey()
    pkey.generate_key(Type_Key, bits) #generating key pair
    private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM , pkey , None) #saving private key contents in byte form 
    public_key = crypto.dump_publickey(crypto.FILETYPE_PEM , pkey) #saving public key contents in byte form 

#---------------------- Funtion reads Private and Public keys from their respective PEM files------------------------#   
def ReadKeyPairFromPEMFile(PrivFilePath, PubFilepath):
    global private_key, public_key
    with open(PrivFilePath, 'rb') as PrivFile:
        private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, PrivFile.read(), None) #loading private key from PEM file in pkey() object form
    with open(PubFilepath, 'rb') as PubFile:
        public_key = PubFile.read().decode('utf-8') #assigning Base64 encoded string (PEM format) of the public key from PEM file
            
#---------------------- Funtion writes Private and Public keys into their respective PEM files------------------------# 
def WriteKeyPairToPEMFile(PrivFilePath, PubFilepath):
    global private_key, public_key
    with open(PrivFilePath, 'wb') as PrivFile:
        PrivFile.write(private_key) #writing private key to PEM file 
    with open(PrivFilePath, 'rb') as PrivFile:
        private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, PrivFile.read(), None) #reassiging private key content to variable in pkey() object form 
    with open(PubFilepath, 'wb') as PubFile:
        PubFile.write(public_key) #writing public key to PEM file
    with open(PubFilepath, 'rb') as PubFile:
        public_key = PubFile.read().decode('utf-8') #assigning Base64 encoded string (PEM format) of the public key from PEM file

#---------------------- Funtion checks the type of operating system on which script is being run------------------------#
def CheckOperatingSystemType():
    OS = platform.system()
    return OS

#------- Funtion checks if directory exists, else tries to create it. If unsuccessful then uses current working directory and configure keys---------#
def CheckIfdirectoryExistsAndThenConfigureKeys():
    global private_key, public_key
    path = os.path.expanduser("~") #initialise home directory

    if CheckOperatingSystemType() == "Windows": #initialise full path for fetching and saving keys based on Operating System
        subPath = "\.local\share\signer"
        finalPath = path + subPath #path for Windows default directory
    elif CheckOperatingSystemType() == "Linux":
        subPath = "/.local/share/signer"
        finalPath = path + subPath #path for Linux default directory
    
    if os.path.exists(finalPath): #Directory for keys exists 
         if CheckOperatingSystemType() == "Windows":
             PubFilepath = finalPath + "\PublicKey.pem" #initialise path for public key in Windows
             PrivFilePath = finalPath + "\PrivateKey.pem" #initialise path for private key in Windows
         elif CheckOperatingSystemType() == "Linux":
             PubFilepath = finalPath + "/PublicKey.pem" #initialise path for public key in Linux
             PrivFilePath = finalPath + "/PrivateKey.pem" #initialise path for private key in Linux

         if os.path.exists(PubFilepath) and os.path.exists(PrivFilePath): #check if both the keys exist
             ReadKeyPairFromPEMFile(PrivFilePath, PubFilepath) #read keys from PEM files and configuring them into variables

         else: #if keys don't exist, create them
             CreateKeyPair() #generating Private and Public keys
             WriteKeyPairToPEMFile(PrivFilePath, PubFilepath) #writing keys into PEM files and configuring them into variables

    else: #Directory for keys does not exists 
         print(finalPath, " does not esist.")
         try : 
             os.mkdir(finalPath)  # trying to create the directory 
         except :
             pass #executing further script in case directory creation encounters an error
         if os.path.exists(finalPath) == True: #checking if directory has been created successfully
             print("Directory Created")
             CheckIfdirectoryExistsAndThenConfigureKeys() #recursion
         else: 
             print(finalPath, " could not be created due to access permission issue.")
             path = os.getcwd() #initialising current working directory as path
             print("Instead of ", finalPath, " program will now use current working directory ", path)
             if CheckOperatingSystemType() == "Windows":
                 PubFilepath = path + "\PublicKey.pem" #initialise path in current working directory for public key in Windows
                 PrivFilePath = path + "\PrivateKey.pem" #initialise path in current working directory for private key in Windows
             elif CheckOperatingSystemType() == "Linux":
                 PubFilepath = path + "/PublicKey.pem" #initialise path in current working directory for public key in Linux
                 PrivFilePath = path + "/PrivateKey.pem" #initialise path in current working directory for private key in Linux

             if os.path.exists(PubFilepath) and os.path.exists(PrivFilePath): #check if both the keys exist
                 ReadKeyPairFromPEMFile(PrivFilePath, PubFilepath) #read keys from PEM files and configuring them into variables

             else: #if keys don't exist, create them
                 CreateKeyPair() #generating Private and Public keys
                 WriteKeyPairToPEMFile(PrivFilePath, PubFilepath) #writing keys into PEM files and configuring them into variables


#---- Funtion generates RFC 4648 compliant Base64 encoded cryptographic signature of the message, calculated using the private key and the SHA256 digest of the message----#
def SigningTheMessage():
    global signature, private_key, message
    signature = crypto.sign(private_key, message.encode(), "sha256") #forming signature using private key and sha256 digest of message
    signature = base64.encodebytes(signature).decode() #Base64 encoding of the cryptographic signature of the message

    
#-------------Function generates JSON compliant to the schema defined in README----------------#
def FormJSON():
    global  resultJSON, message, signature, public_key
    resultJSON = { "message": message, "signature":signature, "pubkey":public_key} #initialising dictionary complaint with JSON
    resultJSON = json.dumps(resultJSON, indent=3) # serialising into JSON
    print(resultJSON)

#-------------Main Function----------------#
def Main(): 
    if CheckInputAndConsolidateMessage(): #checking input and consolidating message, if as per policy then program will proceed.
        CheckIfdirectoryExistsAndThenConfigureKeys() #checking if directory exists, else we try to create it. If unsuccessful then we use current working directory and configure the keys
        SigningTheMessage() #generating RFC 4648 compliant Base64 encoded cryptographic signature of the message, calculated using the private key and the SHA256 digest of the message
        FormJSON() #generating JSON compliant to the schema defined in README



if __name__ == "__main__":
    Main()

