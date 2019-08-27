# InvestigationPlaybook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dirty** | **bool** |  | [optional] 
**ready_playbook_inputs** | **dict(str, dict(str, object))** |  | [optional] 
**replaced_playbook** | **bool** | Indicate whether this playbook has new history during this session | [optional] 
**shard_id** | **int** |  | [optional] 
**updated_operator_i_ds** | **bool** |  | [optional] 
**auto_extracting** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 
**has_role** | **bool** | Internal field to make queries on role faster | [optional] 
**id** | **str** |  | [optional] 
**incident_create_date** | **datetime** | Incident create date | [optional] 
**inputs** | [**PlaybookInputs**](PlaybookInputs.md) |  | [optional] 
**investigation_id** | **str** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**outputs** | [**PlaybookOutputs**](PlaybookOutputs.md) |  | [optional] 
**pb_history** | [**list[InvestigationPlaybookData]**](InvestigationPlaybookData.md) | in: body | [optional] 
**playbook_id** | **str** |  | [optional] 
**previous_roles** | **list[str]** | PreviousRoleName - do not change this field manually | [optional] 
**roles** | **list[str]** | The role assigned to this investigation | [optional] 
**sort_values** | **list[str]** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**start_task_id** | **str** | FirstTask is the root task of the playbook | [optional] 
**state** | [**InvestigationPlaybookState**](InvestigationPlaybookState.md) |  | [optional] 
**sub_playbook_inputs** | [**dict(str, PlaybookInputs)**](PlaybookInputs.md) |  | [optional] 
**sub_playbook_outputs** | [**dict(str, PlaybookOutputs)**](PlaybookOutputs.md) |  | [optional] 
**tasks** | [**dict(str, InvestigationPlaybookTask)**](InvestigationPlaybookTask.md) |  | [optional] 
**version** | **int** |  | [optional] 
**view** | [**PlaybookView**](PlaybookView.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


