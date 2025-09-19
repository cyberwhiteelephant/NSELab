import hashlib
import random

# Each user has their own secret key
user_secrets = {
    "alice": "alice_secret_key",
    "bob": "bob_secret_key"
}

# Store used nonces to prevent reuse attacks
used_nonces = set()

def generate_nonce():
    return str(random.randint(100000, 999999))

def hash_response(nonce, secret, username):
    data = nonce + secret + username
    return hashlib.sha256(data.encode()).hexdigest()

# ---------------- CLIENT -----------------
username = "bob"
secret = user_secrets[username]

# Step 1: Server generates nonce
nonce = generate_nonce()
print("Server sends nonce:", nonce)

# Step 2: Client creates response
client_response = hash_response(nonce, secret, username)
print(f"Client ({username}) sends response: {client_response}")

# ---------------- SERVER -----------------
# Step 3: Server verifies
if nonce in used_nonces:
    print("Replay attack detected: Nonce already used")
else:
    expected_response = hash_response(nonce, user_secrets[username], username)
    if client_response == expected_response:
        print(f"Authentication Successful for user {username}")
        used_nonces.add(nonce)  # Mark this nonce as used
    else:
        print("Authentication Failed")