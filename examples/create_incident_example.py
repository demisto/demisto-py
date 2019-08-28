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
