## Documentation for API Endpoints

All URIs are relative to *https://hostname:443*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_ad_hoc_task**](DefaultApi.md#add_ad_hoc_task) | **POST** /inv-playbook/task/add/{investigationId} | Add ad-hoc task
*DefaultApi* | [**close_incidents_batch**](DefaultApi.md#close_incidents_batch) | **POST** /incident/batchClose | Batch close incidents
*DefaultApi* | [**complete_task**](DefaultApi.md#complete_task) | **POST** /inv-playbook/task/complete | [Deprecated] Complete a task
*DefaultApi* | [**complete_task_v2**](DefaultApi.md#complete_task_v2) | **POST** /v2/inv-playbook/task/complete | Complete a task
*DefaultApi* | [**copy_script**](DefaultApi.md#copy_script) | **POST** /automation/copy | Copy automation
*DefaultApi* | [**create_docker_image**](DefaultApi.md#create_docker_image) | **POST** /settings/docker-images | Create Image
*DefaultApi* | [**create_incident**](DefaultApi.md#create_incident) | **POST** /incident | Create single incident
*DefaultApi* | [**create_incident_json**](DefaultApi.md#create_incident_json) | **POST** /incident/json | Create incident from JSON
*DefaultApi* | [**create_incidents_batch**](DefaultApi.md#create_incidents_batch) | **POST** /incident/batch | Batch create incidents
*DefaultApi* | [**create_or_update_incident_type**](DefaultApi.md#create_or_update_incident_type) | **POST** /incidenttype | Create new Incident Type
*DefaultApi* | [**delete_ad_hoc_task**](DefaultApi.md#delete_ad_hoc_task) | **POST** /inv-playbook/task/delete/{investigationId}/{invPBTaskId} | Delete ad-hoc task
*DefaultApi* | [**delete_automation_script**](DefaultApi.md#delete_automation_script) | **POST** /automation/delete | Delete existing automation
*DefaultApi* | [**delete_evidence_op**](DefaultApi.md#delete_evidence_op) | **POST** /evidence/delete | delete evidence
*DefaultApi* | [**delete_incidents_batch**](DefaultApi.md#delete_incidents_batch) | **POST** /incident/batchDelete | Batch delete incidents
*DefaultApi* | [**delete_indicators_batch**](DefaultApi.md#delete_indicators_batch) | **POST** /indicators/batchDelete | Batch whitelist or delete indicators
*DefaultApi* | [**delete_widget**](DefaultApi.md#delete_widget) | **DELETE** /widgets/{id} | Remove existing widget
*DefaultApi* | [**download_latest_report**](DefaultApi.md#download_latest_report) | **GET** /reports/{id}/latest | Get latest report by ID
*DefaultApi* | [**edit_ad_hoc_task**](DefaultApi.md#edit_ad_hoc_task) | **POST** /inv-playbook/task/edit/{investigationId} | Edit ad-hoc task
*DefaultApi* | [**entry_export_artifact**](DefaultApi.md#entry_export_artifact) | **POST** /entry/exportArtifact | Export Artifact
*DefaultApi* | [**execute_report**](DefaultApi.md#execute_report) | **POST** /report/{id}/{requestId}/execute | Execute report
*DefaultApi* | [**export_incidents_to_csv_batch**](DefaultApi.md#export_incidents_to_csv_batch) | **POST** /incident/batch/exportToCsv | Batch export incidents to csv
*DefaultApi* | [**export_indicators_to_csv_batch**](DefaultApi.md#export_indicators_to_csv_batch) | **POST** /indicators/batch/exportToCsv | Batch export indicators to csv
*DefaultApi* | [**export_indicators_to_stix_batch**](DefaultApi.md#export_indicators_to_stix_batch) | **POST** /indicators/batch/export/stix | Batch export indicators to STIX
*DefaultApi* | [**get_all_reports**](DefaultApi.md#get_all_reports) | **GET** /reports | Get all reports
*DefaultApi* | [**get_all_widgets**](DefaultApi.md#get_all_widgets) | **GET** /widgets | 
*DefaultApi* | [**get_audits**](DefaultApi.md#get_audits) | **POST** /settings/audits | Get Audits
*DefaultApi* | [**get_automation_scripts**](DefaultApi.md#get_automation_scripts) | **POST** /automation/search | Search Automation (aka scripts)
*DefaultApi* | [**get_docker_images**](DefaultApi.md#get_docker_images) | **GET** /settings/docker-images | Get Docker Images
*DefaultApi* | [**get_entry_artifact**](DefaultApi.md#get_entry_artifact) | **GET** /entry/artifact/{id} | Get entry artifact
*DefaultApi* | [**get_incident_as_csv**](DefaultApi.md#get_incident_as_csv) | **GET** /incident/csv/{id} | Get incident as CSV
*DefaultApi* | [**get_incidents_fields_by_incident_type**](DefaultApi.md#get_incidents_fields_by_incident_type) | **GET** /incidentfields/associatedTypes/{type} | Get all incident fields associated with incident type
*DefaultApi* | [**get_indicators_as_csv**](DefaultApi.md#get_indicators_as_csv) | **GET** /indicators/csv/{id} | Get indicators as CSV
*DefaultApi* | [**get_indicators_as_stix**](DefaultApi.md#get_indicators_as_stix) | **GET** /indicators/stix/v2/{id} | Get indicators as STIX V2
*DefaultApi* | [**get_report_by_id**](DefaultApi.md#get_report_by_id) | **GET** /reports/{id} | Get report by ID
*DefaultApi* | [**get_stats_for_dashboard**](DefaultApi.md#get_stats_for_dashboard) | **POST** /statistics/dashboards/query | Get Dashboard Statistics
*DefaultApi* | [**get_stats_for_widget**](DefaultApi.md#get_stats_for_widget) | **POST** /statistics/widgets/query | Get Widget Statistics
*DefaultApi* | [**get_widget**](DefaultApi.md#get_widget) | **GET** /widgets/{id} | Get widget by ID
*DefaultApi* | [**import_widget**](DefaultApi.md#import_widget) | **POST** /widgets/import | Import a widget
*DefaultApi* | [**indicator_whitelist**](DefaultApi.md#indicator_whitelist) | **POST** /indicator/whitelist | Whitelists or deletes Indicator
*DefaultApi* | [**indicators_create**](DefaultApi.md#indicators_create) | **POST** /indicator/create | Create Indicator
*DefaultApi* | [**indicators_create_batch**](DefaultApi.md#indicators_create_batch) | **POST** /indicators/upload | Create indicators
*DefaultApi* | [**indicators_edit**](DefaultApi.md#indicators_edit) | **POST** /indicator/edit | Edit Indicator
*DefaultApi* | [**indicators_search**](DefaultApi.md#indicators_search) | **POST** /indicators/search | Search indicators
*DefaultApi* | [**investigation_add_entry_handler**](DefaultApi.md#investigation_add_entry_handler) | **POST** /entry | Create new entry in existing investigation
*DefaultApi* | [**investigation_add_formatted_entry_handler**](DefaultApi.md#investigation_add_formatted_entry_handler) | **POST** /entry/formatted | Create new formatted entry in existing investigation
*DefaultApi* | [**revoke_user_api_key**](DefaultApi.md#revoke_user_api_key) | **POST** /apikeys/revoke/user/{username} | 
*DefaultApi* | [**save_evidence**](DefaultApi.md#save_evidence) | **POST** /evidence | Save evidence
*DefaultApi* | [**save_or_update_script**](DefaultApi.md#save_or_update_script) | **POST** /automation | Create or update automation
*DefaultApi* | [**save_widget**](DefaultApi.md#save_widget) | **POST** /widgets | Add or update a widget
*DefaultApi* | [**search_evidence**](DefaultApi.md#search_evidence) | **POST** /evidence/search | Search evidence
*DefaultApi* | [**search_incidents**](DefaultApi.md#search_incidents) | **POST** /incidents/search | Search incidents by filter
*DefaultApi* | [**search_investigations**](DefaultApi.md#search_investigations) | **POST** /investigations/search | Search investigations by filter
*DefaultApi* | [**simple_complete_task**](DefaultApi.md#simple_complete_task) | **POST** /inv-playbook/task/complete/simple | Complete task simple (no file)
*DefaultApi* | [**submit_task_form**](DefaultApi.md#submit_task_form) | **POST** /v2/inv-playbook/task/form/submit | Complete a task
*DefaultApi* | [**task_add_comment**](DefaultApi.md#task_add_comment) | **POST** /inv-playbook/task/note/add | Task add comment
*DefaultApi* | [**task_assign**](DefaultApi.md#task_assign) | **POST** /inv-playbook/task/assign | Assign task
*DefaultApi* | [**task_set_due**](DefaultApi.md#task_set_due) | **POST** /inv-playbook/task/due | Set task due date
*DefaultApi* | [**task_un_complete**](DefaultApi.md#task_un_complete) | **POST** /inv-playbook/task/uncomplete | Un complete a task
*DefaultApi* | [**update_entry_note**](DefaultApi.md#update_entry_note) | **POST** /entry/note | Mark entry as note
*DefaultApi* | [**update_entry_tags_op**](DefaultApi.md#update_entry_tags_op) | **POST** /entry/tags | Set entry tags


## Documentation For Models

 - [AdvanceArg](AdvanceArg.md)
 - [ArgAtomicFilter](ArgAtomicFilter.md)
 - [ArgFilter](ArgFilter.md)
 - [ArgTransformer](ArgTransformer.md)
 - [Argument](Argument.md)
 - [ArrayPositions](ArrayPositions.md)
 - [Attachment](Attachment.md)
 - [Audit](Audit.md)
 - [AuditResult](AuditResult.md)
 - [AutomationScript](AutomationScript.md)
 - [AutomationScriptAPI](AutomationScriptAPI.md)
 - [AutomationScriptFilter](AutomationScriptFilter.md)
 - [AutomationScriptFilterWrapper](AutomationScriptFilterWrapper.md)
 - [AutomationScriptResult](AutomationScriptResult.md)
 - [ComplexArg](ComplexArg.md)
 - [CreateIncidentRequest](CreateIncidentRequest.md)
 - [CustomFields](CustomFields.md)
 - [DBotScore](DBotScore.md)
 - [Dashboard](Dashboard.md)
 - [DataCollectionForm](DataCollectionForm.md)
 - [DateRange](DateRange.md)
 - [DateRangeFilter](DateRangeFilter.md)
 - [DeleteEvidence](DeleteEvidence.md)
 - [DockerImage](DockerImage.md)
 - [DockerImagesResult](DockerImagesResult.md)
 - [DownloadEntry](DownloadEntry.md)
 - [Duration](Duration.md)
 - [EndingType](EndingType.md)
 - [Entry](Entry.md)
 - [EntryCategory](EntryCategory.md)
 - [EntryHistory](EntryHistory.md)
 - [EntryReputation](EntryReputation.md)
 - [EntryTask](EntryTask.md)
 - [EntryType](EntryType.md)
 - [Evidence](Evidence.md)
 - [EvidenceData](EvidenceData.md)
 - [Evidences](Evidences.md)
 - [EvidencesFilterWrapper](EvidencesFilterWrapper.md)
 - [EvidencesSearchResponse](EvidencesSearchResponse.md)
 - [FieldGroup](FieldGroup.md)
 - [FieldMapping](FieldMapping.md)
 - [FieldTermLocationMap](FieldTermLocationMap.md)
 - [FileMetadata](FileMetadata.md)
 - [FilterCache](FilterCache.md)
 - [FilterOperatorID](FilterOperatorID.md)
 - [GenericIndicatorUpdateBatch](GenericIndicatorUpdateBatch.md)
 - [GenericStringDateFilter](GenericStringDateFilter.md)
 - [GenericStringFilter](GenericStringFilter.md)
 - [GridColumn](GridColumn.md)
 - [Group](Group.md)
 - [Groups](Groups.md)
 - [HumanCron](HumanCron.md)
 - [Important](Important.md)
 - [Incident](Incident.md)
 - [IncidentField](IncidentField.md)
 - [IncidentFilter](IncidentFilter.md)
 - [IncidentSearchResponseWrapper](IncidentSearchResponseWrapper.md)
 - [IncidentStatus](IncidentStatus.md)
 - [IncidentType](IncidentType.md)
 - [IncidentWrapper](IncidentWrapper.md)
 - [IndicatorContext](IndicatorContext.md)
 - [IndicatorFilter](IndicatorFilter.md)
 - [IndicatorResult](IndicatorResult.md)
 - [InlineResponse200](InlineResponse200.md)
 - [InsightCache](InsightCache.md)
 - [InvPlaybookAssignee](InvPlaybookAssignee.md)
 - [InvPlaybookDue](InvPlaybookDue.md)
 - [InvPlaybookTaskCompleteData](InvPlaybookTaskCompleteData.md)
 - [InvPlaybookTaskData](InvPlaybookTaskData.md)
 - [InvTaskInfo](InvTaskInfo.md)
 - [Investigation](Investigation.md)
 - [InvestigationFilter](InvestigationFilter.md)
 - [InvestigationPlaybook](InvestigationPlaybook.md)
 - [InvestigationPlaybookData](InvestigationPlaybookData.md)
 - [InvestigationPlaybookState](InvestigationPlaybookState.md)
 - [InvestigationPlaybookTask](InvestigationPlaybookTask.md)
 - [InvestigationPlaybookTasksAPI](InvestigationPlaybookTasksAPI.md)
 - [InvestigationSearchResponse](InvestigationSearchResponse.md)
 - [InvestigationStatus](InvestigationStatus.md)
 - [InvestigationType](InvestigationType.md)
 - [Investigations](Investigations.md)
 - [IocObject](IocObject.md)
 - [IocObjects](IocObjects.md)
 - [Label](Label.md)
 - [Location](Location.md)
 - [Locations](Locations.md)
 - [ModuleArgs](ModuleArgs.md)
 - [NewDockerImage](NewDockerImage.md)
 - [NewDockerImageResult](NewDockerImageResult.md)
 - [NotifiableItem](NotifiableItem.md)
 - [NotifyTimings](NotifyTimings.md)
 - [OperatorArgument](OperatorArgument.md)
 - [Order](Order.md)
 - [Output](Output.md)
 - [OutputType](OutputType.md)
 - [Period](Period.md)
 - [PlaybookInput](PlaybookInput.md)
 - [PlaybookInputs](PlaybookInputs.md)
 - [PlaybookOutput](PlaybookOutput.md)
 - [PlaybookOutputs](PlaybookOutputs.md)
 - [PlaybookView](PlaybookView.md)
 - [Question](Question.md)
 - [RawMessage](RawMessage.md)
 - [RemoteRepos](RemoteRepos.md)
 - [Report](Report.md)
 - [ReportAutomation](ReportAutomation.md)
 - [ReportFieldsDecoder](ReportFieldsDecoder.md)
 - [ReportQuery](ReportQuery.md)
 - [ReputationCalcAlg](ReputationCalcAlg.md)
 - [ReputationData](ReputationData.md)
 - [RunStatus](RunStatus.md)
 - [SLA](SLA.md)
 - [SLAState](SLAState.md)
 - [ScriptSubType](ScriptSubType.md)
 - [ScriptTarget](ScriptTarget.md)
 - [ScriptType](ScriptType.md)
 - [SearchIncidentsData](SearchIncidentsData.md)
 - [Section](Section.md)
 - [SectionItem](SectionItem.md)
 - [Severity](Severity.md)
 - [StatsQueryResponse](StatsQueryResponse.md)
 - [StatsTextResponse](StatsTextResponse.md)
 - [StatsTrendsResponse](StatsTrendsResponse.md)
 - [System](System.md)
 - [SystemAgent](SystemAgent.md)
 - [Task](Task.md)
 - [TaskCondition](TaskCondition.md)
 - [TaskLoop](TaskLoop.md)
 - [TaskState](TaskState.md)
 - [TaskType](TaskType.md)
 - [TaskView](TaskView.md)
 - [TermLocationMap](TermLocationMap.md)
 - [TerminalOptions](TerminalOptions.md)
 - [TimerAction](TimerAction.md)
 - [TimerTrigger](TimerTrigger.md)
 - [TransformerOperatorID](TransformerOperatorID.md)
 - [UpdateDataBatch](UpdateDataBatch.md)
 - [UpdateEntry](UpdateEntry.md)
 - [UpdateEntryTags](UpdateEntryTags.md)
 - [UpdateIndicatorReputationData](UpdateIndicatorReputationData.md)
 - [UpdateResponse](UpdateResponse.md)
 - [UploadedEntry](UploadedEntry.md)
 - [Widget](Widget.md)
 - [WidgetCell](WidgetCell.md)
 - [WidgetCells](WidgetCells.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



