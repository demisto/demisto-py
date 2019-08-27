# Investigation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_id** | **int** |  | [optional] 
**category** | **str** | Category of the investigation | [optional] 
**child_investigations** | **list[str]** | ChildInvestigations id&#39;s | [optional] 
**closed** | **datetime** | When was this closed | [optional] 
**closing_user_id** | **str** | The user ID that closed this investigation | [optional] 
**created** | **datetime** | When was this created | [optional] 
**creating_user_id** | **str** | The user ID that created this investigation | [optional] 
**details** | **str** | User defined free text details | [optional] 
**entitlements** | **list[str]** | One time entitlements | [optional] 
**entry_users** | **list[str]** | EntryUsers | [optional] 
**has_role** | **bool** | Internal field to make queries on role faster | [optional] 
**id** | **str** |  | [optional] 
**is_child_investigation** | **bool** | IsChildInvestigation | [optional] 
**last_open** | **datetime** |  | [optional] 
**mirror_auto_close** | **dict(str, bool)** | MirrorAutoClose will tell us to close the Chat Module channel if we close investigation | [optional] 
**mirror_types** | **dict(str, str)** | MirrorTypes holds info about mirror direction and message type to be mirrored message type can be either &#39;all&#39; or &#39;chat&#39; direction can be either &#39;FromDemisto&#39;, &#39;ToDemisto&#39; or &#39;Both&#39; if this investigation is mirrored | [optional] 
**modified** | **datetime** |  | [optional] 
**name** | **str** | The name of the investigation, which is unique to the project | [optional] 
**open_duration** | **int** | Duration from open to close time | [optional] 
**parent_investigation** | **str** | ParentInvestigation - parent id, in case this is a child investigation of another investigation | [optional] 
**persistent_entitlements** | **dict(str, str)** | Persistent entitlement per tag. Empty tag will also return an entitlement | [optional] 
**previous_roles** | **list[str]** | PreviousRoleName - do not change this field manually | [optional] 
**raw_category** | **str** |  | [optional] 
**reason** | **dict(str, str)** | The reason for the status (resolve) | [optional] 
**roles** | **list[str]** | The role assigned to this investigation | [optional] 
**run_status** | [**RunStatus**](RunStatus.md) |  | [optional] 
**slack_mirror_auto_close** | **bool** | DEPRECATED - DeprecatedSlackMirrorAutoClose will tell us to close the Slack channel if we close investigation | [optional] 
**slack_mirror_type** | **str** | DEPRECATED - DeprecatedSlackMirrorType holds info about mirror direction and message type to be mirror message type can be either &#39;all&#39; or &#39;chat&#39; direction can be either &#39;demisto2Slack&#39;, &#39;slack2Demisto&#39; or &#39;both&#39; if this investigation is mirrored to Slack | [optional] 
**sort_values** | **list[str]** |  | [optional] 
**status** | [**InvestigationStatus**](InvestigationStatus.md) |  | [optional] 
**systems** | [**list[System]**](System.md) | The systems involved | [optional] 
**tags** | **list[str]** | Tags | [optional] 
**type** | [**InvestigationType**](InvestigationType.md) |  | [optional] 
**users** | **list[str]** | The users who share this investigation | [optional] 
**version** | **int** |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


