from __future__ import print_function
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_key = None  # set to your 'YOUR_API_KEY' or set environment variable: DEMISTO_API_KEY
base_url = None  # set to your 'http://DEMISTO_HOST' or set environment variable: DEMISTO_BASE_URL

# create an instance of the API class
api_instance = demisto_client.configure(base_url=base_url, api_key=api_key, debug=True)
filter = demisto_client.demisto_api.SearchIncidentsData()

# Create incident filter object
inc_filter = demisto_client.demisto_api.IncidentFilter()
inc_filter.name = ['test']

filter.filter = inc_filter

try:
    # Search incidents by filter
    api_response = api_instance.search_incidents(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_incidents: %s\n" % e)
