import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

BASE_URL = f"{os.getenv('DEVICE_SCHEME', 'https')}://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv("DEVICE_USER"), os.getenv("DEVICE_PASSWORD"))

ROUTES = [
    {"dst-address": "10.10.0.0/24", "gateway": "192.168.88.2"},
    {"dst-address": "10.20.0.0/24", "gateway": "192.168.88.3"},
]

def main():
    existing = requests.get(f"{BASE_URL}/ip/route", auth=AUTH,
                            verify=False, timeout=5)
    existing.raise_for_status()
    existing_set = {(r.get("dst-address"), r.get("gateway"))
                    for r in existing.json()}

    for route in ROUTES:
        key = (route["dst-address"], route["gateway"])
        if key in existing_set:
            print(f"[SKIP] {key} oki")
            continue
        r = requests.post(f"{BASE_URL}/ip/route", json=route, auth=AUTH,
                          verify=False, timeout=5)
        r.raise_for_status()
        print(f"[OK]   {key} tzed")

if __name__ == "__main__":
    main()
