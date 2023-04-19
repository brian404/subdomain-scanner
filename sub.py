import requests

subdomains = []

for i in range(48, 58):  # ASCII codes for 0-9
    for j in range(97, 123):  # ASCII codes for a-z
        for k in range(97, 123):
            subdomain = f"{chr(i)}{chr(j)}{chr(k)}.example.com"
            try:
                response = requests.head(f"http://{subdomain}", timeout=0.5)
                if response.status_code < 400:
                    subdomains.append((subdomain, response.status_code))
                    print(f"[+] {subdomain} ({response.status_code})")
            except:
                pass

with open("subdomains.txt", "w") as file:
    for subdomain in subdomains:
        file.write(f"{subdomain[0]} ({subdomain[1]})\n")
