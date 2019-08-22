# Demisto SDK for Python

A Python library for the Demisto API.

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
import demisto_client
from demisto_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
api_key = 'GENERATED_API_TOKEN'
host = 'DEMISTO_HOSTNAME'

# create an instance of the API class
api_instance = demisto_client.configure(hostname=host, api_key=api_key)
create_incident_request = demisto_client.CreateIncidentRequest() # CreateIncidentRequest |  (optional)

try:
    # Create single incident
    api_response = api_instance.create_incident(create_incident_request=create_incident_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemistoApi->create_incident: %s\n" % e)
```

By setting the parameter "createInvestigation" to **True**, the newly created incident will also create an Investigation. This will allow for Playbooks to be triggered automatically for the newly created Incident.

```python
client.CreateIncident('incident-name', 'incident-type', 0, 'owner', [{"type": "label", "value": "demisto"}], 'details', {"alertsource":"demisto"}, createInvestigation=True)

```

You can search for incidents by filter:

```python
client.SearchIncidents(0,100,'')
```

Will return all incidents, with a max limit of 100 incidents to return, and page 0 of it

A bit more complex search:

```python
client.SearchIncidents(0,100,'name:test')
```

Will return incidents with name test

* Note - on macOS, the system OpenSSL does not supprot TLSv12 which Demisto server mandates. To run the examples on macOS you will need to install brew and then OpenSSL and Python via brew.

If you don't have brew installed:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

To install Python with new OpenSSL support:
```
brew update
brew install openssl
brew install python --with-brewed-openssl
```

To run the examples:
```
/usr/local/Cellar/python/2.7.13/bin/python example -param val -param val
```
