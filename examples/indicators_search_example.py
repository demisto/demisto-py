from __future__ import print_function
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_key = 'YOUR API KEY'
base_url = 'YOUR DEMISTO URL'

# create an instance of the API class
api_instance = demisto_client.configure(base_url=base_url, api_key=api_key, debug=True)
indicator_filter = demisto_client.demisto_api.IndicatorFilter()

indicator_filter.query = 'value:8.8.8.8'

try:
    # Search indicators
    api_response = api_instance.indicators_search(indicator_filter=indicator_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->indicators_search: %s\n" % e)
