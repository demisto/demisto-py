## Documentation for API Endpoints

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
[**create_or_update_whitelisted**](DefaultApi.md#create_or_update_whitelisted) | **POST** /indicators/whitelist/update | Create whitelisted
[**delete_ad_hoc_task**](DefaultApi.md#delete_ad_hoc_task) | **POST** /inv-playbook/task/delete/{investigationId}/{invPBTaskId} | Delete ad-hoc task
[**delete_automation_script**](DefaultApi.md#delete_automation_script) | **POST** /automation/delete | Delete existing automation
[**delete_evidence_op**](DefaultApi.md#delete_evidence_op) | **POST** /evidence/delete | delete evidence
[**delete_incidents_batch**](DefaultApi.md#delete_incidents_batch) | **POST** /incident/batchDelete | Batch delete incidents
[**delete_indicators_batch**](DefaultApi.md#delete_indicators_batch) | **POST** /indicators/batchDelete | Batch whitelist or delete indicators
[**delete_widget**](DefaultApi.md#delete_widget) | **DELETE** /widgets/{id} | Remove existing widget
[**download_file**](DefaultApi.md#download_file) | **GET** /entry/download/{entryid} | Download file
[**download_latest_report**](DefaultApi.md#download_latest_report) | **GET** /report/{id}/latest | Get latest report by ID
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
[**get_containers**](DefaultApi.md#get_containers) | **GET** /health/containers | Get health containers
[**get_docker_images**](DefaultApi.md#get_docker_images) | **GET** /settings/docker-images | Get Docker Images
[**get_entry_artifact**](DefaultApi.md#get_entry_artifact) | **GET** /entry/artifact/{id} | Get entry artifact
[**get_incident_as_csv**](DefaultApi.md#get_incident_as_csv) | **GET** /incident/csv/{id} | Get incident as CSV
[**get_incidents_fields_by_incident_type**](DefaultApi.md#get_incidents_fields_by_incident_type) | **GET** /incidentfields/associatedTypes/{type} | Get all incident fields associated with incident type
[**get_indicators_as_csv**](DefaultApi.md#get_indicators_as_csv) | **GET** /indicators/csv/{id} | Get indicators as CSV
[**get_indicators_as_stix**](DefaultApi.md#get_indicators_as_stix) | **GET** /indicators/stix/v2/{id} | Get indicators as STIX V2
[**get_report_by_id**](DefaultApi.md#get_report_by_id) | **GET** /reports/{id} | Get report by ID
[**get_stats_for_dashboard**](DefaultApi.md#get_stats_for_dashboard) | **POST** /v2/statistics/dashboards/query | Get Dashboard Statistics
[**get_stats_for_dashboard_old_format**](DefaultApi.md#get_stats_for_dashboard_old_format) | **POST** /statistics/dashboards/query | [Deprecated] Get Dashboard Statistics
[**get_stats_for_widget**](DefaultApi.md#get_stats_for_widget) | **POST** /v2/statistics/widgets/query | Get Widget Statistics
[**get_stats_for_widget_old_format**](DefaultApi.md#get_stats_for_widget_old_format) | **POST** /statistics/widgets/query | [Deprecated] Get Widget Statistics
[**get_widget**](DefaultApi.md#get_widget) | **GET** /widgets/{id} | Get widget by ID
[**health_handler**](DefaultApi.md#health_handler) | **GET** /health | Check if Cortex XSOAR server is available
[**import_classifier**](DefaultApi.md#import_classifier) | **POST** /classifier/import | Import a classifier
[**import_dashboard**](DefaultApi.md#import_dashboard) | **POST** /dashboards/import | Import a dashboard
[**import_incident_fields**](DefaultApi.md#import_incident_fields) | **POST** /incidentfields/import | Import an incident field
[**import_incident_types_handler**](DefaultApi.md#import_incident_types_handler) | **POST** /incidenttypes/import | Import an incident type
[**import_script**](DefaultApi.md#import_script) | **POST** /automation/import | Import an automation
[**import_widget**](DefaultApi.md#import_widget) | **POST** /widgets/import | Import a widget
[**incident_file_upload**](DefaultApi.md#incident_file_upload) | **POST** /incident/upload/{id} | 
[**indicator_whitelist**](DefaultApi.md#indicator_whitelist) | **POST** /indicator/whitelist | Whitelists or deletes Indicator
[**indicators_create**](DefaultApi.md#indicators_create) | **POST** /indicator/create | Create Indicator
[**indicators_create_batch**](DefaultApi.md#indicators_create_batch) | **POST** /indicators/upload | Create indicators
[**indicators_edit**](DefaultApi.md#indicators_edit) | **POST** /indicator/edit | Edit Indicator
[**indicators_search**](DefaultApi.md#indicators_search) | **POST** /indicators/search | Search indicators
[**indicators_timeline_delete**](DefaultApi.md#indicators_timeline_delete) | **POST** /indicators/timeline/delete | Delete indicators timeline
[**integration_upload**](DefaultApi.md#integration_upload) | **POST** /settings/integration-conf/upload | Upload an integration
[**investigation_add_entries_sync**](DefaultApi.md#investigation_add_entries_sync) | **POST** /entry/execute/sync | Create new entry in existing investigation
[**investigation_add_entry_handler**](DefaultApi.md#investigation_add_entry_handler) | **POST** /entry | Create new entry in existing investigation
[**investigation_add_formatted_entry_handler**](DefaultApi.md#investigation_add_formatted_entry_handler) | **POST** /entry/formatted | Create new formatted entry in existing investigation
[**logout_everyone_handler**](DefaultApi.md#logout_everyone_handler) | **POST** /logout/everyone | Sign out all open users sessions
[**logout_myself_handler**](DefaultApi.md#logout_myself_handler) | **POST** /logout/myself | Sign out all my open sessions
[**logout_myself_other_sessions_handler**](DefaultApi.md#logout_myself_other_sessions_handler) | **POST** /logout/myself/other | Sign out all my other open sessions
[**logout_user_sessions_handler**](DefaultApi.md#logout_user_sessions_handler) | **POST** /logout/user/{username} | Sign out all sessions of the provided username
[**override_playbook_yaml**](DefaultApi.md#override_playbook_yaml) | **POST** /playbook/save/yaml | Import and override playbook
[**reset_roi_widget**](DefaultApi.md#reset_roi_widget) | **DELETE** /statistics/application/roi | Reset ROI widget
[**revoke_user_api_key**](DefaultApi.md#revoke_user_api_key) | **POST** /apikeys/revoke/user/{username} | 
[**save_evidence**](DefaultApi.md#save_evidence) | **POST** /evidence | Save evidence
[**save_or_update_script**](DefaultApi.md#save_or_update_script) | **POST** /automation | Create or update automation
[**save_widget**](DefaultApi.md#save_widget) | **POST** /widgets | Add or update a widget
[**search_evidence**](DefaultApi.md#search_evidence) | **POST** /evidence/search | Search evidence
[**search_incidents**](DefaultApi.md#search_incidents) | **POST** /incidents/search | Search incidents by filter
[**search_investigations**](DefaultApi.md#search_investigations) | **POST** /investigations/search | Search investigations by filter
[**set_tags_field**](DefaultApi.md#set_tags_field) | **POST** /incidentfield/tags/reset/{id} | Set tags field
[**simple_complete_task**](DefaultApi.md#simple_complete_task) | **POST** /inv-playbook/task/complete/simple | Complete task simple (no file)
[**submit_task_form**](DefaultApi.md#submit_task_form) | **POST** /v2/inv-playbook/task/form/submit | Complete a task
[**task_add_comment**](DefaultApi.md#task_add_comment) | **POST** /inv-playbook/task/note/add | Task add comment
[**task_assign**](DefaultApi.md#task_assign) | **POST** /inv-playbook/task/assign | Assign task
[**task_set_due**](DefaultApi.md#task_set_due) | **POST** /inv-playbook/task/due | Set task due date
[**task_un_complete**](DefaultApi.md#task_un_complete) | **POST** /inv-playbook/task/uncomplete | Un complete a task
[**update_entry_note**](DefaultApi.md#update_entry_note) | **POST** /entry/note | Mark entry as note
[**update_entry_tags_op**](DefaultApi.md#update_entry_tags_op) | **POST** /entry/tags | Set entry tags
[**workers_status_handler**](DefaultApi.md#workers_status_handler) | **GET** /workers/status | Get workers status


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
 - [AuthenticateOKBody](AuthenticateOKBody.md)
 - [AutomationScript](AutomationScript.md)
 - [AutomationScriptFilter](AutomationScriptFilter.md)
 - [AutomationScriptFilterWrapper](AutomationScriptFilterWrapper.md)
 - [AutomationScriptResult](AutomationScriptResult.md)
 - [BaseFilter](BaseFilter.md)
 - [Bucket](Bucket.md)
 - [Buckets](Buckets.md)
 - [Command](Command.md)
 - [Comment](Comment.md)
 - [CommentType](CommentType.md)
 - [CommentUpdate](CommentUpdate.md)
 - [Comments](Comments.md)
 - [CommentsFields](CommentsFields.md)
 - [CommonFields](CommonFields.md)
 - [CommonUpdateBatch](CommonUpdateBatch.md)
 - [ComplexArg](ComplexArg.md)
 - [ConfigDataType](ConfigDataType.md)
 - [ConfigField](ConfigField.md)
 - [ContainerChangeResponseItem](ContainerChangeResponseItem.md)
 - [ContainerCreateCreatedBody](ContainerCreateCreatedBody.md)
 - [ContainerTopOKBody](ContainerTopOKBody.md)
 - [ContainerUpdateOKBody](ContainerUpdateOKBody.md)
 - [ContainerWaitOKBody](ContainerWaitOKBody.md)
 - [ContainerWaitOKBodyError](ContainerWaitOKBodyError.md)
 - [ContainersInfo](ContainersInfo.md)
 - [ContentItemExportableFields](ContentItemExportableFields.md)
 - [ContentItemFields](ContentItemFields.md)
 - [ContentItemVersionedFields](ContentItemVersionedFields.md)
 - [CreateIncidentRequest](CreateIncidentRequest.md)
 - [CustomFields](CustomFields.md)
 - [CustomGroup](CustomGroup.md)
 - [CustomGroups](CustomGroups.md)
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
 - [ElasticCommonFields](ElasticCommonFields.md)
 - [ElasticVersionFields](ElasticVersionFields.md)
 - [EndingType](EndingType.md)
 - [Entry](Entry.md)
 - [EntryCategory](EntryCategory.md)
 - [EntryHistory](EntryHistory.md)
 - [EntryReputation](EntryReputation.md)
 - [EntryTask](EntryTask.md)
 - [EntryType](EntryType.md)
 - [ErrorResponse](ErrorResponse.md)
 - [Evidence](Evidence.md)
 - [EvidenceData](EvidenceData.md)
 - [Evidences](Evidences.md)
 - [EvidencesFilterWrapper](EvidencesFilterWrapper.md)
 - [EvidencesSearchResponse](EvidencesSearchResponse.md)
 - [ExpirationIndicator](ExpirationIndicator.md)
 - [ExpirationPolicy](ExpirationPolicy.md)
 - [ExpirationSettingsSource](ExpirationSettingsSource.md)
 - [ExpirationSource](ExpirationSource.md)
 - [ExpirationStatus](ExpirationStatus.md)
 - [ExtractSettingsMode](ExtractSettingsMode.md)
 - [FeedIndicator](FeedIndicator.md)
 - [FeedIndicatorComment](FeedIndicatorComment.md)
 - [FeedIndicatorCommentsFields](FeedIndicatorCommentsFields.md)
 - [FeedIndicators](FeedIndicators.md)
 - [FeedIndicatorsRequest](FeedIndicatorsRequest.md)
 - [FeedMetadata](FeedMetadata.md)
 - [FieldExtractSetting](FieldExtractSetting.md)
 - [FieldGroup](FieldGroup.md)
 - [FieldMapping](FieldMapping.md)
 - [FieldMergeStrategy](FieldMergeStrategy.md)
 - [FieldTermLocationMap](FieldTermLocationMap.md)
 - [FileMetadata](FileMetadata.md)
 - [FilterOperatorID](FilterOperatorID.md)
 - [FormDisplay](FormDisplay.md)
 - [FullVersion](FullVersion.md)
 - [GenericIndicatorUpdateBatch](GenericIndicatorUpdateBatch.md)
 - [GenericStringDateFilter](GenericStringDateFilter.md)
 - [GenericStringFilter](GenericStringFilter.md)
 - [GraphDriverData](GraphDriverData.md)
 - [GridColumn](GridColumn.md)
 - [Group](Group.md)
 - [Groups](Groups.md)
 - [HumanCron](HumanCron.md)
 - [IdResponse](IdResponse.md)
 - [IdVersion](IdVersion.md)
 - [ImageDeleteResponseItem](ImageDeleteResponseItem.md)
 - [ImageSummary](ImageSummary.md)
 - [Important](Important.md)
 - [Incident](Incident.md)
 - [IncidentField](IncidentField.md)
 - [IncidentFieldsWithErrors](IncidentFieldsWithErrors.md)
 - [IncidentFilter](IncidentFilter.md)
 - [IncidentSearchResponseWrapper](IncidentSearchResponseWrapper.md)
 - [IncidentStatus](IncidentStatus.md)
 - [IncidentType](IncidentType.md)
 - [IncidentTypeExtractSettings](IncidentTypeExtractSettings.md)
 - [IncidentTypesWithErrors](IncidentTypesWithErrors.md)
 - [IncidentWrapper](IncidentWrapper.md)
 - [Incidents](Incidents.md)
 - [IndicatorContext](IndicatorContext.md)
 - [IndicatorEditBulkResponse](IndicatorEditBulkResponse.md)
 - [IndicatorFilter](IndicatorFilter.md)
 - [IndicatorResult](IndicatorResult.md)
 - [IndicatorTimeline](IndicatorTimeline.md)
 - [IndicatorTimelineFromEntry](IndicatorTimelineFromEntry.md)
 - [Info](Info.md)
 - [InlineResponse200](InlineResponse200.md)
 - [InsightCache](InsightCache.md)
 - [InstanceClassifier](InstanceClassifier.md)
 - [IntegrationScript](IntegrationScript.md)
 - [InvPlaybookAssignee](InvPlaybookAssignee.md)
 - [InvPlaybookDebugInfo](InvPlaybookDebugInfo.md)
 - [InvPlaybookDue](InvPlaybookDue.md)
 - [InvPlaybookTaskCompleteData](InvPlaybookTaskCompleteData.md)
 - [InvPlaybookTaskData](InvPlaybookTaskData.md)
 - [InvTaskDebug](InvTaskDebug.md)
 - [InvTaskInfo](InvTaskInfo.md)
 - [Investigation](Investigation.md)
 - [InvestigationFilter](InvestigationFilter.md)
 - [InvestigationPlaybook](InvestigationPlaybook.md)
 - [InvestigationPlaybookData](InvestigationPlaybookData.md)
 - [InvestigationPlaybookState](InvestigationPlaybookState.md)
 - [InvestigationPlaybookTask](InvestigationPlaybookTask.md)
 - [InvestigationSearchResponse](InvestigationSearchResponse.md)
 - [InvestigationStatus](InvestigationStatus.md)
 - [InvestigationType](InvestigationType.md)
 - [Investigations](Investigations.md)
 - [IocObject](IocObject.md)
 - [IocObjects](IocObjects.md)
 - [Label](Label.md)
 - [Layout](Layout.md)
 - [LayoutAPI](LayoutAPI.md)
 - [LayoutCommon](LayoutCommon.md)
 - [LayoutField](LayoutField.md)
 - [LayoutSection](LayoutSection.md)
 - [Location](Location.md)
 - [Locations](Locations.md)
 - [Mapper](Mapper.md)
 - [MapperType](MapperType.md)
 - [ModuleArgs](ModuleArgs.md)
 - [ModuleConfiguration](ModuleConfiguration.md)
 - [NewDockerImage](NewDockerImage.md)
 - [NewDockerImageResult](NewDockerImageResult.md)
 - [NotifiableItem](NotifiableItem.md)
 - [NotifyTimings](NotifyTimings.md)
 - [OperatorArgument](OperatorArgument.md)
 - [OperatorType](OperatorType.md)
 - [Order](Order.md)
 - [Output](Output.md)
 - [OutputType](OutputType.md)
 - [Period](Period.md)
 - [Playbook](Playbook.md)
 - [PlaybookInput](PlaybookInput.md)
 - [PlaybookInputQuery](PlaybookInputQuery.md)
 - [PlaybookInputs](PlaybookInputs.md)
 - [PlaybookOutput](PlaybookOutput.md)
 - [PlaybookOutputs](PlaybookOutputs.md)
 - [PlaybookTask](PlaybookTask.md)
 - [PlaybookView](PlaybookView.md)
 - [PlaybookWithWarnings](PlaybookWithWarnings.md)
 - [Plugin](Plugin.md)
 - [PluginConfig](PluginConfig.md)
 - [PluginConfigArgs](PluginConfigArgs.md)
 - [PluginConfigInterface](PluginConfigInterface.md)
 - [PluginConfigLinux](PluginConfigLinux.md)
 - [PluginConfigNetwork](PluginConfigNetwork.md)
 - [PluginConfigRootfs](PluginConfigRootfs.md)
 - [PluginConfigUser](PluginConfigUser.md)
 - [PluginDevice](PluginDevice.md)
 - [PluginEnv](PluginEnv.md)
 - [PluginInterfaceType](PluginInterfaceType.md)
 - [PluginMount](PluginMount.md)
 - [PluginSettings](PluginSettings.md)
 - [Port](Port.md)
 - [ProcessInfo](ProcessInfo.md)
 - [QueryState](QueryState.md)
 - [Question](Question.md)
 - [QuietMode](QuietMode.md)
 - [RBAC](RBAC.md)
 - [RawFeedIndicator](RawFeedIndicator.md)
 - [RelationshipAPI](RelationshipAPI.md)
 - [RelationshipCommonFields](RelationshipCommonFields.md)
 - [RelationshipFilter](RelationshipFilter.md)
 - [RelationshipsAPI](RelationshipsAPI.md)
 - [Reliability](Reliability.md)
 - [Report](Report.md)
 - [ReportAutomation](ReportAutomation.md)
 - [ReportFieldsDecoder](ReportFieldsDecoder.md)
 - [ReportQuery](ReportQuery.md)
 - [ReputationCalcAlg](ReputationCalcAlg.md)
 - [ReputationData](ReputationData.md)
 - [RunStatus](RunStatus.md)
 - [SLA](SLA.md)
 - [SLAState](SLAState.md)
 - [Schedule](Schedule.md)
 - [Scheduler](Scheduler.md)
 - [ScriptAPI](ScriptAPI.md)
 - [ScriptSubType](ScriptSubType.md)
 - [ScriptTarget](ScriptTarget.md)
 - [ScriptType](ScriptType.md)
 - [SearchIncidentsData](SearchIncidentsData.md)
 - [SearchInvestigationsData](SearchInvestigationsData.md)
 - [SearchStats](SearchStats.md)
 - [SearchStatsDeletionResponse](SearchStatsDeletionResponse.md)
 - [SearchStatsResponse](SearchStatsResponse.md)
 - [Section](Section.md)
 - [ServiceUpdateResponse](ServiceUpdateResponse.md)
 - [Severity](Severity.md)
 - [ShardedFields](ShardedFields.md)
 - [StatsQueryError](StatsQueryError.md)
 - [StatsQueryResponse](StatsQueryResponse.md)
 - [StatsQueryResponseWithError](StatsQueryResponseWithError.md)
 - [StatsResponseWithReferenceLine](StatsResponseWithReferenceLine.md)
 - [StatsScatterResponse](StatsScatterResponse.md)
 - [StatsTextResponse](StatsTextResponse.md)
 - [StatsTrendsResponse](StatsTrendsResponse.md)
 - [System](System.md)
 - [SystemAgent](SystemAgent.md)
 - [TagsFieldValues](TagsFieldValues.md)
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
 - [TypeAndKind](TypeAndKind.md)
 - [UnclassifiedCases](UnclassifiedCases.md)
 - [UpdateDataBatch](UpdateDataBatch.md)
 - [UpdateEntry](UpdateEntry.md)
 - [UpdateEntryTags](UpdateEntryTags.md)
 - [UpdateIndicatorBatch](UpdateIndicatorBatch.md)
 - [UpdateIndicatorReputationData](UpdateIndicatorReputationData.md)
 - [UpdateResponse](UpdateResponse.md)
 - [UploadedEntry](UploadedEntry.md)
 - [Version](Version.md)
 - [VersionedCommit](VersionedCommit.md)
 - [Volume](Volume.md)
 - [VolumeUsageData](VolumeUsageData.md)
 - [WhitelistedIndicator](WhitelistedIndicator.md)
 - [Widget](Widget.md)
 - [WidgetCell](WidgetCell.md)
 - [WidgetCells](WidgetCells.md)
 - [WithCustomFields](WithCustomFields.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header






