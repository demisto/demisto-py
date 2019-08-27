# InvestigationFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | **dict(str, list[str])** | Cache of join functions | [optional] 
**and_op** | **bool** |  | [optional] 
**category** | **list[str]** |  | [optional] 
**from_close_date** | **datetime** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**from_date_license** | **datetime** |  | [optional] 
**id** | **list[str]** |  | [optional] 
**ids_only** | **bool** |  | [optional] 
**include_child_inv** | **bool** |  | [optional] 
**name** | **list[str]** |  | [optional] 
**not_category** | **list[str]** |  | [optional] 
**not_i_ds** | **list[str]** |  | [optional] 
**page** | **int** | 0-based page | [optional] 
**period** | [**Period**](Period.md) |  | [optional] 
**reason** | **list[str]** |  | [optional] 
**search_after** | **list[str]** | Efficient next page, pass max sort value from previous page | [optional] 
**search_before** | **list[str]** | Efficient prev page, pass min sort value from next page | [optional] 
**size** | **int** | Size is limited to 1000, if not passed it defaults to 0, and no results will return | [optional] 
**sort** | [**list[Order]**](Order.md) | The sort order | [optional] 
**status** | [**list[InvestigationStatus]**](InvestigationStatus.md) |  | [optional] 
**time_frame** | [**Duration**](Duration.md) |  | [optional] 
**to_close_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**type** | [**list[InvestigationType]**](InvestigationType.md) |  | [optional] 
**user** | **list[str]** |  | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


