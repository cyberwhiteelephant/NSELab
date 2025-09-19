import subprocess
import os

# Absolute paths
BASE_DIR = "/home/raghu/Documents/NSELab/exp4"
PRIVATE_KEY_FILE = os.path.join(BASE_DIR, "private.key")
CERT_FILE = os.path.join(BASE_DIR, "certificate.crt")

def run_command(command, input_text=None):
    """Run a shell command and return its output."""
    result = subprocess.run(
        command,
        input=input_text,
        text=True,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    return result.stdout

# 1. Generate private key (RSA 2048)
print("Generating private key...")
run_command(f"openssl genpkey -algorithm RSA -out \"{PRIVATE_KEY_FILE}\" -pkeyopt rsa_keygen_bits:2048")

# 2. Generate self-signed certificate (valid for 365 days)
print("Generating self-signed certificate...")
subject = "/C=IN/ST=Jammu/L=Jammu/O=MyOrg/OU=IT/CN=localhost"
run_command(f"openssl req -new -x509 -key \"{PRIVATE_KEY_FILE}\" -out \"{CERT_FILE}\" -days 365 -subj \"{subject}\"")

# 3. View certificate details
print("\nCertificate details:")
details = run_command(f"openssl x509 -in \"{CERT_FILE}\" -text -noout")
print(details)

# 4. Verify certificate signature (self-signed)
print("Verifying certificate...")
verify = run_command(f"openssl verify -CAfile \"{CERT_FILE}\" \"{CERT_FILE}\"")
print(verify)

print("Done.")
