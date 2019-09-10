[![PyPI version](https://badge.fury.io/py/demisto-py.svg)](https://badge.fury.io/py/demisto-py)
[![CircleCI](https://circleci.com/gh/demisto/demisto-py/tree/master.svg?style=svg)](https://circleci.com/gh/demisto/demisto-py/tree/master)
# Demisto SDK for Python

A Python library for the Demisto API.

Version 2.x is compatible with Demisto server version 4.5 and later.

**Note:** You are viewing the demisto-py 2.x development branch. demisto-py 1.x is officially deprecated (maintenance-mode only) and can be obtained at: https://github.com/demisto/demisto-py/releases.

## Demisto for Python Usage
This section covers the steps you need to take to get the SDK configured.

### 1. Get a Demisto API Key
Follow these instructions to generate your Demisto API Key.
1. In Demisto, navigate to **Settings > API Keys**.
2. Click the **Generate Your Key** button.

### 2. Create a Demisto client instance with the api-key and server-url:
```python
import demisto_client

api_key = 'YOUR_API_KEY'
host = 'https://YOUR_DEMISTO_HOST'

api_instance = demisto_client.configure(base_url=host, api_key=api_key)

```

**Alternatively, you can login with username and password:**

```python
import demisto_client

host = 'https://YOUR_DEMISTO_HOST'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

api_instance = demisto_client.configure(base_url=host, username=username, password=password)

```


### 3. Create incidents

```python
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException


api_key = 'YOUR_API_KEY'
host = 'https://YOUR_DEMISTO_HOST'

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

## API Documentation
API Documentation based upon the Demisto Server Swagger API is available [here](docs/README.md)

## Code Generation
Library code was generated using the Demisto Server 4.5.0 Swagger definition. 
We use a script to generate the code and then modify as needed. 
If you would like to contribute don't modify the generated code directly, modify the script. 
To generate the code run (requires bash, sed and docker):
```
./gen-code.sh
```

## License
Apache 2.0 - See [LICENSE](LICENSE) for more information.
