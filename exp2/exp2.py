import hashlib

sender_file = "/home/raghu/Documents/network-security-lab/exp2/sender.txt"

# Step 1: Generate sender.txt hash
try:
    with open(sender_file, "rb") as f:
        sender_data = f.read()
        sender_hash = hashlib.sha256(sender_data).hexdigest()
except FileNotFoundError:
    print(f"Sender file '{sender_file}' not found.")
    exit(1)

# Step 2: Get receiver file and compare hashes
receiver_file = input("Enter the receiver file path: ").strip()
try:
    with open(receiver_file, "rb") as f:
        receiver_data = f.read()
        receiver_hash = hashlib.sha256(receiver_data).hexdigest()
    
    print(f"Sender Hash is : '{sender_hash}'")
    print(f"Receiver Hash is : '{receiver_hash}'")
    if receiver_hash == sender_hash:
        print("Data integrity verified: Hashes match.")
    else:
        print("Data integrity verification failed: Hashes do not match.")
except FileNotFoundError:
    print("Receiver file not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
