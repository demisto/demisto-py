# Evidence

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_id** | **int** |  | [optional] 
**all_read** | **bool** |  | [optional] 
**all_read_write** | **bool** |  | [optional] 
**dbot_created_by** | **str** | Who has created this event - relevant only for manual incidents | [optional] 
**description** | **str** | The description for the resolve | [optional] 
**entry_id** | **str** | The entry ID | [optional] 
**fetched** | **datetime** | when the evidence entry was fetched | [optional] 
**has_role** | **bool** | Internal field to make queries on role faster | [optional] 
**highlight** | **dict(str, list[str])** |  | [optional] 
**id** | **str** |  | [optional] 
**incident_id** | **str** | The incident ID | [optional] 
**marked_by** | **str** | the user that marked this evidence | [optional] 
**marked_date** | **datetime** | when this evidence was marked | [optional] 
**modified** | **datetime** |  | [optional] 
**numeric_id** | **int** |  | [optional] 
**occurred** | **datetime** | When this evidence has occurred | [optional] 
**previous_all_read** | **bool** |  | [optional] 
**previous_all_read_write** | **bool** |  | [optional] 
**previous_roles** | **list[str]** | Do not change this field manually | [optional] 
**primary_term** | **int** |  | [optional] 
**roles** | **list[str]** | The role assigned to this investigation | [optional] 
**sequence_number** | **int** |  | [optional] 
**sort_values** | **list[str]** |  | [optional] 
**tags** | **list[str]** | Tags | [optional] 
**tags_raw** | **list[str]** | TagsRaw | [optional] 
**task_id** | **str** | when the evidence entry was fetched | [optional] 
**version** | **int** |  | [optional] 
**xsoar_has_read_only_role** | **bool** |  | [optional] 
**xsoar_previous_read_only_roles** | **list[str]** |  | [optional] 
**xsoar_read_only_roles** | **list[str]** |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


