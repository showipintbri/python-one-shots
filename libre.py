

import requests

# Basic Example
# response = requests.get('https://[internal-libreNMS-fqdn]/api/v0', headers={'X-Auth-Token': '[api-key]'}, verify=False)

# Get ALL VLANs
# response = requests.get('https://[internal-libreNMS-fqdn]/api/v0/resources/vlans', headers={'X-Auth-Token': '[api-key]'}, verify=False)

# Get Device VLANs
response = requests.get('https://[internal-libreNMS-fqdn]/api/v0/devices/10.3.0.13/vlans', headers={'X-Auth-Token': '[api-key]'}, verify=False)

# Get Interface Details
# response = requests.get('https://[internal-libreNMS-fqdn]/api/v0/ports/678', headers={'X-Auth-Token': '[api-key]'}, verify=False)

# Get Interfaces and Return Only Specific Columns
# response = requests.get('https://[internal-libreNMS-fqdn]/api/v0/ports?columns=device_id,ifName,port_id', headers={'X-Auth-Token': '[api-key]'}, verify=False)

# Get Device Details
# response = requests.get('https://[internal-libreNMS-fqdn]/api/v0/devices/10.3.0.13', headers={'X-Auth-Token': '[api-key]'}, verify=False)

try:
    print(response.json())
    
except ConnectionError:
    print('Connection Error')
