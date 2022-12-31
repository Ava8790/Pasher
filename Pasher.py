import sys, hashlib, colorama
from threading import Thread
print("Pasher from 31rd December 2022")
if sys.argv[-1] == "-h" or sys.argv[-1] == "--help" or len(sys.argv) < 2: print("Correct usage: script hashesfile wordlist");exit()
def calculateAlgorithm(hash):
    if len(hash) == 32: return "MD5"
    elif len(hash) == 40: return "SHA1"
    elif len(hash) == 56: return "SHA224"
    elif len(hash) == 64: return "SHA256"
    elif len(hash) == 96: return "SHA384"
    elif len(hash) == 128: return "SHA512"
    else: return "unknown"
def checkHash(hash, word):
    if calculateAlgorithm(hash) == "MD5": return hashlib.md5(word.strip().encode()).hexdigest() == hash
    elif calculateAlgorithm(hash) == "SHA1": return hashlib.sha1(word.strip().encode()).hexdigest() == hash
    elif calculateAlgorithm(hash) == "SHA224": return hashlib.sha224(word.strip().encode()).hexdigest() == hash
    elif calculateAlgorithm(hash) == "SHA256": return hashlib.sha256(word.strip().encode()).hexdigest() == hash
    elif calculateAlgorithm(hash) == "SHA384": return hashlib.sha384(word.strip().encode()).hexdigest() == hash
    elif calculateAlgorithm(hash) == "SHA512": return hashlib.sha512(word.strip().encode()).hexdigest() == hash
    else: return False
def crack(word, hash):
    if checkHash(hash.strip(), word.strip()): print(f"{colorama.Fore.BLUE}INFO: {colorama.Fore.RESET}Found {hash.strip()} ({calculateAlgorithm(hash.strip())}): {word.strip()}")
print("Checking...")
hashfile = open(sys.argv[1], 'r', encoding='utf8');words = open(sys.argv[2], 'r', encoding='latin1')
for word in words:
    if word == "": continue
    if word.startswith(";"): continue
    for hash in hashfile:
        if hash == "": continue
        if hash.startswith(";"): continue
        Thread(target=crack, args=(word.strip(), hash)).start()
words.close();hashesstr = ""