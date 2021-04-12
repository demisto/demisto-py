# Playbook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brands** | **list[str]** |  | [optional] 
**commands** | **list[str]** |  | [optional] 
**comment** | **str** |  | [optional] 
**commit_message** | **str** |  | [optional] 
**dbot_created_by** | **str** | Who has created this event - relevant only for manual incidents | [optional] 
**detached** | **bool** |  | [optional] 
**from_server_version** | [**Version**](Version.md) |  | [optional] 
**has_role** | **bool** | Internal field to make queries on role faster | [optional] 
**hidden** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**inputs** | [**PlaybookInputs**](PlaybookInputs.md) |  | [optional] 
**item_version** | [**Version**](Version.md) |  | [optional] 
**locked** | **bool** |  | [optional] 
**missing_scripts_ids** | **list[str]** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**name_raw** | **str** |  | [optional] 
**outputs** | [**PlaybookOutputs**](PlaybookOutputs.md) |  | [optional] 
**pack_id** | **str** |  | [optional] 
**prev_name** | **str** |  | [optional] 
**previous_roles** | **list[str]** | PreviousRoleName - do not change this field manually | [optional] 
**primary_term** | **int** |  | [optional] 
**private** | **bool** |  | [optional] 
**propagation_labels** | **list[str]** |  | [optional] 
**quiet** | **bool** |  | [optional] 
**roles** | **list[str]** | The role assigned to this investigation | [optional] 
**script_ids** | **list[str]** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**should_commit** | **bool** |  | [optional] 
**sort_values** | **list[str]** |  | [optional] 
**source_playbook_id** | **str** |  | [optional] 
**start_task_id** | **str** |  | [optional] 
**system** | **bool** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**task_ids** | **list[str]** | auto generated field that will contain all task ids in this playbook Needed for searching with bleve | [optional] 
**tasks** | [**dict(str, PlaybookTask)**](PlaybookTask.md) |  | [optional] 
**to_server_version** | [**Version**](Version.md) |  | [optional] 
**vc_should_ignore** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 
**view** | [**PlaybookView**](PlaybookView.md) |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


