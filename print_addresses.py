import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

BASE_URL = f"{os.getenv('DEVICE_SCHEME', 'https')}://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv("DEVICE_USER"), os.getenv("DEVICE_PASSWORD"))

r = requests.get(f"{BASE_URL}/ip/address", auth=AUTH, verify=False, timeout=5)
r.raise_for_status()
print(f"{'#':<4}{'ADDRESS':<20}{'INTERFACE':<12}")
for i, a in enumerate(r.json()):
    print(f"{i:<4}{a['address']:<20}{a['interface']:<12}")