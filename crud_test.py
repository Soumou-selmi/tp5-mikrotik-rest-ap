import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

BASE_URL = f"{os.getenv('DEVICE_SCHEME', 'https')}://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv("DEVICE_USER"), os.getenv("DEVICE_PASSWORD"))

def api(method, path, **kw):
    r = requests.request(method, f"{BASE_URL}{path}", auth=AUTH,
                         verify=False, timeout=5, **kw)
    r.raise_for_status()
    return r.json() if r.text else None

# GET
print(api("GET", "/ip/address"))

# POST
created = api("POST", "/ip/address",
              json={"address": "192.168.20.1/24", "interface": "ether2"})
print(created)
ip_id = created[".id"]

# PATCH
api("PATCH", f"/ip/address/{ip_id}", json={"comment": "TP5 test"})

# DELETE
api("DELETE", f"/ip/address/{ip_id}")