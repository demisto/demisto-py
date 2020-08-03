# PlaybookTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[TaskCondition]**](TaskCondition.md) | Conditions - optional list of conditions to run when task is conditional. we check conditions by their order (e.i. - considering the first one that satisfied) | [optional] 
**continue_on_error** | **bool** |  | [optional] 
**default_assignee** | **str** |  | [optional] 
**default_assignee_complex** | [**AdvanceArg**](AdvanceArg.md) |  | [optional] 
**default_reminder** | **int** |  | [optional] 
**evidence_data** | [**EvidenceData**](EvidenceData.md) |  | [optional] 
**field_mapping** | [**list[FieldMapping]**](FieldMapping.md) |  | [optional] 
**form** | [**DataCollectionForm**](DataCollectionForm.md) |  | [optional] 
**form_display** | [**FormDisplay**](FormDisplay.md) |  | [optional] 
**id** | **str** |  | [optional] 
**ignore_worker** | **bool** | Do not run this task in a worker | [optional] 
**loop** | [**TaskLoop**](TaskLoop.md) |  | [optional] 
**message** | [**NotifiableItem**](NotifiableItem.md) |  | [optional] 
**next_tasks** | **dict(str, list[str])** |  | [optional] 
**note** | **bool** |  | [optional] 
**quiet_mode** | [**QuietMode**](QuietMode.md) |  | [optional] 
**reputation_calc** | [**ReputationCalcAlg**](ReputationCalcAlg.md) |  | [optional] 
**restricted_completion** | **bool** |  | [optional] 
**script_arguments** | [**dict(str, AdvanceArg)**](AdvanceArg.md) |  | [optional] 
**separate_context** | **bool** |  | [optional] 
**skip_unavailable** | **bool** | SkipUnavailable if true then will check if automation exists, integration of that command is installed and active or sub playbook exists in Demisto | [optional] 
**sla** | [**SLA**](SLA.md) |  | [optional] 
**sla_reminder** | [**SLA**](SLA.md) |  | [optional] 
**task** | [**Task**](Task.md) |  | [optional] 
**task_id** | **str** |  | [optional] 
**timer_triggers** | [**list[TimerTrigger]**](TimerTrigger.md) | SLA fields | [optional] 
**type** | [**TaskType**](TaskType.md) |  | [optional] 
**view** | [**TaskView**](TaskView.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


