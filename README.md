# Demisto API Python Client
This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client. 
Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 
'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on 
the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you 
to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users
 data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the
  data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s?
   To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and
    Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict
     error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using
      'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: 
      application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed
       -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```


## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install


```sh
pip install demisto-py
```

Then import the package:
```python
import demisto 
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import demisto
from demisto.rest import ApiException
from pprint import pprint


api_key = 'GENERATED_API_TOKEN'
host = 'DEMISTO_HOSTNAME'

api_instance = demisto.connection(hostname=host, api_key=api_key)
investigation_id = 'investigation_id_example'  # str | investigation ID
inv_playbook_task_data = demisto.InvPlaybookTaskData()  # InvPlaybookTaskData |  (optional)

try:
    # Add ad-hoc task
    api_response = api_instance.add_ad_hoc_task(investigation_id, inv_playbook_task_data=inv_playbook_task_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DemistoApi->add_ad_hoc_task: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to your Demisto Hostname.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DemistoApi* | [**add_ad_hoc_task**](docs/DemistoApi.md#add_ad_hoc_task) | **POST** /inv-playbook/task/add/{investigationId} | Add ad-hoc task
*DemistoApi* | [**close_incidents_batch**](docs/DemistoApi.md#close_incidents_batch) | **POST** /incident/batchClose | Batch close incidents
*DemistoApi* | [**complete_task**](docs/DemistoApi.md#complete_task) | **POST** /inv-playbook/task/complete | [Deprecated] Complete a task
*DemistoApi* | [**complete_task_v2**](docs/DemistoApi.md#complete_task_v2) | **POST** /v2/inv-playbook/task/complete | Complete a task
*DemistoApi* | [**copy_script**](docs/DemistoApi.md#copy_script) | **POST** /automation/copy | Copy automation
*DemistoApi* | [**create_docker_image**](docs/DemistoApi.md#create_docker_image) | **POST** /settings/docker-images | Create Image
*DemistoApi* | [**create_incident**](docs/DemistoApi.md#create_incident) | **POST** /incident | Create single incident
*DemistoApi* | [**create_incident_json**](docs/DemistoApi.md#create_incident_json) | **POST** /incident/json | Create incident from JSON
*DemistoApi* | [**create_incidents_batch**](docs/DemistoApi.md#create_incidents_batch) | **POST** /incident/batch | Batch create incidents
*DemistoApi* | [**create_or_update_incident_type**](docs/DemistoApi.md#create_or_update_incident_type) | **POST** /incidenttype | Create new Incident Type
*DemistoApi* | [**delete_ad_hoc_task**](docs/DemistoApi.md#delete_ad_hoc_task) | **POST** /inv-playbook/task/delete/{investigationId}/{invPBTaskId} | Delete ad-hoc task
*DemistoApi* | [**delete_automation_script**](docs/DemistoApi.md#delete_automation_script) | **POST** /automation/delete | Delete existing automation
*DemistoApi* | [**delete_evidence_op**](docs/DemistoApi.md#delete_evidence_op) | **POST** /evidence/delete | delete evidence
*DemistoApi* | [**delete_incidents_batch**](docs/DemistoApi.md#delete_incidents_batch) | **POST** /incident/batchDelete | Batch delete incidents
*DemistoApi* | [**delete_indicators_batch**](docs/DemistoApi.md#delete_indicators_batch) | **POST** /indicators/batchDelete | Batch whitelist or delete indicators
*DemistoApi* | [**delete_widget**](docs/DemistoApi.md#delete_widget) | **DELETE** /widgets/{id} | Remove existing widget
*DemistoApi* | [**download_latest_report**](docs/DemistoApi.md#download_latest_report) | **GET** /reports/{id}/latest | Get latest report by ID
*DemistoApi* | [**edit_ad_hoc_task**](docs/DemistoApi.md#edit_ad_hoc_task) | **POST** /inv-playbook/task/edit/{investigationId} | Edit ad-hoc task
*DemistoApi* | [**entry_export_artifact**](docs/DemistoApi.md#entry_export_artifact) | **POST** /entry/exportArtifact | Export Artifact
*DemistoApi* | [**execute_report**](docs/DemistoApi.md#execute_report) | **POST** /report/{id}/{requestId}/execute | Execute report
*DemistoApi* | [**export_incidents_to_csv_batch**](docs/DemistoApi.md#export_incidents_to_csv_batch) | **POST** /incident/batch/exportToCsv | Batch export incidents to csv
*DemistoApi* | [**export_indicators_to_csv_batch**](docs/DemistoApi.md#export_indicators_to_csv_batch) | **POST** /indicators/batch/exportToCsv | Batch export indicators to csv
*DemistoApi* | [**export_indicators_to_stix_batch**](docs/DemistoApi.md#export_indicators_to_stix_batch) | **POST** /indicators/batch/export/stix | Batch export indicators to STIX
*DemistoApi* | [**get_all_reports**](docs/DemistoApi.md#get_all_reports) | **GET** /reports | Get all reports
*DemistoApi* | [**get_all_widgets**](docs/DemistoApi.md#get_all_widgets) | **GET** /widgets | 
*DemistoApi* | [**get_audits**](docs/DemistoApi.md#get_audits) | **POST** /settings/audits | Get Audits
*DemistoApi* | [**get_automation_script**](docs/DemistoApi.md#get_automation_script) | **POST** /automation/load/{id} | Load Automation
*DemistoApi* | [**get_automation_scripts**](docs/DemistoApi.md#get_automation_scripts) | **POST** /automation/search | Search Automation (aka scripts)
*DemistoApi* | [**get_docker_images**](docs/DemistoApi.md#get_docker_images) | **GET** /settings/docker-images | Get Docker Images
*DemistoApi* | [**get_entry_artifact**](docs/DemistoApi.md#get_entry_artifact) | **GET** /entry/artifact/{id} | Get entry artifact
*DemistoApi* | [**get_incident_as_csv**](docs/DemistoApi.md#get_incident_as_csv) | **GET** /incident/csv/{id} | Get incident as CSV
*DemistoApi* | [**get_incidents_fields_by_incident_type**](docs/DemistoApi.md#get_incidents_fields_by_incident_type) | **GET** /incidentfields/associatedTypes/{type} | Get all incident fields associated with incident type
*DemistoApi* | [**get_indicators_as_csv**](docs/DemistoApi.md#get_indicators_as_csv) | **GET** /indicators/csv/{id} | Get indicators as CSV
*DemistoApi* | [**get_indicators_as_stix**](docs/DemistoApi.md#get_indicators_as_stix) | **GET** /indicators/stix/v2/{id} | Get indicators as STIX V2
*DemistoApi* | [**get_report_by_id**](docs/DemistoApi.md#get_report_by_id) | **GET** /reports/{id} | Get report by ID
*DemistoApi* | [**get_stats_for_dashboard**](docs/DemistoApi.md#get_stats_for_dashboard) | **POST** /statistics/dashboards/query | Get Dashboard Statistics
*DemistoApi* | [**get_stats_for_widget**](docs/DemistoApi.md#get_stats_for_widget) | **POST** /statistics/widgets/query | Get Widget Statistics
*DemistoApi* | [**get_widget**](docs/DemistoApi.md#get_widget) | **GET** /widgets/{id} | Get widget by ID
*DemistoApi* | [**import_widget**](docs/DemistoApi.md#import_widget) | **POST** /widgets/import | Import a widget
*DemistoApi* | [**indicator_whitelist**](docs/DemistoApi.md#indicator_whitelist) | **POST** /indicator/whitelist | Whitelists or deletes Indicator
*DemistoApi* | [**indicators_create**](docs/DemistoApi.md#indicators_create) | **POST** /indicator/create | Create Indicator
*DemistoApi* | [**indicators_create_batch**](docs/DemistoApi.md#indicators_create_batch) | **POST** /indicators/upload | Create indicators
*DemistoApi* | [**indicators_edit**](docs/DemistoApi.md#indicators_edit) | **POST** /indicator/edit | Edit Indicator
*DemistoApi* | [**indicators_search**](docs/DemistoApi.md#indicators_search) | **POST** /indicators/search | Search indicators
*DemistoApi* | [**investigation_add_entry_handler**](docs/DemistoApi.md#investigation_add_entry_handler) | **POST** /entry | Create new entry in existing investigation
*DemistoApi* | [**investigation_add_formatted_entry_handler**](docs/DemistoApi.md#investigation_add_formatted_entry_handler) | **POST** /entry/formatted | Create new formatted entry in existing investigation
*DemistoApi* | [**revoke_user_api_key**](docs/DemistoApi.md#revoke_user_api_key) | **POST** /apikeys/revoke/user/{username} | 
*DemistoApi* | [**save_evidence**](docs/DemistoApi.md#save_evidence) | **POST** /evidence | Save evidence
*DemistoApi* | [**save_or_update_script**](docs/DemistoApi.md#save_or_update_script) | **POST** /automation | Create or update automation
*DemistoApi* | [**save_widget**](docs/DemistoApi.md#save_widget) | **POST** /widgets | Add or update a widget
*DemistoApi* | [**search_evidence**](docs/DemistoApi.md#search_evidence) | **POST** /evidence/search | Search evidence
*DemistoApi* | [**search_incidents**](docs/DemistoApi.md#search_incidents) | **POST** /incidents/search | Search incidents by filter
*DemistoApi* | [**search_investigations**](docs/DemistoApi.md#search_investigations) | **POST** /investigations/search | Search investigations by filter
*DemistoApi* | [**simple_complete_task**](docs/DemistoApi.md#simple_complete_task) | **POST** /inv-playbook/task/complete/simple | Complete task simple (no file)
*DemistoApi* | [**submit_task_form**](docs/DemistoApi.md#submit_task_form) | **POST** /v2/inv-playbook/task/form/submit | Complete a task
*DemistoApi* | [**task_add_comment**](docs/DemistoApi.md#task_add_comment) | **POST** /inv-playbook/task/note/add | Task add comment
*DemistoApi* | [**task_assign**](docs/DemistoApi.md#task_assign) | **POST** /inv-playbook/task/assign | Assign task
*DemistoApi* | [**task_set_due**](docs/DemistoApi.md#task_set_due) | **POST** /inv-playbook/task/due | Set task due date
*DemistoApi* | [**task_un_complete**](docs/DemistoApi.md#task_un_complete) | **POST** /inv-playbook/task/uncomplete | Un complete a task
*DemistoApi* | [**update_entry_note**](docs/DemistoApi.md#update_entry_note) | **POST** /entry/note | Mark entry as note
*DemistoApi* | [**update_entry_tags_op**](docs/DemistoApi.md#update_entry_tags_op) | **POST** /entry/tags | Set entry tags


## Documentation For Models

 - [AdvanceArg](docs/AdvanceArg.md)
 - [ArgAtomicFilter](docs/ArgAtomicFilter.md)
 - [ArgFilter](docs/ArgFilter.md)
 - [ArgTransformer](docs/ArgTransformer.md)
 - [Argument](docs/Argument.md)
 - [ArrayPositions](docs/ArrayPositions.md)
 - [Attachment](docs/Attachment.md)
 - [Audit](docs/Audit.md)
 - [AuditResult](docs/AuditResult.md)
 - [AutomationScript](docs/AutomationScript.md)
 - [AutomationScriptAPI](docs/AutomationScriptAPI.md)
 - [AutomationScriptFilter](docs/AutomationScriptFilter.md)
 - [AutomationScriptFilterWrapper](docs/AutomationScriptFilterWrapper.md)
 - [AutomationScriptResult](docs/AutomationScriptResult.md)
 - [ComplexArg](docs/ComplexArg.md)
 - [CreateIncidentRequest](docs/CreateIncidentRequest.md)
 - [CustomFields](docs/CustomFields.md)
 - [DBotScore](docs/DBotScore.md)
 - [Dashboard](docs/Dashboard.md)
 - [DataCollectionForm](docs/DataCollectionForm.md)
 - [DateRange](docs/DateRange.md)
 - [DateRangeFilter](docs/DateRangeFilter.md)
 - [DeleteEvidence](docs/DeleteEvidence.md)
 - [DockerImage](docs/DockerImage.md)
 - [DockerImagesResult](docs/DockerImagesResult.md)
 - [DownloadEntry](docs/DownloadEntry.md)
 - [Duration](docs/Duration.md)
 - [EndingType](docs/EndingType.md)
 - [Entry](docs/Entry.md)
 - [EntryCategory](docs/EntryCategory.md)
 - [EntryHistory](docs/EntryHistory.md)
 - [EntryReputation](docs/EntryReputation.md)
 - [EntryTask](docs/EntryTask.md)
 - [EntryType](docs/EntryType.md)
 - [Evidence](docs/Evidence.md)
 - [EvidenceData](docs/EvidenceData.md)
 - [Evidences](docs/Evidences.md)
 - [EvidencesFilterWrapper](docs/EvidencesFilterWrapper.md)
 - [EvidencesSearchResponse](docs/EvidencesSearchResponse.md)
 - [FieldGroup](docs/FieldGroup.md)
 - [FieldMapping](docs/FieldMapping.md)
 - [FieldTermLocationMap](docs/FieldTermLocationMap.md)
 - [FileMetadata](docs/FileMetadata.md)
 - [FilterCache](docs/FilterCache.md)
 - [FilterOperatorID](docs/FilterOperatorID.md)
 - [GenericIndicatorUpdateBatch](docs/GenericIndicatorUpdateBatch.md)
 - [GenericStringDateFilter](docs/GenericStringDateFilter.md)
 - [GenericStringFilter](docs/GenericStringFilter.md)
 - [GridColumn](docs/GridColumn.md)
 - [Group](docs/Group.md)
 - [Groups](docs/Groups.md)
 - [HumanCron](docs/HumanCron.md)
 - [Important](docs/Important.md)
 - [Incident](docs/Incident.md)
 - [IncidentField](docs/IncidentField.md)
 - [IncidentFilter](docs/IncidentFilter.md)
 - [IncidentSearchResponseWrapper](docs/IncidentSearchResponseWrapper.md)
 - [IncidentStatus](docs/IncidentStatus.md)
 - [IncidentType](docs/IncidentType.md)
 - [IncidentWrapper](docs/IncidentWrapper.md)
 - [IndicatorContext](docs/IndicatorContext.md)
 - [IndicatorFilter](docs/IndicatorFilter.md)
 - [IndicatorResult](docs/IndicatorResult.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InsightCache](docs/InsightCache.md)
 - [InvPlaybookAssignee](docs/InvPlaybookAssignee.md)
 - [InvPlaybookDue](docs/InvPlaybookDue.md)
 - [InvPlaybookTaskCompleteData](docs/InvPlaybookTaskCompleteData.md)
 - [InvPlaybookTaskData](docs/InvPlaybookTaskData.md)
 - [InvTaskInfo](docs/InvTaskInfo.md)
 - [Investigation](docs/Investigation.md)
 - [InvestigationFilter](docs/InvestigationFilter.md)
 - [InvestigationPlaybook](docs/InvestigationPlaybook.md)
 - [InvestigationPlaybookData](docs/InvestigationPlaybookData.md)
 - [InvestigationPlaybookState](docs/InvestigationPlaybookState.md)
 - [InvestigationPlaybookTask](docs/InvestigationPlaybookTask.md)
 - [InvestigationPlaybookTasksAPI](docs/InvestigationPlaybookTasksAPI.md)
 - [InvestigationSearchResponse](docs/InvestigationSearchResponse.md)
 - [InvestigationStatus](docs/InvestigationStatus.md)
 - [InvestigationType](docs/InvestigationType.md)
 - [Investigations](docs/Investigations.md)
 - [IocObject](docs/IocObject.md)
 - [IocObjects](docs/IocObjects.md)
 - [Label](docs/Label.md)
 - [Location](docs/Location.md)
 - [Locations](docs/Locations.md)
 - [ModuleArgs](docs/ModuleArgs.md)
 - [NewDockerImage](docs/NewDockerImage.md)
 - [NewDockerImageResult](docs/NewDockerImageResult.md)
 - [NotifiableItem](docs/NotifiableItem.md)
 - [NotifyTimings](docs/NotifyTimings.md)
 - [OperatorArgument](docs/OperatorArgument.md)
 - [Order](docs/Order.md)
 - [Output](docs/Output.md)
 - [OutputType](docs/OutputType.md)
 - [Period](docs/Period.md)
 - [PlaybookInput](docs/PlaybookInput.md)
 - [PlaybookInputs](docs/PlaybookInputs.md)
 - [PlaybookOutput](docs/PlaybookOutput.md)
 - [PlaybookOutputs](docs/PlaybookOutputs.md)
 - [PlaybookView](docs/PlaybookView.md)
 - [Question](docs/Question.md)
 - [RawMessage](docs/RawMessage.md)
 - [RemoteRepos](docs/RemoteRepos.md)
 - [Report](docs/Report.md)
 - [ReportAutomation](docs/ReportAutomation.md)
 - [ReportFieldsDecoder](docs/ReportFieldsDecoder.md)
 - [ReportQuery](docs/ReportQuery.md)
 - [ReputationCalcAlg](docs/ReputationCalcAlg.md)
 - [ReputationData](docs/ReputationData.md)
 - [RunStatus](docs/RunStatus.md)
 - [SLA](docs/SLA.md)
 - [SLAState](docs/SLAState.md)
 - [ScriptSubType](docs/ScriptSubType.md)
 - [ScriptTarget](docs/ScriptTarget.md)
 - [ScriptType](docs/ScriptType.md)
 - [SearchIncidentsData](docs/SearchIncidentsData.md)
 - [Section](docs/Section.md)
 - [SectionItem](docs/SectionItem.md)
 - [Severity](docs/Severity.md)
 - [StatsQueryResponse](docs/StatsQueryResponse.md)
 - [StatsTextResponse](docs/StatsTextResponse.md)
 - [StatsTrendsResponse](docs/StatsTrendsResponse.md)
 - [System](docs/System.md)
 - [SystemAgent](docs/SystemAgent.md)
 - [Task](docs/Task.md)
 - [TaskCondition](docs/TaskCondition.md)
 - [TaskLoop](docs/TaskLoop.md)
 - [TaskState](docs/TaskState.md)
 - [TaskType](docs/TaskType.md)
 - [TaskView](docs/TaskView.md)
 - [TermLocationMap](docs/TermLocationMap.md)
 - [TerminalOptions](docs/TerminalOptions.md)
 - [TimerAction](docs/TimerAction.md)
 - [TimerTrigger](docs/TimerTrigger.md)
 - [TransformerOperatorID](docs/TransformerOperatorID.md)
 - [UpdateDataBatch](docs/UpdateDataBatch.md)
 - [UpdateEntry](docs/UpdateEntry.md)
 - [UpdateEntryTags](docs/UpdateEntryTags.md)
 - [UpdateIndicatorReputationData](docs/UpdateIndicatorReputationData.md)
 - [UpdateResponse](docs/UpdateResponse.md)
 - [UploadedEntry](docs/UploadedEntry.md)
 - [Widget](docs/Widget.md)
 - [WidgetCell](docs/WidgetCell.md)
 - [WidgetCells](docs/WidgetCells.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header
