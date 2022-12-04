import sys, hashlib, colorama
from threading import Thread
print("Pasher from 3rd December 2022")
if sys.argv[-1] == "-h" or sys.argv[-1] == "--help" or len(sys.argv) < 2: print("Correct usage: script hashesfile wordlist");exit()
hashfile = open(sys.argv[1], 'r', encoding='utf8');wordlist = open(sys.argv[2], 'r', encoding='latin1');words = [];hashes = [];donehashes = [];count = 0;hashes1 = 0
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
print(f"{colorama.Fore.WHITE}LOG: {colorama.Fore.RESET}Reading...")
for line in wordlist:
    if line == "": continue
    if line.startswith(";"): continue
    count = count + 1;words.append(line)
for line in hashfile:
    if line == "": continue
    if line.startswith(";"): continue
    hashes1 = hashes1 + 1;hashes.append(line)
print(f"{colorama.Fore.WHITE}LOG: {colorama.Fore.RESET}Found {hashes1} hashes and {count} words.")
hashesleft = hashes1 - 1
for hash in hashes: hashes[hashes.index(hash)] = hash.strip()
def crack(word, hash):
    if checkHash(hash.strip(), word.strip()):
        global hashesleft
        global donehashes
        print(f"{colorama.Fore.BLUE}INFO: {colorama.Fore.RESET}Found {hash.strip()}: {word.strip()}")
        donehashes.append(hash)
        hashesleft = hashesleft - 1
for word in words:
    for hash in hashes:
        Thread(target=crack, args=(word.strip(), hash)).start()
        if hashesleft == 0: wordlist.close();print(f"{colorama.Fore.GREEN}SUCCESS: {colorama.Fore.RESET}Done.");exit()
wordlist.close();hashesstr = ""
for hash in donehashes: hashes.remove(hash)
for hash in hashes:
    if hashes[hashes.index(hash)] == hashes[-1]: hashesstr = hashesstr + f"{hash.strip()}"
    else: hashesstr = hashesstr + f"{hash.strip()}, "
if hashesleft != 0: print(f"{colorama.Fore.YELLOW}WARN: {colorama.Fore.RESET}Failed to get: {hashesstr}")