import hashlib
import random

shared_key = "Hello"

def generateNonce():
    return random.randint(1000, 9999)

def generateHash(shared_key, nonce):
    combined = shared_key + str(nonce)
    return hashlib.sha256(combined.encode()).hexdigest()

server_nonce = generateNonce()
client_hash = generateHash(shared_key, server_nonce)
attckrnonce=4356545
attacker_hash = generateHash(shared_key, attckrnonce)
server_hash = generateHash(shared_key, server_nonce)

if server_hash == attacker_hash:
    print("Authentication Successful")
else:
    print("Not successfull")
