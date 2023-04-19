import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python3 sub.py <domain>")
    sys.exit(1)

subdomain = ""
domain = sys.argv[1]

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
