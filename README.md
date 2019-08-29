[![PyPI version](https://badge.fury.io/py/demisto-py.svg)](https://badge.fury.io/py/demisto-py)
# Demisto SDK for Python

A Python library for the Demisto API.

Version 2.x is compatible with Demisto server version 4.5 and above.

**Note:** You are viewing demisto-py 2.x development branch. demisto-py 1.x is officially in maintenance-mode only and can be obtained at: https://github.com/demisto/demisto-py/releases .

## Usage

First, you will need to obtain your Demisto API Key. You can generate one via your Demisto UI by navigating to  `settings`->`API keys`.

Create demisto client instance with the api-key and server-url:
```python
import demisto_client

api_key = 'YOUR_API_KEY'
host = 'YOUR_HOSTNAME'

api_instance = demisto_client.configure(hostname=host, api_key=api_key)

```

Alternatively, you can login with username and password:

```python
import demisto_client

host = 'YOUR_HOSTNAME'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

api_instance = demisto_client.configure(hostname=host, username=username, password=password)

```


You can create incidents:

```python
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException


api_key = 'YOUR_API_KEY'
host = 'YOUR_DEMISTO_HOST'

api_instance = demisto_client.configure(base_url=host, api_key=api_key, debug=False)
create_incident_request = demisto_client.demisto_api.CreateIncidentRequest()

create_incident_request.name = 'Sample Simulation Incident'
create_incident_request.type = 'Simulation'
create_incident_request.owner = 'Admin'

try:
    api_response = api_instance.create_incident(create_incident_request=create_incident_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_incident: %s\n" % e)

```
