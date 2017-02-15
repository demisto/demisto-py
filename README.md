# Demisto SDK for Python

A Python library for the Docker Engine API. It lets you do anything the `docker` command does, but from within Python apps – run containers, manage containers, manage Swarms, etc.

## Usage

```python
import demisto
client = demisto.DemistoClient('admin', 'password', 'https://localhost:8443')
client.Login()
```
Should return <Response [200]>


You can create incidents:

```python
client.CreateIncident('incident-name', 'incident-type', 0, 'owner', [{"type": "label", "value": "demisto"}], 'details', {"alertsource":"demisto"})

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

