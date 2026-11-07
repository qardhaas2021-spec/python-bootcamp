from pathlib import Path
import os

hosts_file = Path(__file__).parent / "hosts.txt"

# Read IPs from hosts.txt (edit that file yourself — do not overwrite here)
with open(hosts_file, "r") as f:
    ip_addresses = f.read().splitlines()
    print(ip_addresses)

# Ping each IP (Mac: -c 1)
for ip in ip_addresses:
    if not ip.strip():
        continue
    try:
        print(f"\nPinging {ip} ...")
        # -W 1000 = wait max 1 second (Mac), so bad IPs fail fast
        response = os.system("ping -c 1 -W 1000 " + ip)
        if response == 0:
            print(f"{ip} is reachable")
        else:
            print(f"{ip} is not reachable")
    except Exception as e:
        print(f"Host {ip} is down / error: {e}")
        print("*" * 50)
