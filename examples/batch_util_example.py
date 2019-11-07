from __future__ import print_function
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_key = 'YOUR API KEY'
base_url = 'YOUR DEMISTO URL'

# create an instance of the API class
api_instance = demisto_client.configure(base_url=base_url, api_key=api_key, debug=False)
update_data_batch = demisto_client.demisto_api.UpdateDataBatch()

update_data_batch.ids = ['1001', '1002', '1003']
update_data_batch.close_notes = 'Incident is a duplicate to incident 1000'
update_data_batch.close_reason = 'Closed as duplicate'

try:
    # Batch close incidents
    api_response = api_instance.close_incidents_batch(update_data_batch=update_data_batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->close_incidents_batch: %s\n" % e)
