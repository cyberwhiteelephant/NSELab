import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def verify_data(original_data, received_data):
    original_hash = generate_hash(original_data)
    received_hash = generate_hash(received_data)
    return original_hash == received_hash, original_hash, received_hash

data = "Hello World"
modified_data = "Hello Wor1d"

status, orig, recv = verify_data(data, modified_data)

print("Original Hash:", orig)
print("Received Hash:", recv)
print("Integrity Verified:", status)
