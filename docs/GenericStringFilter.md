# GenericStringFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | **dict(str, list[str])** | Cache of join functions | [optional] 
**page** | **int** | 0-based page | [optional] 
**query** | **str** |  | [optional] 
**search_after** | **list[str]** | Efficient next page, pass max sort value from previous page | [optional] 
**search_before** | **list[str]** | Efficient prev page, pass min sort value from next page | [optional] 
**size** | **int** | Size is limited to 1000, if not passed it defaults to 0, and no results will return | [optional] 
**sort** | [**list[Order]**](Order.md) | The sort order | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


