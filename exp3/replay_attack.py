import hashlib, uuid

SHARED_SECRET = "my_secret_password"

def generate_response(challenge, secret):
    return hashlib.sha256((challenge + secret).encode()).hexdigest()

def server_issue_challenge():
    return str(uuid.uuid4())

def authenticate():
    challenge = server_issue_challenge()
    print("Server Challenge:", challenge)

    client_response = generate_response(challenge, SHARED_SECRET)

    server_response = generate_response(challenge, SHARED_SECRET)
    if client_response == server_response:
        print("Authentication Successful ✅")
        return challenge, client_response
    else:
        print("Authentication Failed ❌")
        return challenge, None

challenge, valid_response = authenticate()

print("\n--- Replay Attack Simulation ---")
new_challenge = server_issue_challenge()
print("New Challenge (server):", new_challenge)

attacker_response = valid_response
print("Attacker Replay Response:", attacker_response)

expected_response = generate_response(new_challenge, SHARED_SECRET)

if attacker_response == expected_response:
    print("Replay Attack Successful ❌ (Should not happen!)")
else:
    print("Replay Attack Detected ✅")
