import sys
import requests
import time

if len(sys.argv) != 2:
    print("Usage: python3 sub.py <domain>")
    sys.exit(1)

subdomain = ""
domain = sys.argv[1]

print(f"Scanning subdomains on {domain}...\n")

# Define the animation sequence
animation = "|/-\\"

# Loop through the animation while scanning subdomains
for i in range(48, 58):
    for j in range(48, 58):
        for k in range(48, 58):
            subdomain = f"{chr(i)}{chr(j)}{chr(k)}.{domain}"
            try:
                response = requests.head(f"http://{subdomain}", timeout=1)
                if response.status_code < 400:
                    print(f"{subdomain} ({response.status_code})")
            except:
                pass

            # Update the animation sequence
            print(f"\rScanning subdomains on {domain}... {animation[i % len(animation)]}", end="")
            time.sleep(0.1)

# Print a newline character to ensure the prompt is on a new line
print("\n")
