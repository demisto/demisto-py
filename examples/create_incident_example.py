import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from datetime import datetime
import tempfile
import os
import time

api_key = None  # set to your 'YOUR_API_KEY' or set environment variable: DEMISTO_API_KEY
base_url = None  # set to your 'http://DEMISTO_HOST' or set environment variable: DEMISTO_BASE_URL

api_instance = demisto_client.configure(base_url=base_url, api_key=api_key, debug=True)
create_incident_request = demisto_client.demisto_api.CreateIncidentRequest()

create_incident_request.name = 'Sample Malware Incident: {}'.format(datetime.now())
create_incident_request.type = 'Malware'
create_incident_request.owner = 'admin'
create_incident_request.severity = 1
create_incident_request.occurred = datetime.now()
create_incident_request.create_investigation = False  # we set to false as we still neeed to upload a file
create_incident_request.playbook_id = 'malware_investigation-_generic'
# If you want to set source_brand and source_instance it is required to set the `Instance` label
create_incident_request.labels = [demisto_client.demisto_api.Label('Instance', 'Demisto Py Client')]
create_incident_request.source_brand = 'API'
create_incident_request.source_instance = 'Demisto Py Client'
create_incident_request.custom_fields = {
    'src': '1.1.1.1',
    'dest': '192.168.1.1',
    'malwarefamily': 'Trojan.Generic',
    'filehash': '142b638c6a60b60c7f9928da4fb85a5a8e1422a9ffdc9ee49e17e56ccca9cf6e',
    'vendorproduct': 'Secure Product',
}

tf = None
try:
    api_response = api_instance.create_incident(create_incident_request=create_incident_request)
    print("Create incident response: {}".format(api_response))
    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.write(b'Test data representing an uploaded file')
    tf.close()
    # note that this is a form post. `last` needs to be true/false string and not boolean
    res_upload = api_instance.incident_file_upload(id=api_response.id, file=tf.name, file_name="test-report.txt", 
                                                   file_comment='Test report file', last='true')
    print("Upload file to incident response: {}".format(res_upload))
    # the uploaded file will be the 3rd entry. Let's download it
    print('sleeping 10 seconds before download....')
    time.sleep(10)  # sleep a few seconds to allow server to fully index
    res_download = api_instance.download_file('3@{}'.format(api_response.id))
    print("Download file result: {}".format(res_download))
except ApiException as e:
    print("Exception when calling DefaultApi->create_incident: %s\n" % e)
finally:
    if tf:
        os.unlink(tf.name)
