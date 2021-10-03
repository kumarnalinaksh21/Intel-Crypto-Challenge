import sys, os, platform, base64, json
from OpenSSL import crypto


message = "" #initialising empty message
count = 0    #initialising empty count for number of characters in the message
Type_Key = crypto.TYPE_RSA #initialising key type to RSA
bits = 2048 #initialising 
private_key = "" #initialising empty private key
public_key = "" #initialising empty public key
pkey = "" #initialising empty pkey object
signature = "" #initialising empty MAC
resultJSON = {} #initialising empty JSON response
flag = False #set global flag as false
numberOfArguments = len(sys.argv) #total arguments passed to the script


def checkInputAndConsolidateMessage(): #Funtion parses arguments, checks min and max character limits and forms message
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

        
def CreateKeyPair():
    global Type_Key, bits, private_key, public_key, pkey
    pkey = crypto.PKey()
    pkey.generate_key(Type_Key, bits)
    private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM , pkey , None)
    public_key = crypto.dump_publickey(crypto.FILETYPE_PEM , pkey)


def checkOperatingSystemType():
    OS = platform.system()
    return OS

def CheckIfdirectoryExistsAndThenConfigureKeys():
    global private_key, public_key, flag
    path = os.path.expanduser("~") #initialise home directory

    if checkOperatingSystemType() == "Windows": #initialise full path for fetching and saving keys based on Operating System
        subPath = "\.local\share\signer"
        finalPath = path + subPath
    elif checkOperatingSystemType() == "Linux":
        subPath = "/.local/share/signer"
        finalPath = path + subPath
    
    if os.path.exists(finalPath): #Directory for keys exists 
         if checkOperatingSystemType() == "Windows":
             PubFilepath = finalPath + "\PublicKey.pem" #initialise path for public key in Windows
             PrivFilePath = finalPath + "\PrivateKey.pem" #initialise path for private key in Windows
         elif checkOperatingSystemType() == "Linux":
             PubFilepath = finalPath + "/PublicKey.pem" #initialise path for public key in Windows
             PrivFilePath = finalPath + "/PrivateKey.pem" #initialise path for private key in Windows

         if os.path.exists(PubFilepath) and os.path.exists(PrivFilePath): #check if both the keys exist
             with open(PrivFilePath, 'rb') as PrivFile:
                 private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, PrivFile.read(), None)
             with open(PubFilepath, 'rb') as PubFile:
                 public_key = PubFile.read().decode('utf-8')
             flag = True

         else: #if keys don't exist, create them
             CreateKeyPair() 
             with open(PrivFilePath, 'wb') as PrivFile:
                 PrivFile.write(private_key)
             with open(PrivFilePath, 'rb') as PrivFile:
                 private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, PrivFile.read(), None)
             with open(PubFilepath, 'wb') as PubFile:
                 PubFile.write(public_key)
             with open(PubFilepath, 'rb') as PubFile:
                      public_key = PubFile.read().decode('utf-8')
             flag = True

    else: #Directory for keys does not exists 
         print(finalPath, " does not esist.")
         try : 
             os.mkdir(finalPath)  # trying to create the directory 
         except :
             pass
         if os.path.exists(finalPath) == True:
             print("Directory Created")
             CheckIfdirectoryExistsAndThenConfigureKeys()
         else: 
             print(finalPath, " could not be created due to access permission issue.")
             path = os.getcwd()
             flag = True
             print("Instead of ", finalPath, " program will now use current working directory ", path)
             if checkOperatingSystemType() == "Windows":
                 PubFilepath = path + "\PublicKey.pem" #initialise path for public key in Windows
                 PrivFilePath = path + "\PrivateKey.pem" #initialise path for private key in Windows
             elif checkOperatingSystemType() == "Linux":
                 PubFilepath = path + "/PublicKey.pem" #initialise path for public key in Windows
                 PrivFilePath = path + "/PrivateKey.pem" #initialise path for private key in Windows

             if os.path.exists(PubFilepath) and os.path.exists(PrivFilePath): #check if both the keys exist
                 with open(PrivFilePath, 'rb') as PrivFile:
                     private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, PrivFile.read(), None)
                 with open(PubFilepath, 'rb') as PubFile:
                      public_key = PubFile.read().decode('utf-8')
                 flag = True

             else: #if keys don't exist, create them
                 CreateKeyPair()
                 with open(PrivFilePath, 'wb') as PrivFile:
                     PrivFile.write(private_key)
                 with open(PrivFilePath, 'rb') as PrivFile:
                     private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, PrivFile.read(), None)
                 with open(PubFilepath, 'wb') as PubFile:
                     PubFile.write(public_key)
                 with open(PubFilepath, 'rb') as PubFile:
                      public_key = PubFile.read().decode('utf-8')
                 flag = True




def signingTheMessage():
    global signature, private_key, message
    signature = crypto.sign(private_key, message.encode(), "sha256")
    signature = base64.encodebytes(signature).decode()


    
def formJSON():
    global  resultJSON, message, signature, public_key
    resultJSON = { "message": message, "signature":signature, "pubkey":public_key}
    resultJSON = json.dumps(resultJSON, indent=3)
    print(resultJSON)

if checkInputAndConsolidateMessage():
    CheckIfdirectoryExistsAndThenConfigureKeys()
    if flag == True:
        signingTheMessage()
        formJSON()



