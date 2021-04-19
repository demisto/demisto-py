# demisto_client.demisto_api.DefaultApi

All URIs are relative to *https://hostname:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ad_hoc_task**](DefaultApi.md#add_ad_hoc_task) | **POST** /inv-playbook/task/add/{investigationId} | Add ad-hoc task
[**close_incidents_batch**](DefaultApi.md#close_incidents_batch) | **POST** /incident/batchClose | Batch close incidents
[**complete_task**](DefaultApi.md#complete_task) | **POST** /inv-playbook/task/complete | [Deprecated] Complete a task
[**complete_task_v2**](DefaultApi.md#complete_task_v2) | **POST** /v2/inv-playbook/task/complete | Complete a task
[**copy_script**](DefaultApi.md#copy_script) | **POST** /automation/copy | Copy automation
[**create_docker_image**](DefaultApi.md#create_docker_image) | **POST** /settings/docker-images | Create Image
[**create_feed_indicators_json**](DefaultApi.md#create_feed_indicators_json) | **POST** /indicators/feed/json | Create feed indicators from JSON
[**create_incident**](DefaultApi.md#create_incident) | **POST** /incident | Create single incident
[**create_incident_json**](DefaultApi.md#create_incident_json) | **POST** /incident/json | Create incident from JSON
[**create_incidents_batch**](DefaultApi.md#create_incidents_batch) | **POST** /incident/batch | Batch create incidents
[**create_or_update_incident_type**](DefaultApi.md#create_or_update_incident_type) | **POST** /incidenttype | Create new Incident Type
[**delete_ad_hoc_task**](DefaultApi.md#delete_ad_hoc_task) | **POST** /inv-playbook/task/delete/{investigationId}/{invPBTaskId} | Delete ad-hoc task
[**delete_automation_script**](DefaultApi.md#delete_automation_script) | **POST** /automation/delete | Delete existing automation
[**delete_evidence_op**](DefaultApi.md#delete_evidence_op) | **POST** /evidence/delete | delete evidence
[**delete_incidents_batch**](DefaultApi.md#delete_incidents_batch) | **POST** /incident/batchDelete | Batch delete incidents
[**delete_indicators_batch**](DefaultApi.md#delete_indicators_batch) | **POST** /indicators/batchDelete | Batch whitelist or delete indicators
[**delete_widget**](DefaultApi.md#delete_widget) | **DELETE** /widgets/{id} | Remove existing widget
[**download_file**](DefaultApi.md#download_file) | **GET** /entry/download/{entryid} | Download file
[**download_latest_report**](DefaultApi.md#download_latest_report) | **GET** /reports/{id}/latest | Get latest report by ID
[**edit_ad_hoc_task**](DefaultApi.md#edit_ad_hoc_task) | **POST** /inv-playbook/task/edit/{investigationId} | Edit ad-hoc task
[**entry_export_artifact**](DefaultApi.md#entry_export_artifact) | **POST** /entry/exportArtifact | Export Artifact
[**execute_report**](DefaultApi.md#execute_report) | **POST** /report/{id}/{requestId}/execute | Execute report
[**export_incidents_to_csv_batch**](DefaultApi.md#export_incidents_to_csv_batch) | **POST** /incident/batch/exportToCsv | Batch export incidents to csv
[**export_indicators_to_csv_batch**](DefaultApi.md#export_indicators_to_csv_batch) | **POST** /indicators/batch/exportToCsv | Batch export indicators to csv
[**export_indicators_to_stix_batch**](DefaultApi.md#export_indicators_to_stix_batch) | **POST** /indicators/batch/export/stix | Batch export indicators to STIX
[**get_all_reports**](DefaultApi.md#get_all_reports) | **GET** /reports | Get all reports
[**get_all_widgets**](DefaultApi.md#get_all_widgets) | **GET** /widgets | 
[**get_audits**](DefaultApi.md#get_audits) | **POST** /settings/audits | Get Audits
[**get_automation_scripts**](DefaultApi.md#get_automation_scripts) | **POST** /automation/search | Search Automation (aka scripts)
[**get_docker_images**](DefaultApi.md#get_docker_images) | **GET** /settings/docker-images | Get Docker Images
[**get_entry_artifact**](DefaultApi.md#get_entry_artifact) | **GET** /entry/artifact/{id} | Get entry artifact
[**get_incident_as_csv**](DefaultApi.md#get_incident_as_csv) | **GET** /incident/csv/{id} | Get incident as CSV
[**get_incidents_fields_by_incident_type**](DefaultApi.md#get_incidents_fields_by_incident_type) | **GET** /incidentfields/associatedTypes/{type} | Get all incident fields associated with incident type
[**get_indicators_as_csv**](DefaultApi.md#get_indicators_as_csv) | **GET** /indicators/csv/{id} | Get indicators as CSV
[**get_indicators_as_stix**](DefaultApi.md#get_indicators_as_stix) | **GET** /indicators/stix/v2/{id} | Get indicators as STIX V2
[**get_report_by_id**](DefaultApi.md#get_report_by_id) | **GET** /reports/{id} | Get report by ID
[**get_stats_for_dashboard**](DefaultApi.md#get_stats_for_dashboard) | **POST** /statistics/dashboards/query | Get Dashboard Statistics
[**get_stats_for_widget**](DefaultApi.md#get_stats_for_widget) | **POST** /statistics/widgets/query | Get Widget Statistics
[**get_widget**](DefaultApi.md#get_widget) | **GET** /widgets/{id} | Get widget by ID
[**import_classifier**](DefaultApi.md#import_classifier) | **POST** /classifier/import | Import a classifier
[**import_dashboard**](DefaultApi.md#import_dashboard) | **POST** /dashboards/import | Import a dashboard
[**import_incident_fields**](DefaultApi.md#import_incident_fields) | **POST** /incidentfields/import | Import an incidents field
[**import_incident_types_handler**](DefaultApi.md#import_incident_types_handler) | **POST** /incidenttypes/import | Import an incident type
[**import_layout**](DefaultApi.md#import_layout) | **POST** /v2/layouts/import | Import a layout
[**import_playbook**](DefaultApi.md#import_playbook) | **POST** /playbook/save/yaml | Import and override playbook
[**import_script**](DefaultApi.md#import_script) | **POST** /automation/import | Upload an automation
[**import_widget**](DefaultApi.md#import_widget) | **POST** /widgets/import | Import a widget
[**incident_file_upload**](DefaultApi.md#incident_file_upload) | **POST** /incident/upload/{id} | 
[**indicator_whitelist**](DefaultApi.md#indicator_whitelist) | **POST** /indicator/whitelist | Whitelists or deletes Indicator
[**indicators_create**](DefaultApi.md#indicators_create) | **POST** /indicator/create | Create Indicator
[**indicators_create_batch**](DefaultApi.md#indicators_create_batch) | **POST** /indicators/upload | Create indicators
[**indicators_edit**](DefaultApi.md#indicators_edit) | **POST** /indicator/edit | Edit Indicator
[**indicators_search**](DefaultApi.md#indicators_search) | **POST** /indicators/search | Search indicators
[**integration_upload**](DefaultApi.md#integration_upload) | **POST** /settings/integration-conf/upload | Upload an integration
[**investigation_add_entries_sync**](DefaultApi.md#investigation_add_entries_sync) | **POST** /entry/execute/sync | Create new entry in existing investigation
[**investigation_add_entry_handler**](DefaultApi.md#investigation_add_entry_handler) | **POST** /entry | Create new entry in existing investigation
[**investigation_add_formatted_entry_handler**](DefaultApi.md#investigation_add_formatted_entry_handler) | **POST** /entry/formatted | Create new formatted entry in existing investigation
[**revoke_user_api_key**](DefaultApi.md#revoke_user_api_key) | **POST** /apikeys/revoke/user/{username} | 
[**save_evidence**](DefaultApi.md#save_evidence) | **POST** /evidence | Save evidence
[**save_or_update_script**](DefaultApi.md#save_or_update_script) | **POST** /automation | Create or update automation
[**save_widget**](DefaultApi.md#save_widget) | **POST** /widgets | Add or update a widget
[**search_evidence**](DefaultApi.md#search_evidence) | **POST** /evidence/search | Search evidence
[**search_incidents**](DefaultApi.md#search_incidents) | **POST** /incidents/search | Search incidents by filter
[**search_investigations**](DefaultApi.md#search_investigations) | **POST** /investigations/search | Search investigations by filter
[**simple_complete_task**](DefaultApi.md#simple_complete_task) | **POST** /inv-playbook/task/complete/simple | Complete task simple (no file)
[**submit_task_form**](DefaultApi.md#submit_task_form) | **POST** /v2/inv-playbook/task/form/submit | Complete a task
[**task_add_comment**](DefaultApi.md#task_add_comment) | **POST** /inv-playbook/task/note/add | Task add comment
[**task_assign**](DefaultApi.md#task_assign) | **POST** /inv-playbook/task/assign | Assign task
[**task_set_due**](DefaultApi.md#task_set_due) | **POST** /inv-playbook/task/due | Set task due date
[**task_un_complete**](DefaultApi.md#task_un_complete) | **POST** /inv-playbook/task/uncomplete | Un complete a task
[**update_entry_note**](DefaultApi.md#update_entry_note) | **POST** /entry/note | Mark entry as note
[**update_entry_tags_op**](DefaultApi.md#update_entry_tags_op) | **POST** /entry/tags | Set entry tags


# **add_ad_hoc_task**
> InvestigationPlaybook add_ad_hoc_task(investigation_id, inv_playbook_task_data=inv_playbook_task_data)

Add ad-hoc task

Add an ad-hoc task to a running playbook

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
investigation_id = 'investigation_id_example' # str | investigation ID
inv_playbook_task_data = demisto_client.demisto_api.InvPlaybookTaskData() # InvPlaybookTaskData |  (optional)

try:
    # Add ad-hoc task
    api_response = api_instance.add_ad_hoc_task(investigation_id, inv_playbook_task_data=inv_playbook_task_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_ad_hoc_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**| investigation ID | 
 **inv_playbook_task_data** | [**InvPlaybookTaskData**](InvPlaybookTaskData.md)|  | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **close_incidents_batch**
> IncidentSearchResponseWrapper close_incidents_batch(update_data_batch=update_data_batch)

Batch close incidents

Closes an incidents batch To update incident custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip To get the actual key name you can also go to Demisto CLI and run /incident_add and look for the key that you would like to update

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_data_batch = demisto_client.demisto_api.UpdateDataBatch() # UpdateDataBatch |  (optional)

try:
    # Batch close incidents
    api_response = api_instance.close_incidents_batch(update_data_batch=update_data_batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->close_incidents_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_data_batch** | [**UpdateDataBatch**](UpdateDataBatch.md)|  | [optional] 

### Return type

[**IncidentSearchResponseWrapper**](IncidentSearchResponseWrapper.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **complete_task**
> InvestigationPlaybook complete_task(investigation_id, file_comment, task_id, task_input, version, file, file_name=file_name)

[Deprecated] Complete a task

Complete a task with a file attachment Deprecated - use \"/v2/inv-playbook/task/complete\"

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
investigation_id = 'investigation_id_example' # str | investigation ID
file_comment = 'file_comment_example' # str | file comment
task_id = 'task_id_example' # str | Task Id
task_input = 'task_input_example' # str | task input
version = 'version_example' # str | Version
file = '/path/to/file.txt' # file | file
file_name = 'file_name_example' # str | file name (optional)

try:
    # [Deprecated] Complete a task
    api_response = api_instance.complete_task(investigation_id, file_comment, task_id, task_input, version, file, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->complete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**| investigation ID | 
 **file_comment** | **str**| file comment | 
 **task_id** | **str**| Task Id | 
 **task_input** | **str**| task input | 
 **version** | **str**| Version | 
 **file** | **file**| file | 
 **file_name** | **str**| file name | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **complete_task_v2**
> InvestigationPlaybook complete_task_v2(investigation_id, task_id, task_input, version, file, task_comment=task_comment, file_names=file_names, file_comments=file_comments)

Complete a task

Complete a task with command and multiple file attachments

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
investigation_id = 'investigation_id_example' # str | investigation ID
task_id = 'task_id_example' # str | Task Id
task_input = 'task_input_example' # str | Task input
version = 'version_example' # str | Version
file = '/path/to/file.txt' # file | Files to attach to the task
task_comment = 'task_comment_example' # str | Task comment or command to run (optional)
file_names = 'file_names_example' # str | file names separated by %###% (only if files provided) (optional)
file_comments = 'file_comments_example' # str | file comment separated by %###% (only if files provided) (optional)

try:
    # Complete a task
    api_response = api_instance.complete_task_v2(investigation_id, task_id, task_input, version, file, task_comment=task_comment, file_names=file_names, file_comments=file_comments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->complete_task_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**| investigation ID | 
 **task_id** | **str**| Task Id | 
 **task_input** | **str**| Task input | 
 **version** | **str**| Version | 
 **file** | **file**| Files to attach to the task | 
 **task_comment** | **str**| Task comment or command to run | [optional] 
 **file_names** | **str**| file names separated by %###% (only if files provided) | [optional] 
 **file_comments** | **str**| file comment separated by %###% (only if files provided) | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **copy_script**
> AutomationScriptResult copy_script(automation_script_filter_wrapper=automation_script_filter_wrapper)

Copy automation

Copy given automation

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
automation_script_filter_wrapper = demisto_client.demisto_api.AutomationScriptFilterWrapper() # AutomationScriptFilterWrapper |  (optional)

try:
    # Copy automation
    api_response = api_instance.copy_script(automation_script_filter_wrapper=automation_script_filter_wrapper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->copy_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_script_filter_wrapper** | [**AutomationScriptFilterWrapper**](AutomationScriptFilterWrapper.md)|  | [optional] 

### Return type

[**AutomationScriptResult**](AutomationScriptResult.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_docker_image**
> NewDockerImageResult create_docker_image(new_docker_image=new_docker_image)

Create Image

Create an image with a given list of dependencies

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
new_docker_image = demisto_client.demisto_api.NewDockerImage() # NewDockerImage |  (optional)

try:
    # Create Image
    api_response = api_instance.create_docker_image(new_docker_image=new_docker_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_docker_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_docker_image** | [**NewDockerImage**](NewDockerImage.md)|  | [optional] 

### Return type

[**NewDockerImageResult**](NewDockerImageResult.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_feed_indicators_json**
> create_feed_indicators_json(feed_indicators_request)

Create feed indicators from JSON

Create indicators from raw JSON (similar to ingesting from a feed). Builds indicators according to the specified feed classifier, or uses the default one if not specified. Indicator properties (all optional except for value): **value** (string, required) | **type** (string) | **score** (number, 0-3, default `0`, where `0` means None, `1` Good, `2` Suspicious, and `3` Bad) | **sourceBrand** (string, default `\"External\"`) | **sourceInstance** (string, default `\"External\"`) | **reliability** (string, one of `\"A - Completely reliable\"`, `\"B - Usually reliable\"`, `\"C - Fairly reliable\"`, `\"D - Not usually reliable\"`, `\"E - Unreliable\"`, `\"F - Reliability cannot be judged\"`) | **expirationPolicy** (string, one of `\"never\"`, `\"interval\"`, `\"indicatorType\"`) | **expirationInterval** (number, in minutes)

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
feed_indicators_request = demisto_client.demisto_api.FeedIndicatorsRequest() # FeedIndicatorsRequest | 

try:
    # Create feed indicators from JSON
    api_instance.create_feed_indicators_json(feed_indicators_request)
except ApiException as e:
    print("Exception when calling DefaultApi->create_feed_indicators_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feed_indicators_request** | [**FeedIndicatorsRequest**](FeedIndicatorsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_incident**
> IncidentWrapper create_incident(create_incident_request=create_incident_request)

Create single incident

Create or update incident according to JSON structure. To update incident custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip To get the actual key name you can also go to Demisto CLI and run /incident_add and look for the key that you would like to update  Use the 'createInvestigation\\: True' to start the investigation process automatically. (by running a playbook based on incident type.)

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
create_incident_request = demisto_client.demisto_api.CreateIncidentRequest() # CreateIncidentRequest |  (optional)

try:
    # Create single incident
    api_response = api_instance.create_incident(create_incident_request=create_incident_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_incident_request** | [**CreateIncidentRequest**](CreateIncidentRequest.md)|  | [optional] 

### Return type

[**IncidentWrapper**](IncidentWrapper.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_incident_json**
> IncidentWrapper create_incident_json()

Create incident from JSON

Create single incident from raw JSON, builds incident according to default mapping

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")

try:
    # Create incident from JSON
    api_response = api_instance.create_incident_json()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_incident_json: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IncidentWrapper**](IncidentWrapper.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_incidents_batch**
> IncidentSearchResponseWrapper create_incidents_batch(update_data_batch=update_data_batch)

Batch create incidents

Create or update an incidents batch To update incident custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip To get the actual key name you can also go to Demisto CLI and run /incident_add and look for the key that you would like to update

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_data_batch = demisto_client.demisto_api.UpdateDataBatch() # UpdateDataBatch |  (optional)

try:
    # Batch create incidents
    api_response = api_instance.create_incidents_batch(update_data_batch=update_data_batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_incidents_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_data_batch** | [**UpdateDataBatch**](UpdateDataBatch.md)|  | [optional] 

### Return type

[**IncidentSearchResponseWrapper**](IncidentSearchResponseWrapper.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **create_or_update_incident_type**
> IncidentType create_or_update_incident_type(incident_type=incident_type)

Create new Incident Type

API to create new Incident Type

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
incident_type = demisto_client.demisto_api.IncidentType() # IncidentType |  (optional)

try:
    # Create new Incident Type
    api_response = api_instance.create_or_update_incident_type(incident_type=incident_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_or_update_incident_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_type** | [**IncidentType**](IncidentType.md)|  | [optional] 

### Return type

[**IncidentType**](IncidentType.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_ad_hoc_task**
> InvestigationPlaybook delete_ad_hoc_task(investigation_id, inv_pb_task_id)

Delete ad-hoc task

Delete an ad-hoc task from a running playbook

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
investigation_id = 'investigation_id_example' # str | investigation ID
inv_pb_task_id = 'inv_pb_task_id_example' # str | ad-hoc task ID

try:
    # Delete ad-hoc task
    api_response = api_instance.delete_ad_hoc_task(investigation_id, inv_pb_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_ad_hoc_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**| investigation ID | 
 **inv_pb_task_id** | **str**| ad-hoc task ID | 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_automation_script**
> delete_automation_script(automation_script_filter_wrapper=automation_script_filter_wrapper)

Delete existing automation

Delete a given automation from the system.

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
automation_script_filter_wrapper = demisto_client.demisto_api.AutomationScriptFilterWrapper() # AutomationScriptFilterWrapper |  (optional)

try:
    # Delete existing automation
    api_instance.delete_automation_script(automation_script_filter_wrapper=automation_script_filter_wrapper)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_automation_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_script_filter_wrapper** | [**AutomationScriptFilterWrapper**](AutomationScriptFilterWrapper.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_evidence_op**
> delete_evidence_op(delete_evidence_id=delete_evidence_id)

delete evidence

Delete an evidence entity

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
delete_evidence_id = demisto_client.demisto_api.DeleteEvidence() # DeleteEvidence |  (optional)

try:
    # delete evidence
    api_instance.delete_evidence_op(delete_evidence_id=delete_evidence_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_evidence_op: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_evidence_id** | [**DeleteEvidence**](DeleteEvidence.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_incidents_batch**
> IncidentSearchResponseWrapper delete_incidents_batch(update_data_batch=update_data_batch)

Batch delete incidents

Deletes an incidents batch

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_data_batch = demisto_client.demisto_api.UpdateDataBatch() # UpdateDataBatch |  (optional)

try:
    # Batch delete incidents
    api_response = api_instance.delete_incidents_batch(update_data_batch=update_data_batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_incidents_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_data_batch** | [**UpdateDataBatch**](UpdateDataBatch.md)|  | [optional] 

### Return type

[**IncidentSearchResponseWrapper**](IncidentSearchResponseWrapper.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_indicators_batch**
> UpdateResponse delete_indicators_batch(generic_indicator_update_batch=generic_indicator_update_batch)

Batch whitelist or delete indicators

Batch whitelist or delete indicators entities In order to delete indicators and not whitelist, set doNotWhitelist boolean field to true

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
generic_indicator_update_batch = demisto_client.demisto_api.GenericIndicatorUpdateBatch() # GenericIndicatorUpdateBatch |  (optional)

try:
    # Batch whitelist or delete indicators
    api_response = api_instance.delete_indicators_batch(generic_indicator_update_batch=generic_indicator_update_batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_indicators_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_indicator_update_batch** | [**GenericIndicatorUpdateBatch**](GenericIndicatorUpdateBatch.md)|  | [optional] 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_widget**
> delete_widget(id)

Remove existing widget

Remove a given widget Id from the system.

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | Widget id to remove (returned from widget save or widgets get)

try:
    # Remove existing widget
    api_instance.delete_widget(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Widget id to remove (returned from widget save or widgets get) | 

### Return type

void (empty response body)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **download_file**
> file download_file(entryid)

Download file

Download file from Demisto by entry ID

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
entryid = 'entryid_example' # str | Entry ID

try:
    # Download file
    api_response = api_instance.download_file(entryid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entryid** | **str**| Entry ID | 

### Return type

[**file**](file.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **download_latest_report**
> file download_latest_report(id)

Get latest report by ID

Get the latest report by its ID

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | the ID of the report to get

try:
    # Get latest report by ID
    api_response = api_instance.download_latest_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->download_latest_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the report to get | 

### Return type

[**file**](file.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **edit_ad_hoc_task**
> InvestigationPlaybook edit_ad_hoc_task(investigation_id, inv_playbook_task_data=inv_playbook_task_data)

Edit ad-hoc task

Edit an ad-hoc task in a running playbook

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
investigation_id = 'investigation_id_example' # str | investigation ID
inv_playbook_task_data = demisto_client.demisto_api.InvPlaybookTaskData() # InvPlaybookTaskData |  (optional)

try:
    # Edit ad-hoc task
    api_response = api_instance.edit_ad_hoc_task(investigation_id, inv_playbook_task_data=inv_playbook_task_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->edit_ad_hoc_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**| investigation ID | 
 **inv_playbook_task_data** | [**InvPlaybookTaskData**](InvPlaybookTaskData.md)|  | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **entry_export_artifact**
> str entry_export_artifact(download_entry=download_entry)

Export Artifact

Export an entry artifact

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
download_entry = demisto_client.demisto_api.DownloadEntry() # DownloadEntry |  (optional)

try:
    # Export Artifact
    api_response = api_instance.entry_export_artifact(download_entry=download_entry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->entry_export_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_entry** | [**DownloadEntry**](DownloadEntry.md)|  | [optional] 

### Return type

**str**

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **execute_report**
> execute_report(id, request_id)

Execute report

Execute a new report

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | the ID of the report to get
request_id = 'request_id_example' # str | the ID to register the request under

try:
    # Execute report
    api_instance.execute_report(id, request_id)
except ApiException as e:
    print("Exception when calling DefaultApi->execute_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the report to get | 
 **request_id** | **str**| the ID to register the request under | 

### Return type

void (empty response body)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **export_incidents_to_csv_batch**
> str export_incidents_to_csv_batch(update_data_batch=update_data_batch)

Batch export incidents to csv

Exports an incidents batch to CSV file (returns file ID)

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_data_batch = demisto_client.demisto_api.UpdateDataBatch() # UpdateDataBatch |  (optional)

try:
    # Batch export incidents to csv
    api_response = api_instance.export_incidents_to_csv_batch(update_data_batch=update_data_batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->export_incidents_to_csv_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_data_batch** | [**UpdateDataBatch**](UpdateDataBatch.md)|  | [optional] 

### Return type

**str**

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **export_indicators_to_csv_batch**
> str export_indicators_to_csv_batch(generic_indicator_update_batch=generic_indicator_update_batch)

Batch export indicators to csv

Exports an indicators batch to CSV file (returns file ID)

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
generic_indicator_update_batch = demisto_client.demisto_api.GenericIndicatorUpdateBatch() # GenericIndicatorUpdateBatch | Required parameters from `genericIndicatorUpdateBatch`: `columns`, `filter`. You should also include either `all` or `ids`  (optional)

try:
    # Batch export indicators to csv
    api_response = api_instance.export_indicators_to_csv_batch(generic_indicator_update_batch=generic_indicator_update_batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->export_indicators_to_csv_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_indicator_update_batch** | [**GenericIndicatorUpdateBatch**](GenericIndicatorUpdateBatch.md)| Required parameters from &#x60;genericIndicatorUpdateBatch&#x60;: &#x60;columns&#x60;, &#x60;filter&#x60;. You should also include either &#x60;all&#x60; or &#x60;ids&#x60;  | [optional] 

### Return type

**str**

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **export_indicators_to_stix_batch**
> str export_indicators_to_stix_batch(generic_indicator_update_batch=generic_indicator_update_batch)

Batch export indicators to STIX

Exports an indicators batch to STIX file (returns file ID)

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
generic_indicator_update_batch = demisto_client.demisto_api.GenericIndicatorUpdateBatch() # GenericIndicatorUpdateBatch |  (optional)

try:
    # Batch export indicators to STIX
    api_response = api_instance.export_indicators_to_stix_batch(generic_indicator_update_batch=generic_indicator_update_batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->export_indicators_to_stix_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_indicator_update_batch** | [**GenericIndicatorUpdateBatch**](GenericIndicatorUpdateBatch.md)|  | [optional] 

### Return type

**str**

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_all_reports**
> list[Report] get_all_reports()

Get all reports

Get all of the reports

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")

try:
    # Get all reports
    api_response = api_instance.get_all_reports()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_reports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Report]**](Report.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_all_widgets**
> list[Widget] get_all_widgets()



Get all widgets

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")

try:
    api_response = api_instance.get_all_widgets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_widgets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Widget]**](Widget.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_audits**
> AuditResult get_audits(filter=filter)

Get Audits

Get audits by filter

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
filter = demisto_client.demisto_api.GenericStringDateFilter() # GenericStringDateFilter |  (optional)

try:
    # Get Audits
    api_response = api_instance.get_audits(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_audits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**GenericStringDateFilter**](GenericStringDateFilter.md)|  | [optional] 

### Return type

[**AuditResult**](AuditResult.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_automation_scripts**
> AutomationScriptResult get_automation_scripts(automation_script_filter=automation_script_filter)

Search Automation (aka scripts)

Search Automation by filter

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
automation_script_filter = demisto_client.demisto_api.AutomationScriptFilter() # AutomationScriptFilter |  (optional)

try:
    # Search Automation (aka scripts)
    api_response = api_instance.get_automation_scripts(automation_script_filter=automation_script_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_automation_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_script_filter** | [**AutomationScriptFilter**](AutomationScriptFilter.md)|  | [optional] 

### Return type

[**AutomationScriptResult**](AutomationScriptResult.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_docker_images**
> DockerImagesResult get_docker_images()

Get Docker Images

Get list of all available docker image names

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")

try:
    # Get Docker Images
    api_response = api_instance.get_docker_images()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_docker_images: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DockerImagesResult**](DockerImagesResult.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_entry_artifact**
> file get_entry_artifact(id)

Get entry artifact

Get the entry artifact file

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | file to fetch (returned from entry export artifact call)

try:
    # Get entry artifact
    api_response = api_instance.get_entry_artifact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_entry_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| file to fetch (returned from entry export artifact call) | 

### Return type

[**file**](file.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_incident_as_csv**
> file get_incident_as_csv(id)

Get incident as CSV

Get an incident CSV file that was exported, by ID

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | CSV file to fetch (returned from batch export to csv call)

try:
    # Get incident as CSV
    api_response = api_instance.get_incident_as_csv(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_incident_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CSV file to fetch (returned from batch export to csv call) | 

### Return type

[**file**](file.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_incidents_fields_by_incident_type**
> list[IncidentField] get_incidents_fields_by_incident_type(type)

Get all incident fields associated with incident type

Get all incident fields associated with incident type

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
type = 'type_example' # str | the name (case sensitive) of the incident type

try:
    # Get all incident fields associated with incident type
    api_response = api_instance.get_incidents_fields_by_incident_type(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_incidents_fields_by_incident_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| the name (case sensitive) of the incident type | 

### Return type

[**list[IncidentField]**](IncidentField.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_indicators_as_csv**
> file get_indicators_as_csv(id)

Get indicators as CSV

Get an indicators CSV file that was exported, by ID

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | CSV file to fetch (returned from batch export to csv call)

try:
    # Get indicators as CSV
    api_response = api_instance.get_indicators_as_csv(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_indicators_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CSV file to fetch (returned from batch export to csv call) | 

### Return type

[**file**](file.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_indicators_as_stix**
> file get_indicators_as_stix(id)

Get indicators as STIX V2

Get an indicators STIX V2 file that was exported, by ID

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | STIX V2 file to fetch (returned from batch export to STIX call)

try:
    # Get indicators as STIX V2
    api_response = api_instance.get_indicators_as_stix(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_indicators_as_stix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| STIX V2 file to fetch (returned from batch export to STIX call) | 

### Return type

[**file**](file.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_report_by_id**
> Report get_report_by_id(id)

Get report by ID

Get a report by its ID

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | the ID of the report to get

try:
    # Get report by ID
    api_response = api_instance.get_report_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the report to get | 

### Return type

[**Report**](Report.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_stats_for_dashboard**
> list[StatsQueryResponse] get_stats_for_dashboard()

Get Dashboard Statistics

Get a given dashboard statistics result.

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")

try:
    # Get Dashboard Statistics
    api_response = api_instance.get_stats_for_dashboard()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_stats_for_dashboard: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StatsQueryResponse]**](StatsQueryResponse.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_stats_for_widget**
> object get_stats_for_widget()

Get Widget Statistics

Get a given widget object statistics result. Note: This route has many return types based on the widget type and data. Each 200X represent a 200 OK request of specific widget type and data

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")

try:
    # Get Widget Statistics
    api_response = api_instance.get_stats_for_widget()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_stats_for_widget: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_widget**
> Widget get_widget(id)

Get widget by ID

Get a widget object by a given ID.

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | The ID of widget to get.

try:
    # Get widget by ID
    api_response = api_instance.get_widget(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of widget to get. | 

### Return type

[**Widget**](Widget.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **import_classifier**
> InstanceClassifier import_classifier(file)

Import a classifier

Import a classifier to Cortex XSOAR

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file
classifier_id = 'classifier_id_example' # str | associated typeID for the layout

try:
    # Import a classifier
    api_response = api_instance.import_classifier(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_classifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 
 **classifier_id** | **str**| associated typeID for the layout | 

### Return type

[**InstanceClassifier**](InstanceClassifier.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **import_dashboard**
> Dashboard import_dashboard(file)

Import a dashboard

Import a dashboard to Cortex XSOAR

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file

try:
    # Import a dashboard
    api_response = api_instance.import_dashboard(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **import_incident_fields**
> IncidentField import_incident_fields(file)

Import an incidents field

Import an incidents field to Cortex XSOAR

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file

try:
    # Import an incidents field
    api_response = api_instance.import_incident_fields(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_incident_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

[**IncidentField**](IncidentField.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **import_incident_types_handler**
> IncidentType import_incident_types_handler(file)

Import an incident type

Import an incident type to Cortex XSOAR

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file

try:
    # Import an incident type
    api_response = api_instance.import_incident_types_handler(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_incident_types_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

[**IncidentType**](IncidentType.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **import_layout**
> LayoutAPI import_layout(file)

Import a layout

Import a layout to Cortex XSOAR

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file
type = 'type_example' # str | associated typeID for the layout
kind = 'kind_example' # str | layout kind details

try:
    # Import a layout
    api_response = api_instance.import_layout(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

[**LayoutAPI**](LayoutAPI.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **import_playbook**
> Playbook import_playbook(file)

Import and override playbook

Import and override playbook in Cortex XSOAR

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file

try:
    # Import and override playbook
    api_response = api_instance.import_playbook(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_playbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

[**Playbook**](Playbook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **import_script**
> AutomationScript import_script(file)

Upload an automation

Upload an automation to Cortex XSOAR

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file

try:
    # Upload an automation
    api_response = api_instance.import_script(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

[**AutomationScript**](AutomationScript.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **import_widget**
> Widget import_widget(file)

Import a widget

Import a widget to the system, ignoring ID or version, used to import new widgets.

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file

try:
    # Import a widget
    api_response = api_instance.import_widget(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->import_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

[**Widget**](Widget.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **incident_file_upload**
> IncidentWrapper incident_file_upload(id, file, file_name=file_name, file_comment=file_comment, field=field, show_media_file=show_media_file, last=last)



Add file attachement to an incidents

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
id = 'id_example' # str | Incident id to update
file = '/path/to/file.txt' # file | file
file_name = 'file_name_example' # str | file name (optional)
file_comment = 'file_comment_example' # str | file comment (optional)
field = 'field_example' # str | field name to hold the attachment details. If not specified, `attachment` will be used. (optional)
show_media_file = true # bool | show media file (optional)
last = true # bool | If set to true will create an investigation. Used for uploading after creating incident. (optional)

try:
    api_response = api_instance.incident_file_upload(id, file, file_name=file_name, file_comment=file_comment, field=field, show_media_file=show_media_file, last=last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->incident_file_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Incident id to update | 
 **file** | **file**| file | 
 **file_name** | **str**| file name | [optional] 
 **file_comment** | **str**| file comment | [optional] 
 **field** | **str**| field name to hold the attachment details. If not specified, &#x60;attachment&#x60; will be used. | [optional] 
 **show_media_file** | **bool**| show media file | [optional] 
 **last** | **bool**| If set to true will create an investigation. Used for uploading after creating incident. | [optional] 

### Return type

[**IncidentWrapper**](IncidentWrapper.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **indicator_whitelist**
> UpdateResponse indicator_whitelist(update_indicator_reputation_data=update_indicator_reputation_data)

Whitelists or deletes Indicator

Whitelists or deletes an indicator entity In order to delete an indicator and not whitelist, set doNotWhitelist boolean field to true

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_indicator_reputation_data = demisto_client.demisto_api.UpdateIndicatorReputationData() # UpdateIndicatorReputationData |  (optional)

try:
    # Whitelists or deletes Indicator
    api_response = api_instance.indicator_whitelist(update_indicator_reputation_data=update_indicator_reputation_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->indicator_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_indicator_reputation_data** | [**UpdateIndicatorReputationData**](UpdateIndicatorReputationData.md)|  | [optional] 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **indicators_create**
> IocObject indicators_create(ioc_object=ioc_object)

Create Indicator

Create an indicator entity To update indicator custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
ioc_object = demisto_client.demisto_api.IndicatorContext() # IndicatorContext |  (optional)

try:
    # Create Indicator
    api_response = api_instance.indicators_create(ioc_object=ioc_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->indicators_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ioc_object** | [**IndicatorContext**](IndicatorContext.md)|  | [optional] 

### Return type

[**IocObject**](IocObject.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **indicators_create_batch**
> IocObjects indicators_create_batch(file, file_name=file_name)

Create indicators

Create indicators from a file

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file
file_name = 'file_name_example' # str | file name (optional)

try:
    # Create indicators
    api_response = api_instance.indicators_create_batch(file, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->indicators_create_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 
 **file_name** | **str**| file name | [optional] 

### Return type

[**IocObjects**](IocObjects.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **indicators_edit**
> IocObject indicators_edit(ioc_object=ioc_object)

Edit Indicator

Edit an indicator entity To update indicator custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
ioc_object = demisto_client.demisto_api.IocObject() # IocObject |  (optional)

try:
    # Edit Indicator
    api_response = api_instance.indicators_edit(ioc_object=ioc_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->indicators_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ioc_object** | [**IocObject**](IocObject.md)|  | [optional] 

### Return type

[**IocObject**](IocObject.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **indicators_search**
> IndicatorResult indicators_search(indicator_filter=indicator_filter)

Search indicators

Search indicators by filter

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
indicator_filter = demisto_client.demisto_api.IndicatorFilter() # IndicatorFilter |  (optional)

try:
    # Search indicators
    api_response = api_instance.indicators_search(indicator_filter=indicator_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->indicators_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indicator_filter** | [**IndicatorFilter**](IndicatorFilter.md)|  | [optional] 

### Return type

[**IndicatorResult**](IndicatorResult.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **integration_upload**
> ModuleConfiguration integration_upload(file)

Upload an integration

Upload an integration to Demisto

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
file = '/path/to/file.txt' # file | file

try:
    # Upload an integration
    api_response = api_instance.integration_upload(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->integration_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 

### Return type

[**ModuleConfiguration**](ModuleConfiguration.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **investigation_add_entries_sync**
> list[Entry] investigation_add_entries_sync(update_entry=update_entry)

Create new entry in existing investigation

API to create an entry (markdown format) in existing investigation Body example: {\"investigationId\":\"1234\",\"data\":\"entry content…\"}

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_entry = demisto_client.demisto_api.UpdateEntry() # UpdateEntry |  (optional)

try:
    # Create new entry in existing investigation
    api_response = api_instance.investigation_add_entries_sync(update_entry=update_entry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->investigation_add_entries_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_entry** | [**UpdateEntry**](UpdateEntry.md)|  | [optional] 

### Return type

[**list[Entry]**](Entry.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **investigation_add_entry_handler**
> Entry investigation_add_entry_handler(update_entry=update_entry)

Create new entry in existing investigation

API to create an entry (markdown format) in existing investigation Body example: {\"investigationId\":\"1234\",\"data\":\"entry content…\"}

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_entry = demisto_client.demisto_api.UpdateEntry() # UpdateEntry |  (optional)

try:
    # Create new entry in existing investigation
    api_response = api_instance.investigation_add_entry_handler(update_entry=update_entry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->investigation_add_entry_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_entry** | [**UpdateEntry**](UpdateEntry.md)|  | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **investigation_add_formatted_entry_handler**
> Entry investigation_add_formatted_entry_handler(uploaded_entry=uploaded_entry)

Create new formatted entry in existing investigation

API to create a formatted entry (table/json/text/markdown/html) in existing investigation Body example: {\"investigationId\":\"1234\",\"format\":\"table/json/text/markdown/html\",\"contents\":\"entry content…\"}

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
uploaded_entry = demisto_client.demisto_api.UploadedEntry() # UploadedEntry |  (optional)

try:
    # Create new formatted entry in existing investigation
    api_response = api_instance.investigation_add_formatted_entry_handler(uploaded_entry=uploaded_entry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->investigation_add_formatted_entry_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uploaded_entry** | [**UploadedEntry**](UploadedEntry.md)|  | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **revoke_user_api_key**
> revoke_user_api_key(username)



Revoke API Key for user

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
username = 'username_example' # str | The username which the API keys assigned to

try:
    api_instance.revoke_user_api_key(username)
except ApiException as e:
    print("Exception when calling DefaultApi->revoke_user_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username which the API keys assigned to | 

### Return type

void (empty response body)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **save_evidence**
> Evidence save_evidence(evidence=evidence)

Save evidence

Save an evidence entity To update evidence custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
evidence = demisto_client.demisto_api.Evidence() # Evidence |  (optional)

try:
    # Save evidence
    api_response = api_instance.save_evidence(evidence=evidence)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->save_evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evidence** | [**Evidence**](Evidence.md)|  | [optional] 

### Return type

[**Evidence**](Evidence.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **save_or_update_script**
> AutomationScriptResult save_or_update_script(automation_script_filter_wrapper=automation_script_filter_wrapper)

Create or update automation

Create or update a given automation.

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
automation_script_filter_wrapper = demisto_client.demisto_api.AutomationScriptFilterWrapper() # AutomationScriptFilterWrapper |  (optional)

try:
    # Create or update automation
    api_response = api_instance.save_or_update_script(automation_script_filter_wrapper=automation_script_filter_wrapper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->save_or_update_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_script_filter_wrapper** | [**AutomationScriptFilterWrapper**](AutomationScriptFilterWrapper.md)|  | [optional] 

### Return type

[**AutomationScriptResult**](AutomationScriptResult.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **save_widget**
> Widget save_widget(widget=widget)

Add or update a widget

Add or update a given widget based on Id.

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
widget = demisto_client.demisto_api.Widget() # Widget |  (optional)

try:
    # Add or update a widget
    api_response = api_instance.save_widget(widget=widget)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->save_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget** | [**Widget**](Widget.md)|  | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **search_evidence**
> EvidencesSearchResponse search_evidence(evidences_filter_wrapper=evidences_filter_wrapper)

Search evidence

Search for an evidence entutiy by filter

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
evidences_filter_wrapper = demisto_client.demisto_api.EvidencesFilterWrapper() # EvidencesFilterWrapper |  (optional)

try:
    # Search evidence
    api_response = api_instance.search_evidence(evidences_filter_wrapper=evidences_filter_wrapper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evidences_filter_wrapper** | [**EvidencesFilterWrapper**](EvidencesFilterWrapper.md)|  | [optional] 

### Return type

[**EvidencesSearchResponse**](EvidencesSearchResponse.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **search_incidents**
> InlineResponse200 search_incidents(filter)

Search incidents by filter

This will search incidents across all indices You can filter by multiple options

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
filter = demisto_client.demisto_api.SearchIncidentsData() # SearchIncidentsData | 

try:
    # Search incidents by filter
    api_response = api_instance.search_incidents(filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**SearchIncidentsData**](SearchIncidentsData.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **search_investigations**
> InvestigationSearchResponse search_investigations(filter=filter)

Search investigations by filter

This will search investigations across all indices You can filter by multiple options

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
filter = demisto_client.demisto_api.InvestigationFilter() # InvestigationFilter |  (optional)

try:
    # Search investigations by filter
    api_response = api_instance.search_investigations(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_investigations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**InvestigationFilter**](InvestigationFilter.md)|  | [optional] 

### Return type

[**InvestigationSearchResponse**](InvestigationSearchResponse.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **simple_complete_task**
> InvestigationPlaybook simple_complete_task(inv_task_info=inv_task_info)

Complete task simple (no file)

Complete a task without a file attachment

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
inv_task_info = demisto_client.demisto_api.InvTaskInfo() # InvTaskInfo |  (optional)

try:
    # Complete task simple (no file)
    api_response = api_instance.simple_complete_task(inv_task_info=inv_task_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->simple_complete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inv_task_info** | [**InvTaskInfo**](InvTaskInfo.md)|  | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **submit_task_form**
> InvestigationPlaybook submit_task_form(investigation_id, task_id, answers, file=file)

Complete a task

Submit a data collection task with given answers and multiple file attachments

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
investigation_id = 'investigation_id_example' # str | investigation ID
task_id = 'task_id_example' # str | Task Id
answers = 'answers_example' # str | the answers to the task form. Answers are keyed by numerical question id
file = '/path/to/file.txt' # file | Files to attach to the task (optional)

try:
    # Complete a task
    api_response = api_instance.submit_task_form(investigation_id, task_id, answers, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->submit_task_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**| investigation ID | 
 **task_id** | **str**| Task Id | 
 **answers** | **str**| the answers to the task form. Answers are keyed by numerical question id | 
 **file** | **file**| Files to attach to the task | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **task_add_comment**
> InvestigationPlaybook task_add_comment(inv_task_info=inv_task_info)

Task add comment

Add comment to a task

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
inv_task_info = demisto_client.demisto_api.InvTaskInfo() # InvTaskInfo |  (optional)

try:
    # Task add comment
    api_response = api_instance.task_add_comment(inv_task_info=inv_task_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->task_add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inv_task_info** | [**InvTaskInfo**](InvTaskInfo.md)|  | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **task_assign**
> InvestigationPlaybook task_assign(inv_playbook_assignee=inv_playbook_assignee)

Assign task

Assign a task to an owner

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
inv_playbook_assignee = demisto_client.demisto_api.InvPlaybookAssignee() # InvPlaybookAssignee |  (optional)

try:
    # Assign task
    api_response = api_instance.task_assign(inv_playbook_assignee=inv_playbook_assignee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->task_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inv_playbook_assignee** | [**InvPlaybookAssignee**](InvPlaybookAssignee.md)|  | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **task_set_due**
> InvestigationPlaybook task_set_due(inv_playbook_due=inv_playbook_due)

Set task due date

Set the task due date

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
inv_playbook_due = demisto_client.demisto_api.InvPlaybookDue() # InvPlaybookDue |  (optional)

try:
    # Set task due date
    api_response = api_instance.task_set_due(inv_playbook_due=inv_playbook_due)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->task_set_due: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inv_playbook_due** | [**InvPlaybookDue**](InvPlaybookDue.md)|  | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **task_un_complete**
> InvestigationPlaybook task_un_complete(inv_task_info=inv_task_info)

Un complete a task

Reopen a closed task and change the status to uncomplete

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
inv_task_info = demisto_client.demisto_api.InvTaskInfo() # InvTaskInfo |  (optional)

try:
    # Un complete a task
    api_response = api_instance.task_un_complete(inv_task_info=inv_task_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->task_un_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inv_task_info** | [**InvTaskInfo**](InvTaskInfo.md)|  | [optional] 

### Return type

[**InvestigationPlaybook**](InvestigationPlaybook.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_entry_note**
> Entry update_entry_note(update_entry=update_entry)

Mark entry as note

API to mark entry as note, can be used also to remove the note Body example: {\"id\":1\\@1234\",\"version\":\"-1\",\"investigationId\":\"1234\",\"data\":\"true/false\"}

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_entry = demisto_client.demisto_api.UpdateEntry() # UpdateEntry |  (optional)

try:
    # Mark entry as note
    api_response = api_instance.update_entry_note(update_entry=update_entry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_entry_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_entry** | [**UpdateEntry**](UpdateEntry.md)|  | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_entry_tags_op**
> Entry update_entry_tags_op(update_entry_tags=update_entry_tags)

Set entry tags

API to set entry tags Body example: {\"id\":\"1\\@1234\",\"version\":\"-1\",\"investigationId\":\"1234\",\"tags\":[\"tag1\",\"tag2\"]\"}

### Example
```python
from __future__ import print_function
import time
import demisto_client
import demisto_client.demisto_api
from demisto_client.demisto_api.rest import ApiException
from pprint import pprint

api_instance = demisto_client.configure(base_url="https://YOUR_DEMISTO_SERVER", api_key="YOUR_API_KEY")
update_entry_tags = demisto_client.demisto_api.UpdateEntryTags() # UpdateEntryTags |  (optional)

try:
    # Set entry tags
    api_response = api_instance.update_entry_tags_op(update_entry_tags=update_entry_tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_entry_tags_op: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_entry_tags** | [**UpdateEntryTags**](UpdateEntryTags.md)|  | [optional] 

### Return type

[**Entry**](Entry.md)

### Authorization

[api_key](README.md#api_key), [csrf_token](README.md#csrf_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

